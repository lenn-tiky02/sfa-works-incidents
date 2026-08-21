@echo off
cd /d "%~dp0"

echo.
echo ================================================
echo      Lancement du Dashboard SFA Works
echo ================================================
echo.

if not exist "venv\" (
    echo Installation de l'environnement virtuel...
    python -m venv venv
)

echo Activation environnement...
call venv\Scripts\activate.bat

echo Installation des dependances...
pip install -r requirements.txt

echo.
echo ================================================
echo.
echo Acces a: http://localhost:8501
echo.
echo Appuyez sur Ctrl+C pour arreter
echo.
echo ================================================
echo.

streamlit run app.py
pause
