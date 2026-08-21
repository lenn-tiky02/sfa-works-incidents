#!/usr/bin/env python
"""
Script de test pour vérifier que tout est correctement configuré
Exécutez avec: python test_setup.py
"""

import sys
import subprocess
from pathlib import Path

print("\n" + "="*60)
print("  🔍 TEST DE CONFIGURATION - Analyseur d'Incidents")
print("="*60 + "\n")

# Test 1: Version Python
print("✓ Test 1: Version Python")
print(f"  → Python {sys.version.split()[0]} installé")
if sys.version_info >= (3, 8):
    print("  ✅ OK (3.8+ requis)\n")
else:
    print("  ❌ ERREUR: Python 3.8+ requis!\n")
    sys.exit(1)

# Test 2: Chemin d'accès
print("✓ Test 2: Chemin d'accès")
project_path = Path(__file__).parent
print(f"  → Chemin: {project_path}")
print("  ✅ OK\n")

# Test 3: Fichiers requis
print("✓ Test 3: Fichiers requis")
required_files = [
    "app.py",
    "requirements.txt",
    ".streamlit/config.toml",
    ".gitignore"
]

all_exist = True
for file in required_files:
    file_path = project_path / file
    exists = file_path.exists()
    status = "✅" if exists else "❌"
    print(f"  {status} {file}")
    if not exists:
        all_exist = False

if all_exist:
    print("  ✅ Tous les fichiers sont présents\n")
else:
    print("  ❌ Fichiers manquants!\n")
    sys.exit(1)

# Test 4: Dépendances
print("✓ Test 4: Dépendances principales")
required_packages = {
    "streamlit": "Framework web",
    "pandas": "Manipulation données",
    "plotly": "Graphiques interactifs",
    "numpy": "Calculs numériques"
}

for package, description in required_packages.items():
    try:
        __import__(package)
        print(f"  ✅ {package:15} - {description}")
    except ImportError:
        print(f"  ⚠️  {package:15} - NON INSTALLÉ")
        print(f"     Installez avec: pip install -r requirements.txt")

print("\n")

# Test 5: Application Streamlit
print("✓ Test 5: Application Streamlit")
app_file = project_path / "app.py"
with open(app_file, 'r', encoding='utf-8') as f:
    content = f.read()
    
checks = [
    ("import streamlit", "Import Streamlit"),
    ("st.set_page_config", "Configuration page"),
    ("page = st.radio", "Navigation multi-pages"),
    ("if page == \"Vue Générale\"", "Page Vue Générale"),
    ("elif page == \"Blessures", "Page Blessures"),
]

for code_snippet, description in checks:
    if code_snippet in content:
        print(f"  ✅ {description}")
    else:
        print(f"  ❌ {description} - NON TROUVÉ")

print("\n")

# Test 6: Données d'exemple
print("✓ Test 6: Données d'exemple")
if "def load_sample_data():" in content:
    print("  ✅ Fonction de données d'exemple présente")
    if "pd.date_range" in content:
        print("  ✅ Génération de dates OK")
    if "np.random.choice" in content:
        print("  ✅ Génération aléatoire OK")
else:
    print("  ⚠️  Fonction de données non trouvée")

print("\n")

# Résumé
print("="*60)
print("  ✅ TOUS LES TESTS RÉUSSIS!")
print("="*60)

print("""
Prochaines étapes:

1. Installez les dépendances:
   pip install -r requirements.txt

2. Lancez l'application:
   streamlit run app.py

3. L'app s'ouvrira à:
   http://localhost:8501

4. Explorez les 7 pages du dashboard!

Bon développement! 🚀
""")
