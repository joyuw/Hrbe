@echo off
chcp 65001 >nul
echo ==========================================
echo  Fixing DNS Settings - سورس اوروك
echo ==========================================
echo.

:: Flush DNS cache
echo [1/4] Flushing DNS cache...
ipconfig /flushdns

:: Reset Winsock
echo [2/4] Resetting Winsock...
netsh winsock reset

:: Reset TCP/IP stack
echo [3/4] Resetting TCP/IP...
netsh int ip reset

:: Set Google DNS for all active adapters
echo [4/4] Setting Google DNS (8.8.8.8)...
for /f "skip=1 tokens=*" %%a in ('wmic nic where "NetEnabled=true" get NetConnectionID /value 2^>nul') do (
    for /f "tokens=2 delims==" %%b in ("%%a") do (
        echo     Setting DNS for: %%b
        netsh interface ip set dns "%%b" static 8.8.8.8 primary >nul 2>&1
        netsh interface ip add dns "%%b" 8.8.4.4 index=2 >nul 2>&1
    )
)

echo.
echo ==========================================
echo  Done! Restart your computer.
echo  تم التعديل! ريستارت الجهاز مطلوب.
echo ==========================================
pause
