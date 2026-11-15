@echo off
chcp 65001 >nul
title Sarkar Mitra - Server [STOP]
cls
echo ============================================================
echo   SARKAR MITRA - STOPPING SERVER
echo ============================================================
echo.
echo [*] Freeing port 8000 and stopping server processes...
powershell -NoProfile -Command "Get-NetTCPConnection -LocalPort 8000 -ErrorAction SilentlyContinue | ForEach-Object { Stop-Process -Id $_.OwningProcess -Force -ErrorAction SilentlyContinue }; Write-Output 'Processes cleared.'"
echo.
echo ============================================================
echo   Server has been turned OFF successfully!
echo ============================================================
echo.
ping 127.0.0.1 -n 3 >nul