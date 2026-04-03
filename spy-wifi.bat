@echo off
color 0c
title SPY-WIFI-HARVESTER
echo [*] Pulling all saved WiFi Passwords...
echo ------------------------------------------
for /f "tokens=4,*" %%i in ('netsh wlan show profiles ^| findstr /C:"All User Profile"') do (
    set ssid=%%j
    call :get_pass "%%j"
)
pause
goto :eof

:get_pass
set "name=%~1"
for /f "tokens=2 delims=:" %%p in ('netsh wlan show profile name^="%name%" key^=clear ^| findstr "Key Content"') do (
    echo SSID: %name% ^| Password: %%p
)
