"""
Setup script for Aaple Sarkar AI Bot.
Checks configuration and starts the server.
"""
import os
import sys
import subprocess

def main():
    print("=" * 60)
    print("🏛️  SARKAR MITRA - Aaple Sarkar AI Bot Setup")
    print("=" * 60)
    
    # Check for API key
    api_key = os.getenv("GEMINI_API_KEY") or os.getenv("GOOGLE_API_KEY")
    
    # Check .env file
    env_file = os.path.join(os.path.dirname(__file__), ".env")
    if not api_key and os.path.exists(env_file):
        with open(env_file) as f:
            for line in f:
                if line.startswith("GEMINI_API_KEY="):
                    api_key = line.strip().split("=", 1)[1]
                    if api_key and api_key != "your_gemini_api_key_here":
                        os.environ["GEMINI_API_KEY"] = api_key
                        print(f"✅ API key loaded from .env file")
                    break
    
    if not api_key or api_key == "your_gemini_api_key_here":
        print("\n❌ GEMINI_API_KEY not found!")
        print("\nTo get your free API key:")
        print("  1. Go to: https://aistudio.google.com/apikey")
        print("  2. Create a new API key")
        print("  3. Set it using ONE of these methods:")
        print()
        print("  Option A - Edit the .env file:")
        print(f'     Open: {env_file.replace(".env.example", ".env")}')
        print('     Change: GEMINI_API_KEY=your_actual_key_here')
        print()
        print("  Option B - Set environment variable:")
        print('     PowerShell: $env:GEMINI_API_KEY="your_key_here"')
        print('     Then run:   python start.py')
        print()
        
        key_input = input("Or paste your Gemini API key here (press Enter to skip): ").strip()
        if key_input:
            os.environ["GEMINI_API_KEY"] = key_input
            # Save to .env
            with open(env_file.replace(".example", ""), "w") as f:
                f.write(f"GEMINI_API_KEY={key_input}\n")
            print("✅ API key saved to .env file!")
        else:
            print("\n⚠️  Continuing without API key. Chat will not work until you set GEMINI_API_KEY.")
    else:
        print(f"✅ Gemini API key found ({api_key[:8]}...)")
    
    print()
    print("🚀 Starting Sarkar Mitra Bot...")
    print("📱 Open your browser at: http://localhost:8000")
    print("🛑 Press Ctrl+C to stop the server")
    print("-" * 60)
    
    # Start server
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=False)

if __name__ == "__main__":
    main()
