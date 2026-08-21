@echo off
cd /d "%~dp0"
python -m venv venv > nul 2>&1
call venv\Scripts\activate.bat
pip install -r requirements.txt > nul 2>&1
streamlit run app.py
