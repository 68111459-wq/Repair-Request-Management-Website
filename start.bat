@echo off
title Repair Request Management System

cd /d "%~dp0"

echo ================================
echo Repair Request Management System
echo ================================
echo.

echo Checking virtual environment...

if not exist venv (
    echo Creating virtual environment...
    python -m venv venv
)

echo.
echo Activating virtual environment...
call venv\Scripts\activate

echo.
echo Installing requirements...
python -m pip install -r requirements.txt

echo.
echo Creating sample data...
python seed.py

echo Web app will open automatically in 5 seconds...
start "" cmd /c "timeout /t 5 >nul && start http://localhost:8000/web"
echo.
echo Starting FastAPI server...
python -m uvicorn main:app --reload

pause