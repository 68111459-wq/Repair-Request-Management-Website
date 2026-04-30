@echo off
title Run Unit Tests - Repair Request System

cd /d "%~dp0"

echo ================================
echo Repair Request Management System
echo Running Unit Tests
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
echo Running pytest...
python -m pytest -v

echo.
echo ================================
echo Test finished
echo ================================

pause