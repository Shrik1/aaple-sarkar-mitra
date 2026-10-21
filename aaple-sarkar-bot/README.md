# 🏛️ सरकार मित्र | Sarkar Mitra - Aaple Sarkar AI Bot

A voice-first, Marathi-capable AI assistant for Maharashtra government services.
Built for the **SEVA Innovation Challenge 2026**.

## Features

- 🗣️ **Multi-language**: Marathi, Hindi, English support
- 🎤 **Voice Input**: Record voice messages (transcribed by Gemini AI)
- 🤖 **RAG-powered**: Answers grounded in verified government scheme data
- 📋 **9 schemes covered**: PM Kisan, Ladki Bahin, Ration Card, 7/12 Satbara, and more
- 💬 **Multi-turn chat**: Remembers conversation context
- 📱 **Responsive UI**: Works on mobile and desktop
- 🔗 **Direct apply links**: One-click to official government portals

## Quick Start

### 1. Get a Gemini API Key (Free)
Visit: https://aistudio.google.com/apikey

### 2. Set Your API Key
Edit `.env` file:
```
GEMINI_API_KEY=AQ.Ab8RN6Kw1AUTsH5sq_QS2aEB3M0-OWw0_ToXc8R9Ev174S1Xqg
```

### 3. Start the Bot
```bash
python start.py
```
Then open: **http://localhost:8000**

## Project Structure
```
aaple-sarkar-bot/
├── main.py           # FastAPI backend + Gemini AI integration
├── knowledge_base.py # Government schemes data (RAG source)
├── start.py          # Setup & startup script
├── static/
│   └── index.html    # Beautiful responsive frontend
├── .env              # API key (edit this!)
└── requirements.txt  # Python dependencies
```

## Covered Schemes
| Scheme | Category | Benefit |
|--------|----------|---------|
| PM Kisan | Agriculture | ₹6,000/year |
| Mahatma Phule Karj Mafi | Agriculture | Up to ₹2L waiver |
| Ladki Bahin Yojana | Women Welfare | ₹1,500/month |
| Mahaswayam Employment | Employment | Job portal access |
| Ration Card / PDS | Food Security | Subsidized food |
| 7/12 Satbara | Land Records | Official land document |
| Birth Certificate | Certificates | Official birth record |
| Income Certificate | Certificates | Income proof |
| Aaple Sarkar Portal | General | 400+ services |

## Architecture
```
User (Web Browser)
      ↓ HTTP
FastAPI Backend (main.py)
      ↓ RAG Search
Knowledge Base (knowledge_base.py)
      ↓ Gemini API
gemini-3.8-flash model
      ↓ Response
User gets accurate answer in their language
```

## Helpline
📞 **1800-120-8040** (Toll-Free, 24/7)
