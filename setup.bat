@echo off
REM Ensure we are in the correct directory
cd %~dp0

REM Create a virtual environment
python -m venv venv

REM Activate the virtual environment
call venv\Scripts\activate

REM Upgrade pip to the latest version
python -m pip install --upgrade pip

REM Install the required packages from requirements.txt
pip install -r requirements.txt

REM Install Playwright browsers
python -m playwright install

echo Setup is complete. Now you can work with in the virtual environment