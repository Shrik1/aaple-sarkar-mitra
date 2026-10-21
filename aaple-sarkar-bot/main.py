"""
Aaple Sarkar AI Assistant - FastAPI Backend
Voice-first Marathi government scheme assistant.
"""

import os
import json
import base64
import logging
from typing import Optional
from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse, FileResponse
import pathlib
from pydantic import BaseModel
from dotenv import load_dotenv
from google import genai
from knowledge_base import search_knowledge_base, SCHEMES_DATA

load_dotenv()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(title="Aaple Sarkar AI Bot", version="1.0.0")

# Serve static files
STATIC_DIR = pathlib.Path(__file__).parent / "static"
app.mount("/static", StaticFiles(directory=str(STATIC_DIR)), name="static")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Gemini client (lazy initialization)
_client = None

def get_client():
    global _client
    if _client is None:
        api_key = os.getenv("GEMINI_API_KEY") or os.getenv("GOOGLE_API_KEY", "")
        if not api_key:
            raise ValueError("GEMINI_API_KEY not set. Please add it to your .env file.")
        _client = genai.Client(api_key=api_key)
    return _client

# System instruction for the bot
SYSTEM_INSTRUCTION = """You are "Sarkar Mitra" (सरकार मित्र), a helpful AI assistant for the Aaple Sarkar portal (Maharashtra government services).

Your role is to help rural citizens of Maharashtra understand:
1. Government schemes and their eligibility criteria
2. Required documents for applications
3. How to apply for various services
4. Information about PM Kisan, Ladki Bahin Yojana, ration cards, land records (7/12 Satbara), and more

Language Rules:
- If the user writes in Marathi (Devanagari script), respond primarily in Marathi with key terms in English.
- If the user writes in English, respond in English with Marathi terms for important concepts.
- If the user writes in Hinglish (Hindi-English mix), respond in a simple, friendly mix.
- Always be simple, clear, and easy to understand for rural citizens.

Response Guidelines:
- Always be warm, helpful, and respectful
- Use bullet points for eligibility and documents
- Always include helpline numbers when relevant
- If a scheme matches, provide complete information
- If you're unsure, direct them to the Aaple Sarkar portal or helpline 1800-120-8040
- Keep responses concise but complete
- Use emojis sparingly but effectively (✅, 📋, 📞, 💰, 📌)

Context from knowledge base will be provided. Use it as the primary source of truth.
NEVER make up information about schemes. If you don't know, say so clearly."""


class ChatMessage(BaseModel):
    message: str
    language: Optional[str] = "auto"
    previous_interaction_id: Optional[str] = None


class ChatResponse(BaseModel):
    reply: str
    schemes_found: list
    interaction_id: str
    suggestions: list


class AudioMessage(BaseModel):
    audio_base64: str
    mime_type: str = "audio/webm"


@app.get("/", response_class=HTMLResponse)
async def root():
    return FileResponse("static/index.html")


@app.get("/health")
async def health():
    return {"status": "ok", "service": "Aaple Sarkar AI Bot"}


@app.post("/api/chat", response_model=ChatResponse)
async def chat(request: ChatMessage):
    """Main chat endpoint - handles text messages."""
    try:
        # Search knowledge base for relevant schemes
        relevant_schemes = search_knowledge_base(request.message)
        
        # Build context from knowledge base
        context = ""
        if relevant_schemes:
            context = "\n\n=== KNOWLEDGE BASE CONTEXT ===\n"
            for scheme in relevant_schemes:
                context += f"\nScheme: {scheme['title']} ({scheme['title_mr']})\n"
                context += f"Category: {scheme['category']}\n"
                context += f"Description: {scheme['description']}\n"
                context += f"Description (Marathi): {scheme['description_mr']}\n"
                context += f"Eligibility: {', '.join(scheme['eligibility'])}\n"
                context += f"Benefits: {scheme['benefits']}\n"
                context += f"Documents: {', '.join(scheme['documents'])}\n"
                context += f"Apply Link: {scheme['apply_link']}\n"
                context += f"Helpline: {scheme['helpline']}\n"
                context += "---\n"
        
        # Construct the prompt
        full_prompt = f"{SYSTEM_INSTRUCTION}\n{context}\n\nUser Query: {request.message}"
        
        # Build interaction params
        params = {
            "model": "gemini-3.8-flash",
            "input": full_prompt,
        }
        
        # Add conversation continuity if previous interaction exists
        if request.previous_interaction_id:
            params["previous_interaction_id"] = request.previous_interaction_id
        
        # Call Gemini API
        interaction = get_client().interactions.create(**params)
        
        reply_text = interaction.output_text or "माफ करा, मला उत्तर देता आले नाही. कृपया पुन्हा प्रयत्न करा."
        
        # Generate contextual suggestions
        suggestions = _generate_suggestions(request.message, relevant_schemes)
        
        return ChatResponse(
            reply=reply_text,
            schemes_found=[{
                "id": s["id"],
                "title": s["title"],
                "title_mr": s["title_mr"],
                "category": s["category"],
                "apply_link": s["apply_link"],
                "helpline": s["helpline"]
            } for s in relevant_schemes],
            interaction_id=interaction.id,
            suggestions=suggestions
        )
        
    except Exception as e:
        logger.error(f"Chat error: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/api/transcribe")
async def transcribe_audio(request: AudioMessage):
    """Transcribe audio to text using Gemini."""
    try:
        # Decode base64 audio
        audio_data = base64.b64decode(request.audio_base64)
        
        # Use Gemini multimodal to transcribe
        interaction = get_client().interactions.create(
            model="gemini-3.8-flash",
            input=[
                {
                    "type": "text",
                    "text": "Please transcribe this audio message. The speaker may be speaking in Marathi, Hindi, or English. Return ONLY the transcription text, nothing else."
                },
                {
                    "type": "audio",
                    "data": base64.b64encode(audio_data).decode(),
                    "mime_type": request.mime_type
                }
            ]
        )
        
        transcribed_text = interaction.output_text or ""
        return {"text": transcribed_text.strip(), "success": True}
        
    except Exception as e:
        logger.error(f"Transcription error: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/api/schemes")
async def get_all_schemes():
    """Get list of all available schemes."""
    return {
        "schemes": [{
            "id": s["id"],
            "title": s["title"],
            "title_mr": s["title_mr"],
            "category": s["category"],
            "benefits": s["benefits"],
            "benefits_mr": s["benefits_mr"],
            "apply_link": s["apply_link"],
            "helpline": s["helpline"]
        } for s in SCHEMES_DATA]
    }


@app.get("/api/scheme/{scheme_id}")
async def get_scheme(scheme_id: str):
    """Get full details of a specific scheme."""
    scheme = next((s for s in SCHEMES_DATA if s["id"] == scheme_id), None)
    if not scheme:
        raise HTTPException(status_code=404, detail="Scheme not found")
    return scheme


def _generate_suggestions(query: str, schemes: list) -> list:
    """Generate contextual follow-up suggestions."""
    base_suggestions = [
        "पात्रता तपासा (Check Eligibility)",
        "आवश्यक कागदपत्रे (Required Documents)",
        "अर्ज कसा करावा? (How to Apply?)",
        "हेल्पलाइन नंबर (Helpline Number)"
    ]
    
    if "pm kisan" in query.lower() or "किसान" in query:
        return [
            "PM Kisan साठी पात्रता काय आहे?",
            "पैसे कधी मिळतील?",
            "pm kisan status check कसे करावे?",
            "7/12 उतारा कसा मिळवावा?"
        ]
    elif "ladki bahin" in query.lower() or "लाडकी बहीण" in query:
        return [
            "लाडकी बहीण साठी अर्ज कसा करावा?",
            "पैसे कधी मिळतात?",
            "अर्जाची स्थिती कशी तपासावी?",
            "आवश्यक कागदपत्रे कोणती?"
        ]
    elif "ration" in query.lower() or "रेशन" in query:
        return [
            "रेशन कार्ड साठी कोण पात्र आहे?",
            "रेशन कार्ड कुठे मिळेल?",
            "BPL आणि APL मध्ये फरक काय?",
            "रेशन कार्ड बद्दल तक्रार कुठे करावी?"
        ]
    else:
        return [
            "शेतकरी योजना (Farmer Schemes)",
            "महिला योजना (Women Schemes)", 
            "जमीन नोंदी (Land Records)",
            "प्रमाणपत्रे (Certificates)"
        ]


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
