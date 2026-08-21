@echo off
cd /d "%~dp0"

echo.
echo ================================================
echo  Nettoyage et Redemarrage
echo ================================================
echo.

echo [1/4] Suppression de l'ancien environnement...
if exist venv (
    rmdir /s /q venv
    echo       OK
) else (
    echo       Rien a supprimer
)

echo.
echo [2/4] Creation de l'environnement...
python -m venv venv
echo       OK

echo.
echo [3/4] Activation de l'environnement...
call venv\Scripts\activate.bat
echo       OK

echo.
echo [4/4] Installation des dependances...
pip install --upgrade pip setuptools wheel > nul 2>&1
pip install -r requirements.txt

echo.
echo ================================================
echo  Redemarrage termine!
echo ================================================
echo.
echo  Lancement de l'application...
echo  Acces a: http://localhost:8501
echo  Appuyez sur Ctrl+C pour arreter
echo.

streamlit run app.py
pause
