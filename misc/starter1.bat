cls


:start


start "" "start.bat"

timeout /T 10

TASKKILL /F /IM python3.9.exe /T

goto start