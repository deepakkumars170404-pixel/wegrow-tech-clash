@echo off
cd /d "D:\WEGROW\14.Game"
title Tech Clash Arena Server
echo ========================================================
echo         STARTING TECH CLASH ARENA SERVER
echo ========================================================
echo.
echo Freeing port 3000...
powershell -NoProfile -Command "Get-NetTCPConnection -LocalPort 3000 -ErrorAction SilentlyContinue | ForEach-Object { Stop-Process -Id $_.OwningProcess -Force -ErrorAction SilentlyContinue }" >nul 2>&1
timeout /t 1 /nobreak >nul
echo Starting server...
node server.js
pause
