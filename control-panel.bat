@echo off
chcp 65001 >nul
title Sarkar Mitra - Control Panel
:menu
cls
echo ============================================================
echo   SARKAR MITRA - SERVER CONTROL PANEL
echo ============================================================
echo.
echo   [1] START Server (Turn ON)
echo   [2] STOP Server  (Turn OFF)
echo   [3] CHECK Status (Online / Offline)
echo   [4] OPEN Browser (http://localhost:8000)
echo   [5] SHARE on Mobile / Other Devices (Tunnel & QR)
echo   [6] EXIT
echo.
echo ============================================================
set /p opt="Select an option (1-6): "

if "%opt%"=="1" goto start_server
if "%opt%"=="2" goto stop_server
if "%opt%"=="3" goto check_status
if "%opt%"=="4" goto open_browser
if "%opt%"=="5" goto share_tunnel
if "%opt%"=="6" goto exit_panel
goto menu

:start_server
cls
echo Starting server in a new window...
start "Sarkar Mitra Server" cmd /k "cd /d C:\Users\Lenovo\.gemini\antigravity\scratch\aaple-sarkar-bot && python start.py"
timeout /t 2 >nul
start "" http://localhost:8000
goto menu

:stop_server
cls
echo Stopping server on port 8000 and closing tunnels...
powershell -NoProfile -Command "Get-NetTCPConnection -LocalPort 8000 -ErrorAction SilentlyContinue | ForEach-Object { Stop-Process -Id $_.OwningProcess -Force -ErrorAction SilentlyContinue }; Get-Process cloudflared -ErrorAction SilentlyContinue | Stop-Process -Force -ErrorAction SilentlyContinue; Write-Output 'Done.'"
echo.
echo Server and tunnels stopped.
pause
goto menu

:check_status
cls
echo Checking server status on port 8000...
powershell -NoProfile -Command "try { $r = Invoke-RestMethod -Uri 'http://127.0.0.1:8000/health' -TimeoutSec 2; Write-Host 'SERVER IS ONLINE (Healthy)' -ForegroundColor Green; Write-Host ('Service: ' + $r.service); Write-Host ('Loaded Schemes: ' + $r.schemes_loaded) } catch { Write-Host 'SERVER IS CURRENTLY OFFLINE' -ForegroundColor Red }"
echo.
pause
goto menu

:open_browser
start "" http://localhost:8000
goto menu

:share_tunnel
cls
echo Launching Mobile & Device Tunnel with QR code...
start "Sarkar Mitra Mobile Tunnel" cmd /k "cd /d C:\Users\Lenovo\.gemini\antigravity\scratch\aaple-sarkar-bot && python tunnel.py"
goto menu

:exit_panel
exit
