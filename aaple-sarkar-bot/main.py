"""
Sarkar Mitra (सरकार मित्र) — Aaple Sarkar AI Assistant
FastAPI Backend: High-Performance Localhost AI Bot with RAG & Gemini Integration
"""

import os
import json
import base64
import logging
import time
from typing import Optional
from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse, FileResponse, Response
import pathlib
from pydantic import BaseModel
from dotenv import load_dotenv
from google import genai
from knowledge_base import search_knowledge_base, generate_smart_fallback, SCHEMES_DATA

load_dotenv()

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s"
)
logger = logging.getLogger("sarkar-mitra")

app = FastAPI(
    title="Sarkar Mitra — Aaple Sarkar AI",
    description="Voice-first Marathi & Multilingual Citizen AI Assistant for Maharashtra Government Services",
    version="2.5.0"
)

STATIC_DIR = pathlib.Path(__file__).parent / "static"
app.mount("/static", StaticFiles(directory=str(STATIC_DIR)), name="static")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ─── Gemini Client Setup ──────────────────────────────────────────────────────
_client = None

def is_valid_gemini_key(key: Optional[str]) -> bool:
    if not key:
        return False
    key = key.strip()
    if key in ("your_gemini_api_key_here", "placeholder", "test", ""):
        return False
    # Valid keys usually start with AIzaSy and are at least 30 chars
    return len(key) >= 20 and not key.startswith("AQ.")

def get_client() -> Optional[genai.Client]:
    global _client
    key = os.getenv("GEMINI_API_KEY") or os.getenv("GOOGLE_API_KEY", "")
    if not is_valid_gemini_key(key):
        return None
    if _client is None:
        try:
            _client = genai.Client(api_key=key.strip())
            logger.info("✅ Gemini Client initialized successfully with API key.")
        except Exception as e:
            logger.warning(f"Failed to initialize Gemini Client: {e}")
            _client = None
    return _client

SYSTEM_INSTRUCTION = """You are "Sarkar Mitra" (सरकार मित्र), the official AI assistant for Aaple Sarkar (आपले सरकार - Govt of Maharashtra).
Your mission is to empower rural and urban citizens, farmers, women, and students across Maharashtra by providing accurate, clear, and direct answers about state and central welfare schemes.

Guidelines:
1. Dual-Language Requirement (Bilingual):
   - ALWAYS provide the primary answer in the requested language (e.g. fluent, respectful Marathi).
   - IMMEDIATELY following the Marathi/primary answer, ALWAYS include a dedicated, clear English section:
     ---
     🌐 **English Translation & Summary:**
     • **Overview:** [Brief 1-2 sentence English summary]
     • **Benefits:** [Exact financial benefits / subsidies]
     • **Eligibility Criteria:** [Key eligibility bullet points]
     • **Required Documents:** [Key documents checklist]
     • **How to Apply:** [Step or official link]
     • **Helpline:** [Official toll-free number]
   - If the user asks directly in English, provide the full English answer, followed by a brief "मराठी सारांश (Marathi Summary)".
2. Structure your answers:
   - Clear sections with bold headers.
   - Benefits (मिळणारा लाभ) with exact amounts/subsidies.
   - Eligibility Checklist (पात्रता निकष).
   - Required Documents (आवश्यक कागदपत्रे).
   - How to apply & Official Link.
   - Official 24x7 Helpline numbers.
3. Strict Grounding:
   - Use the provided verified Aaple Sarkar knowledge base context.
   - Never fabricate scheme amounts, dates, or criteria.
   - Emphasize that citizens do not need middlemen and can apply via Aaple Sarkar or visit Maha e-Seva Kendras.
4. Emojis: Use tasteful icons (🏛️, ✅, 📋, 💰, 📞, 🌾)."""


# ─── Pydantic Models ──────────────────────────────────────────────────────────
class ChatMessage(BaseModel):
    message: str
    language: Optional[str] = "auto"
    previous_interaction_id: Optional[str] = None

class ChatResponse(BaseModel):
    reply: str
    schemes_found: list
    interaction_id: Optional[str] = None
    suggestions: list
    mode: str  # "gemini" or "knowledge_base"

class AudioMessage(BaseModel):
    audio_base64: str
    mime_type: str = "audio/webm"

class ApiKeyUpdate(BaseModel):
    api_key: str


# ─── Routes ───────────────────────────────────────────────────────────────────
@app.get("/favicon.ico", include_in_schema=False)
async def favicon():
    svg_icon = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100"><text y=".9em" font-size="90">🏛️</text></svg>'
    return Response(content=svg_icon, media_type="image/svg+xml")

@app.get("/", response_class=HTMLResponse)
async def root():
    index_file = STATIC_DIR / "index.html"
    if index_file.exists():
        return FileResponse(str(index_file))
    return HTMLResponse("<h1>Sarkar Mitra backend is running! static/index.html not found.</h1>")

@app.get("/health")
async def health():
    key = os.getenv("GEMINI_API_KEY", "")
    has_valid_key = is_valid_gemini_key(key)
    return {
        "status": "healthy",
        "service": "Sarkar Mitra Localhost Assistant",
        "version": "2.5.0",
        "gemini_ready": has_valid_key,
        "schemes_loaded": len(SCHEMES_DATA)
    }

@app.post("/api/set-key")
async def set_api_key(req: ApiKeyUpdate):
    """Allows setting the Gemini API key directly from the browser UI."""
    global _client
    key = req.api_key.strip()
    if not is_valid_gemini_key(key):
        raise HTTPException(status_code=400, detail="Invalid API key format. Key should start with 'AIzaSy'.")
    
    os.environ["GEMINI_API_KEY"] = key
    _client = None  # Reset client
    
    # Save to .env file
    env_path = pathlib.Path(__file__).parent / ".env"
    try:
        lines = []
        if env_path.exists():
            with open(env_path, "r", encoding="utf-8") as f:
                lines = f.readlines()
        
        found = False
        new_lines = []
        for line in lines:
            if line.startswith("GEMINI_API_KEY="):
                new_lines.append(f"GEMINI_API_KEY={key}\n")
                found = True
            else:
                new_lines.append(line)
        if not found:
            new_lines.append(f"GEMINI_API_KEY={key}\n")
            
        with open(env_path, "w", encoding="utf-8") as f:
            f.writelines(new_lines)
            
        return {"success": True, "message": "Gemini API key updated successfully."}
    except Exception as e:
        logger.error(f"Error saving .env: {e}")
        return {"success": True, "message": "API key set in memory for this session."}

@app.post("/api/chat", response_model=ChatResponse)
async def chat(request: ChatMessage):
    """
    Main Chat API:
    1. Performs high-speed localized RAG match from SCHEMES_DATA.
    2. If Gemini API is available and key is valid, invokes Gemini 3.8 Flash with full RAG grounding.
    3. If Gemini is unavailable, rate-limited, or offline, seamlessly produces a structured, rich fallback.
    """
    query = request.message.strip()
    if not query:
        raise HTTPException(status_code=400, detail="Message cannot be empty.")

    # 1. RAG Search
    relevant_schemes = search_knowledge_base(query)

    # 2. Try Gemini Generative AI
    client = get_client()
    if client:
        try:
            rag_context = ""
            if relevant_schemes:
                rag_context = "\n\n=== VERIFIED STATE SCHEMES KNOWLEDGE BASE ===\n"
                for s in relevant_schemes:
                    rag_context += f"\nScheme: {s['title']} ({s['title_mr']})\n"
                    rag_context += f"Category: {s['category']}\n"
                    rag_context += f"Description: {s['description']}\n"
                    rag_context += f"Marathi: {s['description_mr']}\n"
                    rag_context += f"Benefits: {s['benefits']} | Marathi: {s['benefits_mr']}\n"
                    rag_context += f"Eligibility: {'; '.join(s['eligibility'])}\n"
                    rag_context += f"Eligibility (MR): {'; '.join(s['eligibility_mr'])}\n"
                    rag_context += f"Documents: {'; '.join(s['documents'])}\n"
                    rag_context += f"Apply Link: {s['apply_link']} | Helpline: {s['helpline']}\n"
                    rag_context += "---\n"

            prompt = (
                f"{SYSTEM_INSTRUCTION}\n"
                f"{rag_context}\n\n"
                f"User Question: {query}\n"
                f"Preferred Language: {request.language}\n"
                f"Please provide an accurate, clear, and direct response following the guidelines."
            )

            call_params = {
                "model": "gemini-3.8-flash",
                "input": prompt
            }
            if request.previous_interaction_id:
                call_params["previous_interaction_id"] = request.previous_interaction_id

            interaction = None
            for attempt in range(2):
                try:
                    interaction = client.interactions.create(**call_params)
                    break
                except Exception as ex:
                    ex_str = str(ex)
                    if "429" in ex_str or "RESOURCE_EXHAUSTED" in ex_str:
                        logger.warning(f"Gemini 429 rate limit hit. Waiting 3s (attempt {attempt+1})")
                        time.sleep(3)
                    else:
                        logger.warning(f"Gemini API error: {ex}")
                        break

            if interaction and interaction.output_text:
                return ChatResponse(
                    reply=interaction.output_text,
                    schemes_found=_clean_schemes(relevant_schemes),
                    interaction_id=interaction.id,
                    suggestions=_generate_suggestions(query, relevant_schemes),
                    mode="gemini"
                )
        except Exception as e:
            logger.error(f"Fallback triggered due to Gemini error: {e}")

    # 3. Robust High-Fidelity Fallback
    fallback_text, matched = generate_smart_fallback(query, request.language or "auto")
    return ChatResponse(
        reply=fallback_text,
        schemes_found=_clean_schemes(relevant_schemes or matched),
        interaction_id=None,
        suggestions=_generate_suggestions(query, relevant_schemes or matched),
        mode="knowledge_base"
    )

@app.post("/api/transcribe")
async def transcribe_audio(request: AudioMessage):
    """Transcribes audio using Gemini 3.8 Flash multimodal if key is active."""
    client = get_client()
    if not client:
        return {
            "text": "",
            "success": False,
            "message": "Voice recognition requires a valid Gemini API key in .env. Please type your query."
        }
    
    try:
        audio_data = base64.b64decode(request.audio_base64)
        interaction = client.interactions.create(
            model="gemini-3.8-flash",
            input=[
                {
                    "type": "text",
                    "text": "Transcribe this audio recording accurately. The speaker might be speaking Marathi, Hindi, or English. Return ONLY the transcribed text without quotes or explanations."
                },
                {
                    "type": "audio",
                    "data": base64.b64encode(audio_data).decode(),
                    "mime_type": request.mime_type
                }
            ]
        )
        transcribed = (interaction.output_text or "").strip()
        return {"text": transcribed, "success": True}
    except Exception as e:
        logger.error(f"Transcription error: {e}")
        return {"text": "", "success": False, "message": str(e)}

@app.get("/api/schemes")
async def get_all_schemes():
    """Returns the list of all available government schemes."""
    return {"schemes": _clean_schemes(SCHEMES_DATA)}

@app.get("/api/scheme/{scheme_id}")
async def get_single_scheme(scheme_id: str):
    scheme = next((s for s in SCHEMES_DATA if s["id"] == scheme_id), None)
    if not scheme:
        raise HTTPException(status_code=404, detail="Scheme not found")
    return scheme


# ─── Helper Functions ─────────────────────────────────────────────────────────
def _clean_schemes(schemes: list) -> list:
    return [{
        "id": s["id"],
        "title": s["title"],
        "title_mr": s["title_mr"],
        "category": s["category"],
        "benefits": s["benefits"],
        "benefits_mr": s.get("benefits_mr", ""),
        "apply_link": s["apply_link"],
        "helpline": s["helpline"]
    } for s in schemes]

def _generate_suggestions(query: str, schemes: list) -> list:
    q = query.lower()
    if "pm kisan" in q or "किसान" in q or "शेती" in q:
        return [
            "नमो शेतकरी महासन्मान निधी काय आहे?",
            "७/१२ व ८-अ डिजिटल उतारा कसा काढायचा?",
            "पीक कर्जमाफी ₹२ लाखांची माहिती द्या",
            "शेती अवजारे ट्रॅक्टर अनुदान योजना"
        ]
    elif "ladki bahin" in q or "लाडकी बहीण" in q or "महिला" in q:
        return [
            "लाडकी बहीण योजनेसाठी लागणारे हमीपत्र",
            "अर्जाची स्थिती (DBT Status) कशी तपासायची?",
            "रेशन कार्डवर लाडकी बहीणचा लाभ मिळतो का?",
            "संजय गांधी निराधार योजना काय आहे?"
        ]
    elif "7/12" in q or "सातबारा" in q or "उतारा" in q or "जमीन" in q:
        return [
            "डिजिटल स्वाक्षरीत ७/१२ डाउनलोड कसा करायचा?",
            "८-अ उतारा म्हणजे काय?",
            "तलाठी कार्यालयात न जाता ७/१२ कसा मिळतो?",
            "पीएम किसानसाठी ७/१२ लागतो का?"
        ]
    elif "ration" in q or "रेशन" in q or "अन्न" in q:
        return [
            "नवीन रेशन कार्डसाठी आवश्यक कागदपत्रे",
            "अंत्योदय आणि BPL रेशन कार्डमध्ये काय फरक आहे?",
            "रास्त भाव दुकानात मोफत धान्य मिळते का?",
            "तहसीलदार उत्पन्न दाखला कसा काढायचा?"
        ]
    elif "दाखला" in q or "certificate" in q or "उत्पन्न" in q:
        return [
            "तहसीलदार उत्पन्न दाखला (१ व ३ वर्ष)",
            "अधिवास (Domicile) प्रमाणपत्र कसे काढायचे?",
            "जात प्रमाणपत्र (Caste Certificate) नियम",
            "आपले सरकार पोर्टलवर नोंदणी कशी करावी?"
        ]
    return [
        "🌾 पीएम किसान योजना माहिती",
        "👩 लाडकी बहीण योजना ₹१,५००",
        "📄 डिजिटल ७/१२ उतारा कसा काढायचा?",
        "🍚 रेशन कार्ड नवीन अर्ज",
        "📑 उत्पन्न व रहिवासी दाखला"
    ]


if __name__ == "__main__":
    import uvicorn
    print("\n" + "=" * 65)
    print("🏛️  SARKAR MITRA (सरकार मित्र) — Aaple Sarkar AI Bot")
    print("🌐 Running locally on: http://localhost:8000")
    print("=" * 65 + "\n")
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=False)
