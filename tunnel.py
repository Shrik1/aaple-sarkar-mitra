"""
Tunnel & Remote Access Launcher for Sarkar Mitra (Aaple Sarkar AI Bot)
Connects http://localhost:8000 to a secure HTTPS Cloudflare Tunnel using HTTP/2,
generates a scanable QR code, copies the link to clipboard, and enables access on any device.
"""

import os
import sys
import re
import socket
import subprocess
import time
import shutil
import pathlib
import webbrowser

CLOUDFLARED_CANDIDATES = [
    r"C:\Program Files (x86)\cloudflared\cloudflared.exe",
    r"C:\Program Files\cloudflared\cloudflared.exe",
    shutil.which("cloudflared") or "",
]

def find_cloudflared() -> str:
    for path in CLOUDFLARED_CANDIDATES:
        if path and os.path.exists(path):
            return path
    return ""

def get_local_ip() -> str:
    """Detects the PC's primary LAN/Wi-Fi IPv4 address."""
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
            s.connect(("8.8.8.8", 80))
            return s.getsockname()[0]
    except Exception:
        return "127.0.0.1"

def is_port_open(port: int = 8000, host: str = "127.0.0.1") -> bool:
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(0.6)
            return s.connect_ex((host, port)) == 0
    except Exception:
        return False

def ensure_server_running():
    """If the local server isn't running on port 8000, launch start.py in background."""
    if is_port_open(8000):
        print("  [OK] Local Sarkar Mitra server is active on port 8000.")
        return

    print("  [!] Server not detected on port 8000. Launching start.py...")
    project_dir = pathlib.Path(__file__).parent.resolve()
    start_script = project_dir / "start.py"
    
    subprocess.Popen(
        [sys.executable, str(start_script)],
        cwd=str(project_dir),
        creationflags=subprocess.CREATE_NEW_CONSOLE if sys.platform == "win32" else 0
    )
    
    # Wait up to 10 seconds for server to start
    for _ in range(20):
        time.sleep(0.5)
        if is_port_open(8000):
            print("  [OK] Server launched successfully on port 8000.")
            return
            
    print("  [WARN] Server is starting up, continuing with tunnel...")

def kill_lingering_tunnels():
    """Kill any previous cloudflared processes."""
    try:
        subprocess.run(
            ["powershell", "-NoProfile", "-Command", "Get-Process cloudflared -ErrorAction SilentlyContinue | Stop-Process -Force -ErrorAction SilentlyContinue"],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )
        time.sleep(0.5)
    except Exception:
        pass

def copy_to_clipboard(text: str):
    """Copies text to Windows clipboard."""
    try:
        subprocess.run(
            ["clip"],
            input=text.encode("utf-8"),
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            check=False
        )
    except Exception:
        pass

def create_desktop_helpers(public_url: str, local_ip: str):
    """Creates a desktop shortcut and visual HTML page with QR code."""
    desktop_dir = pathlib.Path.home() / "Desktop"
    if not desktop_dir.exists():
        return

    # 1. Windows Internet Shortcut (.url)
    url_file = desktop_dir / "Sarkar-Mitra-Live-Link.url"
    try:
        url_file.write_text(f"[InternetShortcut]\nURL={public_url}\nIconIndex=0\n", encoding="utf-8")
    except Exception:
        pass

    # 2. Visual HTML page with QR code and mobile instructions
    qr_img_api = f"https://api.qrserver.com/v1/create-qr-code/?size=260x260&data={public_url}"
    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Sarkar Mitra — Live Access & QR Code</title>
  <style>
    body {{
      font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
      background: #0E0F12;
      color: #E6EAF0;
      margin: 0;
      padding: 30px 16px;
      display: flex;
      flex-direction: column;
      align-items: center;
      min-height: 100vh;
      box-sizing: border-box;
    }}
    .card {{
      background: #16181C;
      border: 1px solid rgba(255,255,255,0.08);
      border-radius: 16px;
      padding: 32px 28px;
      max-width: 480px;
      width: 100%;
      text-align: center;
      box-shadow: 0 12px 40px rgba(0,0,0,0.6);
    }}
    h1 {{
      margin: 0 0 8px;
      font-size: 1.5rem;
      color: #FFFFFF;
    }}
    .badge {{
      display: inline-block;
      background: #10A37F;
      color: white;
      padding: 3px 12px;
      border-radius: 6px;
      font-weight: 600;
    }}
    p.subtitle {{
      color: #8E929E;
      font-size: 0.88rem;
      margin: 8px 0 24px;
    }}
    .qr-box {{
      background: #FFFFFF;
      padding: 16px;
      border-radius: 12px;
      display: inline-block;
      margin-bottom: 20px;
    }}
    .qr-box img {{
      display: block;
      width: 220px;
      height: 220px;
    }}
    .link-box {{
      background: rgba(255,255,255,0.04);
      border: 1px solid rgba(255,255,255,0.12);
      border-radius: 8px;
      padding: 12px 14px;
      margin-bottom: 16px;
      word-break: break-all;
    }}
    .link-box a {{
      color: #34D399;
      font-weight: 600;
      font-size: 0.95rem;
      text-decoration: none;
    }}
    .link-box a:hover {{
      text-decoration: underline;
    }}
    .methods {{
      text-align: left;
      font-size: 0.82rem;
      color: #B2B7C2;
      background: rgba(255,255,255,0.02);
      border-radius: 8px;
      padding: 14px 16px;
      line-height: 1.6;
    }}
    .methods strong {{
      color: #FFFFFF;
    }}
  </style>
</head>
<body>
  <div class="card">
    <h1>Welcome to <span class="badge">Sarkar Mitra</span></h1>
    <p class="subtitle">Scan the QR code on your mobile phone to open the bot instantly!</p>
    
    <div class="qr-box">
      <img src="{qr_img_api}" alt="QR Code for Sarkar Mitra">
    </div>

    <div class="link-box">
      <a href="{public_url}" target="_blank">{public_url}</a>
    </div>

    <div class="methods">
      <strong>📱 How to open on other devices:</strong><br>
      • <strong>Mobile / Tablet:</strong> Open Camera & point at this QR code.<br>
      • <strong>Any Network:</strong> Works on home Wi-Fi and mobile data (4G/5G).<br>
      • <strong>Home Wi-Fi Direct:</strong> <a href="http://{local_ip}:8000" style="color:#34D399;">http://{local_ip}:8000</a>
    </div>
  </div>
</body>
</html>
"""
    qr_html_file = desktop_dir / "Sarkar-Mitra-QR.html"
    try:
        qr_html_file.write_text(html_content, encoding="utf-8")
    except Exception:
        pass

def print_terminal_qr(url: str):
    """Prints ASCII QR code in terminal using qrcode library if available."""
    try:
        import qrcode
        qr = qrcode.QRCode(border=1)
        qr.add_data(url)
        print("\n  📱 SCAN WITH YOUR PHONE CAMERA TO OPEN INSTANTLY:\n")
        qr.print_ascii(invert=True)
    except Exception:
        pass

def main():
    print("=" * 68)
    print("🏛️   SARKAR MITRA (सरकार मित्र) — Secure Tunnel & Remote Access")
    print("=" * 68)
    
    cloudflared = find_cloudflared()
    if not cloudflared:
        print("\n❌ cloudflared executable was not found.")
        print("   Please install it using: winget install Cloudflare.cloudflared")
        sys.exit(1)

    print(f"  [i] Using tunnel client: {cloudflared}")
    local_ip = get_local_ip()
    print(f"  [i] Home Wi-Fi IPv4 Address: {local_ip}")

    # Check / launch server
    ensure_server_running()

    # Clear previous processes
    kill_lingering_tunnels()

    print("\n🚀 Establishing secure HTTP/2 tunnel to http://127.0.0.1:8000 ...")

    # Use HTTP/2 protocol to bypass ISP UDP/QUIC blocks on port 7844
    cmd = [
        cloudflared,
        "tunnel",
        "--protocol", "http2",
        "--url", "http://127.0.0.1:8000"
    ]

    try:
        proc = subprocess.Popen(
            cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            encoding="utf-8",
            errors="replace"
        )
    except Exception as e:
        print(f"❌ Failed to start cloudflared: {e}")
        return

    url_pattern = re.compile(r"https://[a-zA-Z0-9-]+\.trycloudflare\.com")
    tunnel_url = None

    try:
        for line in proc.stdout:
            match = url_pattern.search(line)
            if match and not tunnel_url:
                tunnel_url = match.group(0)

                # Copy link to clipboard
                copy_to_clipboard(tunnel_url)

                # Create desktop files
                create_desktop_helpers(tunnel_url, local_ip)

                print("\n" + "🎉 " + "=" * 64)
                print("✨ SARKAR MITRA IS NOW ACCESSIBLE ON ALL DEVICES!")
                print("=" * 68)
                print(f"\n🌐 PUBLIC SECURE LINK (Copied to Clipboard!):")
                print(f"   👉  {tunnel_url}")
                print(f"\n🏠 HOME WI-FI DIRECT LINK:")
                print(f"   👉  http://{local_ip}:8000")
                print("\n" + "-" * 68)

                # Print terminal QR code
                print_terminal_qr(tunnel_url)

                print("-" * 68)
                print("📁 Shortcut saved to your Desktop:")
                print("   • Sarkar-Mitra-QR.html (Open on PC to show large QR code)")
                print("   • Sarkar-Mitra-Live-Link.url (One-click browser shortcut)")
                print("\n🛑 Keep this window open while using the bot on other devices.")
                print("   Press Ctrl+C in this terminal when you want to stop sharing.\n")
                print("=" * 68)

                # Open the QR HTML page in browser automatically
                desktop_html = pathlib.Path.home() / "Desktop" / "Sarkar-Mitra-QR.html"
                if desktop_html.exists():
                    try:
                        webbrowser.open(desktop_html.as_uri())
                    except Exception:
                        pass

            if "ERR" in line and not tunnel_url:
                print(f"  ⚠️  {line.strip()}")

        proc.wait()
    except KeyboardInterrupt:
        print("\n\n🛑 Stopping tunnel...")
        proc.terminate()
        kill_lingering_tunnels()
        print("👋 Tunnel stopped. Bot is now accessible on localhost only.")

if __name__ == "__main__":
    main()
