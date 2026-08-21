#!/usr/bin/env pwsh

# Script de lancement - Analyseur d'Incidents SFA Works

Set-Location (Split-Path -Parent $MyInvocation.MyCommand.Path)

Write-Host "`n" -ForegroundColor White
Write-Host "================================================" -ForegroundColor Cyan
Write-Host "  Analyseur d'Incidents - SFA Works" -ForegroundColor Cyan
Write-Host "================================================" -ForegroundColor Cyan

# Vérifier si l'environnement virtuel existe
if (-not (Test-Path "venv")) {
    Write-Host "`n[*] Création de l'environnement virtuel..." -ForegroundColor Yellow
    python -m venv venv
}

# Activer l'environnement virtuel
Write-Host "`n[*] Activation de l'environnement virtuel..." -ForegroundColor Yellow
& "venv\Scripts\Activate.ps1"

# Installer les dépendances
Write-Host "`n[*] Vérification des dépendances..." -ForegroundColor Yellow
pip install -q -r requirements.txt

# Lancer Streamlit
Write-Host "`n" -ForegroundColor White
Write-Host "================================================" -ForegroundColor Green
Write-Host "  ✓ Lancement de l'application..." -ForegroundColor Green
Write-Host "================================================" -ForegroundColor Green
Write-Host ""
Write-Host "  L'application s'ouvrira à: http://localhost:8501" -ForegroundColor White
Write-Host ""
Write-Host "  Appuyez sur Ctrl+C pour arrêter" -ForegroundColor White
Write-Host ""
Write-Host "================================================" -ForegroundColor Green
Write-Host "`n"

streamlit run app.py
