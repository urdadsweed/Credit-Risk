@echo off
echo Installing dependencies...
pip install -r requirements.txt

echo.
echo Starting Credit Risk Prediction App...
python app.py
pause
