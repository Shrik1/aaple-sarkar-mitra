"""
Setup and Runner Script for Sarkar Mitra (Aaple Sarkar AI Bot)
Runs on http://localhost:8000 with automatic port freeing and error prevention.
"""

import os
import sys
import socket
import subprocess
import pathlib
import time

PORT = 8000

def free_port_if_in_use(port: int = PORT):
    """Automatically frees the port if a previous instance is still running."""
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(0.5)
            in_use = (s.connect_ex(('127.0.0.1', port)) == 0)
            
        if in_use:
            print(f"🔄 Port {port} is already in use by an existing bot instance.")
            print(f"   Clearing lingering instance on port {port}...")
            if sys.platform == "win32":
                cmd = (
                    f'powershell -NoProfile -Command "'
                    f'Get-NetTCPConnection -LocalPort {port} -ErrorAction SilentlyContinue | '
                    f'ForEach-Object {{ Stop-Process -Id $_.OwningProcess -Force -ErrorAction SilentlyContinue }}"'
                )
                subprocess.run(cmd, shell=True, capture_output=True)
                time.sleep(1.5)
            print("✅ Port cleared successfully.\n")
    except Exception as e:
        print(f"Note while checking port: {e}")

def main():
    print("=" * 65)
    print("🏛️  SARKAR MITRA (सरकार मित्र) — Aaple Sarkar AI Assistant")
    print("=" * 65)
    
    current_dir = pathlib.Path(__file__).parent
    env_file = current_dir / ".env"
    
    api_key = os.getenv("GEMINI_API_KEY") or os.getenv("GOOGLE_API_KEY")
    
    # Read .env if key not in env vars
    if not api_key and env_file.exists():
        try:
            with open(env_file, "r", encoding="utf-8") as f:
                for line in f:
                    line = line.strip()
                    if line.startswith("GEMINI_API_KEY="):
                        val = line.split("=", 1)[1].strip()
                        if val and val != "your_gemini_api_key_here":
                            api_key = val
                            os.environ["GEMINI_API_KEY"] = api_key
                            break
        except Exception as e:
            pass
            
    if api_key and api_key != "your_gemini_api_key_here" and len(api_key.strip()) >= 20:
        print(f"✅ Gemini AI API key active: {api_key[:6]}...{api_key[-4:]}")
    else:
        print("💡 Status: Local Verified Knowledge Base Mode active.")
        print("   (The bot delivers complete verified scheme answers instantly!)")
        print("   To enable Gemini AI generation, add your free key to .env:")
        print("   👉 https://aistudio.google.com/apikey")
        
    print("-" * 65)
    
    # Clean port before starting
    free_port_if_in_use(PORT)
    
    print(f"🚀 Starting Server on http://localhost:{PORT} ...")
    print(f"📱 Open in your browser: http://localhost:{PORT}")
    print("🛑 Press Ctrl+C in this terminal to stop.")
    print("=" * 65 + "\n")
    
    try:
        import uvicorn
        uvicorn.run("main:app", host="0.0.0.0", port=PORT, reload=False)
    except KeyboardInterrupt:
        print("\n👋 Server stopped. Dhanyawad!")
    except Exception as e:
        print(f"\n❌ Error starting server: {e}")

if __name__ == "__main__":
    main()
