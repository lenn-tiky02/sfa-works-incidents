#!/usr/bin/env pwsh

$projectPath = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location $projectPath

Write-Host "`n" -ForegroundColor White
Write-Host "════════════════════════════════════════════════════" -ForegroundColor Cyan
Write-Host "  Nettoyage et Redemarrage - Analyseur d'Incidents" -ForegroundColor Green
Write-Host "════════════════════════════════════════════════════" -ForegroundColor Cyan
Write-Host "`n"

# Supprimer l'ancien environnement
Write-Host "[1/4] Suppression de l'ancien environnement..." -ForegroundColor Yellow
if (Test-Path "venv") {
    Remove-Item -Recurse -Force venv
    Write-Host "      ✓ Supprimé`n" -ForegroundColor Green
} else {
    Write-Host "      ✓ Rien à supprimer`n" -ForegroundColor Green
}

# Créer nouvel environnement
Write-Host "[2/4] Creation de l'environnement virtuel..." -ForegroundColor Yellow
python -m venv venv
Write-Host "      ✓ Créé`n" -ForegroundColor Green

# Activer
Write-Host "[3/4] Activation de l'environnement..." -ForegroundColor Yellow
& "venv\Scripts\Activate.ps1"
Write-Host "      ✓ Activé`n" -ForegroundColor Green

# Installer dépendances
Write-Host "[4/4] Installation des dependances..." -ForegroundColor Yellow
pip install --upgrade pip setuptools wheel > $null 2>&1
pip install -r requirements.txt

Write-Host "`n"
Write-Host "════════════════════════════════════════════════════" -ForegroundColor Green
Write-Host "  ✓ Redemarrage terminé!" -ForegroundColor Green
Write-Host "════════════════════════════════════════════════════" -ForegroundColor Green
Write-Host "`n"
Write-Host "  Lancement de l'application..." -ForegroundColor White
Write-Host "  Acces a: http://localhost:8501" -ForegroundColor White
Write-Host "  Appuyez sur Ctrl+C pour arreter" -ForegroundColor White
Write-Host "`n"

streamlit run app.py
