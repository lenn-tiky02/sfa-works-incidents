# 🚀 Guide d'Installation - Analyseur d'Incidents

## ✅ Prérequis

- **Windows 10/11** (ou macOS/Linux)
- **Python 3.8+** - [Télécharger ici](https://www.python.org/downloads/)
- **Connexion Internet** (pour les dépendances)
- **Git** (optionnel)

---

## 📋 Vérifier que Python est Installé

Ouvrez **PowerShell** ou **Invite de Commandes** et tapez:

```bash
python --version
```

Vous devriez voir quelque chose comme: `Python 3.12.8`

Si ce n'est pas le cas, [installez Python ici](https://www.python.org/downloads/).

---

## 🚀 Option 1: Lancement Automatique (Recommandé)

### Sur Windows

**Méthode 1: Double-cliquez sur `run.bat`**
```
D:\SFA Works\T-05\run.bat
```
C'est le plus simple - tout se fera automatiquement!

**Méthode 2: PowerShell**
```powershell
cd "D:\SFA Works\T-05"
Set-ExecutionPolicy -ExecutionPolicy Bypass -Scope Process
.\run.ps1
```

### Sur macOS/Linux

```bash
cd ~/SFA\ Works/T-05
./run.sh  # À créer si nécessaire
```

---

## 🔧 Option 2: Installation Manuelle (Pas à Pas)

Si le lancement automatique ne fonctionne pas, suivez ces étapes:

### Étape 1: Ouvrir le Terminal

**Windows (Recommandé PowerShell):**
```
Touches: Win + X, puis A (ou ouvrir PowerShell depuis Start Menu)
```

**Ou Invite de Commandes:**
```
Touches: Win + R, puis cmd, puis Entrée
```

### Étape 2: Aller dans le Dossier du Projet

```bash
cd "D:\SFA Works\T-05"
```

Vérifiez que vous êtes au bon endroit:
```bash
dir  # Vous devriez voir: app.py, requirements.txt, setup.bat, etc.
```

### Étape 3: Créer un Environnement Virtuel

```bash
python -m venv venv
```

Cela crée un dossier `venv/` qui contient Python isolé pour ce projet.

### Étape 4: Activer l'Environnement Virtuel

**PowerShell:**
```powershell
.\venv\Scripts\Activate.ps1
```

**Invite de Commandes:**
```cmd
venv\Scripts\activate.bat
```

**Bash (macOS/Linux):**
```bash
source venv/bin/activate
```

Vous devriez voir `(venv)` au début de votre ligne de commande.

### Étape 5: Installer les Dépendances

```bash
pip install -r requirements.txt
```

Cela télécharge et installe:
- ✅ streamlit - le framework web
- ✅ pandas - manipulation de données
- ✅ openpyxl - lecture Excel
- ✅ plotly - graphiques interactifs
- ✅ numpy - calculs numériques

### Étape 6: Lancer l'Application

```bash
streamlit run app.py
```

L'application s'ouvrira automatiquement dans votre navigateur:
```
http://localhost:8501
```

---

## ✨ Vous Y Êtes!

L'application devrait maintenant afficher:

```
  👋 Welcome to Streamlit!
  
  If you're one of our development team members...
```

Et votre dashboard sera accessible au lien indiqué.

---

## ⚠️ Troubleshooting

### "Python not found"
```bash
# Python n'est pas dans le PATH
# Solution: Réinstallez Python avec ✓ "Add Python to PATH"
```

### "Permission denied" sur `run.ps1`

```powershell
# Autoriser l'exécution de scripts:
Set-ExecutionPolicy -ExecutionPolicy Bypass -Scope CurrentUser
```

### "Module not found: streamlit"

```bash
# L'environnement virtuel n'est pas activé
# Refaites l'Étape 4 ci-dessus
```

### Port 8501 déjà utilisé

```bash
# Lancer sur un autre port:
streamlit run app.py --server.port 8502
```

### Installation très lente

```bash
# Sauter torch (lourd):
pip install streamlit pandas openpyxl plotly numpy
```

---

## 📂 Structure du Projet

```
T-05/
├── app.py                 # Application principale ⭐
├── requirements.txt       # Dépendances Python
├── run.bat               # 🎯 Lancer sur Windows (double-clic)
├── run.ps1               # Lancer sur PowerShell
├── setup.bat             # Setup initial (optionnel)
├── README.md             # Documentation générale
├── INSTALLATION.md       # Ce fichier
├── .gitignore            # Fichiers ignorés par Git
├── .streamlit/
│   └── config.toml       # Configuration Streamlit
└── venv/                 # 📦 Environnement virtuel (créé après setup)
```

---

## 🎯 Prochaines Étapes

1. ✅ **Environnement créé?** → Continuez!
2. 📤 **Upload votre fichier Excel** via la page "Upload Données"
3. 🤖 **Catégorisation IA** (bientôt)
4. 💾 **Sauvegarde en BDD** (à configurer)

---

## 💡 Astuces

**Pour arrêter l'application:**
```
Ctrl + C dans le terminal
```

**Pour redémarrer l'application:**
```
Ctrl + C, puis streamlit run app.py
```

**Pour réinstaller les dépendances:**
```bash
pip install --upgrade -r requirements.txt
```

**Pour ajouter une nouvelle dépendance:**
```bash
pip install nom_du_package
pip freeze > requirements.txt
```

---

## 📞 Support

- 📖 [Documentation Streamlit](https://docs.streamlit.io/)
- 🐍 [Documentation Python](https://docs.python.org/3/)
- 💬 Questions? Consultez le README.md

---

**Besoin d'aide? C'est normal - Python peut être complexe au premier lancement. N'hésitez pas à demander!** 🙌
