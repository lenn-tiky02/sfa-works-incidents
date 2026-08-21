# Script de setup pour le projet Streamlit - SFA Works

Write-Host "================================" -ForegroundColor Cyan
Write-Host "Setup du Projet - Analyseur d'Incidents" -ForegroundColor Cyan
Write-Host "================================" -ForegroundColor Cyan
Write-Host ""

# Vérifier si Python est installé
Write-Host "✓ Vérification de Python..." -ForegroundColor Yellow
python --version
if ($LASTEXITCODE -ne 0) {
    Write-Host "✗ Python n'est pas installé ou n'est pas dans PATH" -ForegroundColor Red
    exit 1
}

# Créer l'environnement virtuel
Write-Host ""
Write-Host "✓ Création de l'environnement virtuel..." -ForegroundColor Yellow
python -m venv venv

# Activer l'environnement virtuel
Write-Host ""
Write-Host "✓ Activation de l'environnement virtuel..." -ForegroundColor Yellow
& "venv\Scripts\Activate.ps1"

# Mettre à jour pip
Write-Host ""
Write-Host "✓ Mise à jour de pip..." -ForegroundColor Yellow
python -m pip install --upgrade pip

# Installer les dépendances
Write-Host ""
Write-Host "✓ Installation des dépendances..." -ForegroundColor Yellow
pip install -r requirements.txt

Write-Host ""
Write-Host "================================" -ForegroundColor Green
Write-Host "✓ Setup Terminé avec Succès!" -ForegroundColor Green
Write-Host "================================" -ForegroundColor Green
Write-Host ""
Write-Host "Prochaines étapes:" -ForegroundColor Cyan
Write-Host "1. Assurez-vous que l'environnement virtuel est activé:" -ForegroundColor White
Write-Host "   .\venv\Scripts\Activate.ps1" -ForegroundColor Magenta
Write-Host ""
Write-Host "2. Lancez l'application:" -ForegroundColor White
Write-Host "   streamlit run app.py" -ForegroundColor Magenta
Write-Host ""
Write-Host "3. L'application s'ouvrira à: http://localhost:8501" -ForegroundColor White
Write-Host ""
