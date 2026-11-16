# 🏛️ सरकार मित्र (Sarkar Mitra) — Aaple Sarkar AI Bot

An AI-powered, bilingual citizen welfare assistant built for **Aaple Sarkar (Government of Maharashtra)**. Designed for rural farmers, women, students, and citizens across Maharashtra to effortlessly discover state welfare schemes, verify eligibility criteria, check required documents, and access official application portals without middlemen or digital barriers.

---

## ✨ Key Capabilities

- **Dual-Mode AI Architecture (ChatGPT / Claude + Civic Tech)**:
  - 🤖 **General AI Mode**: Answers custom questions on any topic — Science, Computer Science, Python/Web coding, Mathematics, History, Job Interview preparation, Resume writing, and Essay drafting.
  - 🏛️ **Maharashtra Scheme Specialist**: Grounded in official Maharashtra Government Resolutions (GRs) for 10+ major welfare programs with zero hallucinations.
- **ChatGPT-Inspired Dark Minimalist UI**:
  - Sleek, modern charcoal design (`#0E0F12`, `#16181C`) with emerald green accents (`#10A37F`) and responsive mobile drawer.
  - Dual sidebar sections: **✦ Ask Anything (ChatGPT Mode)** and **🏛️ Maharashtra Welfare Schemes**.
- **Bilingual Response Engine (Marathi + English)**:
  - Every scheme response delivers full, authentic **Marathi (मराठी)** details first, followed by a structured **English Translation & Summary** (Overview, Key Benefits, Eligibility Checklist, Required Documents, and Official Links).
- **Speech & Voice Interface**:
  - 🎤 **Voice Input (Speech-to-Text)**: Speak your question directly in Marathi or English.
  - 🔊 **Voice Readout (Text-to-Speech)**: Click the speaker button on any reply to listen to it read aloud.
- **Dual-Engine Architecture (Zero-Failure Guarantee)**:
  - **Gemini 3.8 Flash**: Rich generative conversation via official `google-genai` SDK.
  - **Verified State RAG Knowledge Base**: Instant factual grounding in official Maharashtra Government Resolutions (GRs). Even without an API key or when offline, the bot delivers 100% verified answers without crashing.
- **Comprehensive Schemes Catalog**:
  - 🌾 **Agriculture**: PM Kisan Samman Nidhi & Namo Shetkari (₹12,000/yr), Mahatma Phule Karj Mukti (₹2 Lakh crop loan waiver), MahaDBT Farm Machinery Subsidies.
  - 👩 **Women Welfare**: Mukhyamantri Majhi Ladki Bahin Yojana (₹1,500/month DBT).
  - 📄 **Revenue & Land Records**: Digital 7/12 (सातबारा) and 8-A land extracts with legal QR code validity.
  - 🍚 **Food Security**: Ration Cards (AAY, BPL, PHH) & Subsidized/Free Foodgrains.
  - 📜 **Citizen Certificates**: Tehsildar Income Certificate (1 & 3 year), Caste Certificate, and Domicile Certificate.
  - 🤝 **Social Security**: Sanjay Gandhi Niradhar Anudan Pension (₹1,500/month).
- **Cloudflare Tunnel & Mobile Sharing**:
  - Built-in `tunnel.py` with HTTP/2 protocol to share the bot to any smartphone, tablet, or external computer with an instant terminal ASCII QR code.

---

## 🚀 Quick Start (Local Setup)

### 1. Clone the Repository
```bash
git clone https://github.com/Shrik1/aaple-sarkar-mitra.git
cd aaple-sarkar-mitra
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the Server
```bash
python start.py
```
Or double-click `start-bot.bat` on Windows.

### 4. Open in Browser
Visit: **[http://localhost:8000](http://localhost:8000)**

---

## 📱 Mobile & Multi-Device Access (Tunnel)

To share the app with other devices at home or on mobile data:
```bash
python tunnel.py
```
Or double-click `share-tunnel.bat` on Windows. It generates a secure HTTPS link and an instant QR code you can scan with your phone camera!

---

## 🔑 Adding a Gemini API Key (Optional)

The bot operates **100% reliably out of the box** using its local verified knowledge base. To activate full Gemini generative capabilities:
1. Get a free API key at **[https://aistudio.google.com/apikey](https://aistudio.google.com/apikey)**.
2. Either:
   - Click the ⚙️ icon in the web UI and paste your key, **OR**
   - Create a `.env` file based on `.env.example`:
     ```env
     GEMINI_API_KEY=AIzaSy...your_key_here
     ```

---

## 📂 Project Structure

```
aaple-sarkar-mitra/
├── main.py              # FastAPI application (Chat, Search, Speech, Schemes APIs)
├── knowledge_base.py    # Verified Maharashtra schemes dataset & bilingual RAG
├── general_knowledge.py # Custom questions & general academic/coding knowledge engine
├── start.py             # Automatic port-freeing runner
├── tunnel.py            # Cloudflare HTTP/2 tunnel & QR code generator
├── serve.py             # Lightweight HTTP server fallback
├── requirements.txt     # Python dependencies
├── .env.example         # Template for environment variables
├── .gitignore           # Git ignore rules for secrets and caches
├── start-bot.bat        # Windows one-click start script
├── stop-bot.bat         # Windows one-click stop script
├── control-panel.bat    # Windows interactive management dashboard
├── share-tunnel.bat     # Windows one-click tunnel launcher
├── static/
│   └── index.html       # ChatGPT-style dark minimalist UI with Voice I/O & Bilingual chat
└── README.md            # Documentation
```

---

## 📞 Official Maharashtra Citizen Helplines
- **Aaple Sarkar Toll-Free**: `1800-120-8040` (24x7)
- **Women Helpline**: `181`
- **Kisan Call Center**: `1800-180-1551`
- **Official Portal**: [https://aaplesarkar.mahaonline.gov.in](https://aaplesarkar.mahaonline.gov.in)
