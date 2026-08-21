#!/usr/bin/env pwsh

$projectPath = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location $projectPath

Write-Host "`n================================================`n" -ForegroundColor Cyan
Write-Host "  Analyseur d'Incidents - SFA Works" -ForegroundColor Green
Write-Host "`n================================================`n" -ForegroundColor Cyan

# Creer l'environnement virtuel s'il n'existe pas
if (-not (Test-Path "venv")) {
    Write-Host "[*] Creation de l'environnement virtuel..." -ForegroundColor Yellow
    python -m venv venv
}

# Activer l'environnement
Write-Host "[*] Activation de l'environnement..." -ForegroundColor Yellow
& "venv\Scripts\Activate.ps1"

# Installer les dependances
Write-Host "[*] Installation des dependances..." -ForegroundColor Yellow
pip install -r requirements.txt --quiet

Write-Host "`n================================================`n" -ForegroundColor Green
Write-Host "[+] Lancement de l'application..." -ForegroundColor Green
Write-Host "`nAcces a: http://localhost:8501`n" -ForegroundColor White
Write-Host "Appuyez sur Ctrl+C pour arreter`n" -ForegroundColor White
Write-Host "================================================`n" -ForegroundColor Green

streamlit run app.py
