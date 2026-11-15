@echo off
chcp 65001 >nul
title Sarkar Mitra - Mobile Tunnel & QR Sharing
color 0A
cd /d "C:\Users\Lenovo\.gemini\antigravity\scratch\aaple-sarkar-bot"
cls
echo =================================================================
echo   SARKAR MITRA - Mobile & Multi-Device Tunnel Launcher
echo =================================================================
echo.
echo Starting secure tunnel connection to http://localhost:8000...
echo.
python tunnel.py
if %ERRORLEVEL% NEQ 0 (
    echo.
    echo [ERROR] Tunnel launcher encountered an error.
    pause
)
