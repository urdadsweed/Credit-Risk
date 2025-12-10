@echo off
REM Run this as Administrator to set up auto-start on Windows boot
REM Right-click this file and select "Run as Administrator"

echo.
echo ========================================
echo Setting up Auto-Start on Boot
echo ========================================
echo.

REM Get the full path to app.py
set APP_PATH=%~dp0app.py
set PYTHON_PATH=C:\Users\AVISHKAR LOKHANDE\AppData\Local\Programs\Python\Python311\python.exe

REM Check if Python exists
if not exist "%PYTHON_PATH%" (
    echo ERROR: Python not found at %PYTHON_PATH%
    echo Please update the PYTHON_PATH in this script with your Python installation path.
    pause
    exit /b 1
)

REM Create the scheduled task
echo Creating scheduled task...
schtasks /create /tn "CreditRiskApp" /tr "\"%PYTHON_PATH%\" \"%APP_PATH%\"" /sc onstart /ru SYSTEM /f

if %ERRORLEVEL% EQU 0 (
    echo.
    echo SUCCESS! Credit Risk App will start automatically when Windows boots.
    echo.
    echo The app will be available at: http://localhost:8501
    echo.
    echo To stop auto-start:
    echo   - Open Task Scheduler
    echo   - Find "CreditRiskApp"
    echo   - Right-click and select "Delete"
    echo.
) else (
    echo ERROR: Failed to create scheduled task.
    echo Please make sure you run this as Administrator.
)

pause
