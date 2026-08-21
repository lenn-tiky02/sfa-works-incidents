@echo off
chcp 65001 > nul
color 0A
cls

echo ================================
echo Setup du Projet - Analyseur d'Incidents
echo ================================
echo.

REM Vérifier si Python est installé
echo ✓ Vérification de Python...
python --version
if errorlevel 1 (
    color 0C
    echo ✗ Python n'est pas installé ou n'est pas dans PATH
    pause
    exit /b 1
)

REM Créer l'environnement virtuel
echo.
echo ✓ Création de l'environnement virtuel...
python -m venv venv

REM Installer les dépendances
echo.
echo ✓ Installation des dépendances...
call venv\Scripts\activate.bat
python -m pip install --upgrade pip
pip install -r requirements.txt

echo.
echo ================================
echo ✓ Setup Terminé avec Succès!
echo ================================
echo.
echo Prochaines étapes:
echo 1. Lancez l'application:
echo    streamlit run app.py
echo.
echo 2. L'application s'ouvrira à: http://localhost:8501
echo.
pause
