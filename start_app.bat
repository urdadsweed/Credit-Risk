@echo off
REM Credit Risk Assessment Calculator - Startup Script
REM This script will start the Flask app

cd /d "%~dp0"
title Credit Risk Assessment App - Running on http://localhost:8501
color 0A

echo.
echo ========================================
echo Credit Risk Assessment Calculator
echo ========================================
echo.
echo Starting application...
echo.

python app.py

pause
