@echo off
echo ========================================
echo AI Workout Planner Agent - Setup Script
echo ========================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Python is not installed or not in PATH
    echo Please install Python 3.8 or higher from https://www.python.org/
    pause
    exit /b 1
)

echo [OK] Python found
python --version
echo.

REM Create virtual environment
set /p CREATE_VENV="Do you want to create a virtual environment? (y/n): "

if /i "%CREATE_VENV%"=="y" (
    echo Creating virtual environment...
    python -m venv venv
    
    echo Activating virtual environment...
    call venv\Scripts\activate.bat
    echo [OK] Virtual environment activated
    echo.
)

REM Install requirements
echo Installing required packages...
pip install -r requirements.txt

if errorlevel 1 (
    echo [ERROR] Failed to install packages
    pause
    exit /b 1
)

echo [OK] All packages installed successfully!
echo.

REM Setup .env file
if not exist .env (
    echo Setting up environment variables...
    copy .env.example .env
    echo [OK] Created .env file from template
    echo.
    echo [IMPORTANT] Please edit the .env file and add your OpenAI API key!
    echo You can get one from: https://platform.openai.com/api-keys
    echo.
    pause
    notepad .env
) else (
    echo [OK] .env file already exists
)

echo.
echo ========================================
echo Setup complete!
echo.
echo To run the application:
echo.

if /i "%CREATE_VENV%"=="y" (
    echo 1. Activate the virtual environment:
    echo    venv\Scripts\activate
    echo.
    echo 2. Run the app:
    echo    streamlit run app.py
) else (
    echo    streamlit run app.py
)

echo.
echo Get ready to transform your fitness journey!
echo ========================================
pause
