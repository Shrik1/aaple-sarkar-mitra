@echo off
chcp 65001 >nul
title Sarkar Mitra - Server [ON]
cls
echo ============================================================
echo   SARKAR MITRA (Aaple Sarkar AI Bot) - STARTING SERVER
echo ============================================================
echo.
cd /d "C:\Users\Lenovo\.gemini\antigravity\scratch\aaple-sarkar-bot"

echo [*] Opening browser: http://localhost:8000
start "" http://localhost:8000

echo [*] Starting Python backend server...
echo [*] (To stop the server at any time, press Ctrl+C or run stop-bot.bat)
echo.
python start.py
pause