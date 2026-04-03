@echo off
title SPY-WIFI-EXTRACTOR [123Tool]
color 0b
echo ==========================================
echo    SPY-WIFI-EXTRACTOR (NAGA-PASS)
echo    Coded by SPY-E & 123Tool
echo ==========================================
echo.
echo [*] Sedang menarik data password...
echo ------------------------------------------

setlocal enabledelayedexpansion

for /f "tokens=2 delims=:" %%a in ('netsh wlan show profiles ^| findstr "All User Profile"') do (
    set ssid=%%a
    set ssid=!ssid:~1!
    for /f "tokens=2 delims=:" %%b in ('netsh wlan show profile name^="!ssid!" key^=clear ^| findstr "Key Content"') do (
        set pass=%%b
        echo SSID: !ssid! ^| Password: !pass:~1!
    )
)

echo.
echo ------------------------------------------
echo [+] Ekstraksi Selesai, Bosku!
pause
