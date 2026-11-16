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
from general_knowledge import generate_general_answer, match_general_knowledge
from conversational_reasoner import reason_on_user_question, detect_scheme_from_context

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

SYSTEM_INSTRUCTION = """You are "Sarkar Mitra" (सरकार मित्र), a powerful, friendly, and intelligent AI assistant.

You have TWO modes of operation:

═══════════════════════════════════════════════════════════════
MODE 1 — GOVERNMENT SCHEMES & CITIZEN SERVICES (Primary Specialization)
═══════════════════════════════════════════════════════════════
When the user asks about Maharashtra state schemes, central government welfare programs, 
Aaple Sarkar services, certificates, ration cards, subsidies, land records, pensions, 
or any citizen service — you MUST respond with the highest accuracy:

- Use the VERIFIED SCHEMES KNOWLEDGE BASE context provided below (when available).
- Structure: Detailed breakdown with exact amounts, eligibility criteria, required documents, official links, and helpline numbers.
- Never fabricate scheme amounts, dates, or criteria.
- Emphasize that citizens do NOT need middlemen — they can apply via Aaple Sarkar or Maha e-Seva Kendras.
- Bilingual Format (for scheme-related questions):
    • Primary answer in the user's language (Marathi/Hindi/English).
    • Followed by a divider (---) and a complete translation section:
      🌐 **English Translation & Summary:** (if primary was Marathi/Hindi)
      OR
      🌐 **मराठी सारांश (Marathi Summary):** (if primary was English)

═══════════════════════════════════════════════════════════════
MODE 2 — GENERAL KNOWLEDGE & OPEN CONVERSATION (Like ChatGPT)
═══════════════════════════════════════════════════════════════
When the user asks a general question — about science, technology, math, history, 
coding, health, education, career advice, daily life tips, creative writing, 
explanations, analysis, or ANY topic unrelated to government schemes — you MUST 
answer it helpfully and accurately, just like a world-class AI assistant.

- Answer the question fully, clearly, and directly.
- Use well-structured formatting with headers, bullet points, code blocks, etc.
- Be conversational, warm, and intelligent.
- You can discuss any safe, ethical topic.
- For general questions, bilingual translation is OPTIONAL (only include it if the user seems to prefer bilingual output, or if they asked in Marathi/Hindi and an English summary would be genuinely helpful).

═══════════════════════════════════════════════════════════════
GENERAL GUIDELINES (Both Modes)
═══════════════════════════════════════════════════════════════
1. Language: Match the user's language. If they write in Marathi, reply in Marathi. If in English, reply in English. If mixed, use the dominant language.
2. Emojis: Use tasteful icons sparingly (🏛️, ✅, 📋, 💰, 📞, 🌾, 💡, 🔬, 📖).
3. Tone: Friendly, respectful, knowledgeable. Address the user warmly.
4. Length: Be thorough for complex questions, concise for simple ones.
5. If a general question has a natural connection to a Maharashtra scheme (e.g., "How do farmers get loans?" → mention Mahatma Phule Karj Mukti), weave in the relevant scheme information naturally.
6. Never refuse a reasonable question. You are a helpful general-purpose AI that also happens to be an expert on Maharashtra government schemes."""


# ─── Pydantic Models ──────────────────────────────────────────────────────────
class ChatMessage(BaseModel):
    message: str
    history: Optional[list] = []
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

    # 1. RAG Search & Context Detection
    relevant_schemes = search_knowledge_base(query)
    is_scheme_query = len(relevant_schemes) > 0
    inferred_scheme = detect_scheme_from_context(query, request.history or [], SCHEMES_DATA)
    if not relevant_schemes and inferred_scheme:
        relevant_schemes = [inferred_scheme]
        is_scheme_query = True

    # 2. Try Gemini Generative AI (for BOTH scheme and general questions)
    client = get_client()
    if client:
        try:
            rag_context = ""
            if relevant_schemes:
                rag_context = "\n\n=== VERIFIED STATE SCHEMES KNOWLEDGE BASE ===\n"
                rag_context += "(Use this verified data for accurate scheme rules, amounts, eligibility, and documents.)\n"
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
            else:
                rag_context = "\n\n(No specific government scheme matched this query. This appears to be an open custom question. Answer it freely and helpfully like ChatGPT or Claude.)\n"

            # Multi-turn history context for conversational continuity
            history_str = ""
            if request.history:
                history_str = "\n=== RECENT CONVERSATION CONTEXT ===\n"
                for h in request.history[-6:]:
                    speaker = "Citizen" if h.get("role") == "user" else "Sarkar Mitra"
                    history_str += f"{speaker}: {h.get('content', '')}\n"

            prompt = (
                f"{SYSTEM_INSTRUCTION}\n"
                f"{rag_context}\n"
                f"{history_str}\n\n"
                f"Current Citizen Question: {query}\n"
                f"Preferred Language: {request.language}\n"
                f"CRITICAL INSTRUCTION: Think by yourself and directly answer the citizen's specific personal or follow-up question. "
                f"If the citizen asks a situational question (e.g., age, minor status, income limit, or missing documents), "
                f"provide clear reasoning directly answering their question first, rather than dumping a generic scheme brochure."
            )

            reply_text = None
            interaction_id = None

            # Strategy A: standard client.models.generate_content
            for model_name in ["gemini-2.5-flash", "gemini-2.0-flash"]:
                try:
                    resp = client.models.generate_content(
                        model=model_name,
                        contents=prompt
                    )
                    if resp and resp.text:
                        reply_text = resp.text
                        break
                except Exception as m_err:
                    logger.warning(f"models.generate_content with {model_name} failed: {m_err}")

            # Strategy B: fallback to client.interactions.create
            if not reply_text:
                try:
                    call_params = {
                        "model": "gemini-flash-latest",
                        "input": prompt
                    }
                    if request.previous_interaction_id:
                        call_params["previous_interaction_id"] = request.previous_interaction_id
                    interaction = client.interactions.create(**call_params)
                    if interaction and interaction.output_text:
                        reply_text = interaction.output_text
                        interaction_id = interaction.id
                except Exception as i_err:
                    logger.warning(f"interactions.create failed: {i_err}")

            if reply_text:
                return ChatResponse(
                    reply=reply_text,
                    schemes_found=_clean_schemes(relevant_schemes),
                    interaction_id=interaction_id,
                    suggestions=_generate_suggestions(query, relevant_schemes),
                    mode="gemini"
                )
        except Exception as e:
            logger.error(f"Fallback triggered due to Gemini error: {e}")

    # 3. Dual-Engine Intelligent Reasoning Fallback (Offline / Zero-Key Mode)
    
    # 3A. First, check if the query is a context-aware or specific situational question
    reasoned_reply, matched_scheme = reason_on_user_question(
        query,
        request.history or [],
        SCHEMES_DATA,
        request.language or "auto"
    )
    if reasoned_reply:
        schemes_to_return = [matched_scheme] if matched_scheme else relevant_schemes
        return ChatResponse(
            reply=reasoned_reply,
            schemes_found=_clean_schemes(schemes_to_return),
            interaction_id=None,
            suggestions=_generate_suggestions(query, schemes_to_return),
            mode="reasoning_engine"
        )

    # 3B. Standard scheme inquiry fallback (initial brochure view)
    if is_scheme_query:
        fallback_text, matched = generate_smart_fallback(query, request.language or "auto")
        return ChatResponse(
            reply=fallback_text,
            schemes_found=_clean_schemes(relevant_schemes or matched),
            interaction_id=None,
            suggestions=_generate_suggestions(query, relevant_schemes or matched),
            mode="knowledge_base"
        )
    else:
        # 3C. General / custom academic / coding question fallback
        fallback_text, was_matched = generate_general_answer(query, request.language or "auto")
        return ChatResponse(
            reply=fallback_text,
            schemes_found=[],
            interaction_id=None,
            suggestions=_generate_suggestions(query, []),
            mode="general_ai"
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
    elif "quantum" in q:
        return [
            "What is quantum entanglement?",
            "What is the difference between a bit and a qubit?",
            "How does quantum superposition work?",
            "Real-world uses of quantum computers"
        ]
    elif "python" in q or "code" in q or "programming" in q:
        return [
            "Python list comprehension examples",
            "How to reverse a string in Python?",
            "Explain Object-Oriented Programming (OOP)",
            "How to connect Python with SQL?"
        ]
    elif "machine learning" in q or " ai " in q or "deep learning" in q or "data science" in q:
        return [
            "Difference between Supervised and Unsupervised Learning",
            "What is Deep Learning vs Machine Learning?",
            "How do neural networks work?",
            "Best Python libraries for AI"
        ]
    elif "shivaji" in q or "महाराज" in q:
        return [
            "Chhatrapati Shivaji Maharaj forts history",
            "Who was Jijamata?",
            "Explain Ganimi Kava guerrilla tactics",
            "Shivaji Maharaj coronation at Raigad"
        ]
    elif "newton" in q or "motion" in q or "physics" in q:
        return [
            "Explain Newton's third law with examples",
            "What is the formula F = m * a?",
            "What is inertia in physics?",
            "Difference between mass and weight"
        ]
    elif "resume" in q or "interview" in q or "job" in q:
        return [
            "Sample 1-page fresher resume layout",
            "How to answer 'Tell me about yourself'?",
            "STAR method for job interviews",
            "Write a sick leave application email"
        ]
    elif "photosynthesis" in q or "plant" in q or "biology" in q:
        return [
            "What is the chemical equation of photosynthesis?",
            "Light-dependent vs Calvin cycle reactions",
            "Why are plant leaves green?",
            "Role of chlorophyll in photosynthesis"
        ]
    return [
        "⚛️ Explain quantum computing",
        "🐍 Learn Python programming",
        "👩 लाडकी बहीण योजना पात्रता",
        "🌾 पीएम किसान योजना लाभ",
        "📄 How to write a standout resume?"
    ]


if __name__ == "__main__":
    import uvicorn
    print("\n" + "=" * 65)
    print("🏛️  SARKAR MITRA (सरकार मित्र) — Aaple Sarkar AI Bot")
    print("🌐 Running locally on: http://localhost:8000")
    print("=" * 65 + "\n")
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=False)
