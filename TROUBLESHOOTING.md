# 🔧 TROUBLESHOOTING - Résolution des Erreurs

## ❌ Erreurs Batch (run.bat ne fonctionne pas)

### Problème: Caractères spéciaux non reconnus
```
'~dp0"' n'est pas reconnu...
'Vérifier' n'est pas reconnu...
'Activer' n'est pas reconnu...
```

**Cause:** Le fichier `run.bat` contient des caractères Unicode/spéciaux

**Solution 1: Utiliser `start.bat` (Plus simple)**
```bash
Double-cliquez sur: start.bat
```

C'est la version simplifiée qui fonctionne mieux!

**Solution 2: Méthode Manuelle (PowerShell)**
```powershell
cd "D:\SFA Works\T-05"
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
streamlit run app.py
```

**Solution 3: Méthode Manuelle (CMD)**
```cmd
cd "D:\SFA Works\T-05"
python -m venv venv
venv\Scripts\activate.bat
pip install -r requirements.txt
streamlit run app.py
```

---

## ❌ Erreur: "python" not found

### Problème
```
'python' n'est pas reconnu en tant que commande interne...
```

**Cause:** Python n'est pas installé ou pas dans le PATH

**Solution 1: Vérifier l'installation**
```bash
python --version
```

Si ce ne fonctionne pas → Python n'est pas installé

**Solution 2: Installer Python**
1. Aller sur https://www.python.org/downloads/
2. Télécharger Python 3.10+ (ou plus récent)
3. **Important:** Cocher "Add Python to PATH" pendant l'installation
4. Installer
5. Redémarrer votre ordinateur
6. Retenter

**Solution 3: Python personnalisé**
```bash
# Trouver le chemin exact:
C:\Users\VOTRE_NOM\AppData\Local\Programs\Python\Python312\python.exe
```

Puis utilisez ce chemin complet au lieu de "python"

---

## ❌ Erreur: "streamlit" not found

### Problème
```
'streamlit' n'est pas reconnu en tant que commande interne...
```

**Cause:** Streamlit n'est pas installé ou l'environnement virtuel n'est pas activé

**Solution 1: Réinstaller Streamlit**
```bash
# PowerShell ou CMD, dans le dossier D:\SFA Works\T-05:
python -m venv venv
.\venv\Scripts\activate       (PowerShell)
  OU
venv\Scripts\activate.bat     (CMD)

pip install streamlit pandas plotly numpy openpyxl
```

**Solution 2: Installation complète**
```bash
pip install -r requirements.txt
```

**Solution 3: Vérifier l'activation**
Vous devez voir `(venv)` au début de votre ligne:
```
(venv) D:\SFA Works\T-05>
```

Si ce n'est pas le cas, l'environnement n'est pas activé!

---

## ❌ Erreur: "Le chemin d'accès spécifié est introuvable"

### Problème
```
Le chemin d'accès spécifié est introuvable.
```

**Cause:** Vous ne êtes pas dans le bon dossier

**Solution:**
```bash
# Allez dans le bon dossier:
cd "D:\SFA Works\T-05"

# Vérifiez que vous voyez les fichiers:
dir
# Vous devriez voir: app.py, requirements.txt, run.bat, etc.

# Puis relancez:
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
streamlit run app.py
```

---

## ❌ Erreur: Port 8501 déjà utilisé

### Problème
```
Port 8501 is already in use.
```

**Cause:** Une autre instance Streamlit utilise le port

**Solution 1: Arrêter l'autre instance**
```bash
# Appuyez sur Ctrl + C dans l'autre fenêtre
```

**Solution 2: Utiliser un autre port**
```bash
streamlit run app.py --server.port 8502
```

**Solution 3: Tuer le processus (Avancé)**
```powershell
# PowerShell en admin:
Get-Process python | Stop-Process
```

---

## ❌ Erreur: "venv" n'existe pas

### Problème
```
Impossible de trouver le dossier venv
```

**Solution:**
```bash
# Créer l'environnement virtuel:
cd "D:\SFA Works\T-05"
python -m venv venv

# Attendez que ça finisse (1-2 minutes)
```

---

## ❌ App plante au démarrage

### Problème
```
Error in app.py
ModuleNotFoundError: No module named 'pandas'
```

**Cause:** Dépendances manquantes

**Solution:**
```bash
# Réinstaller toutes les dépendances:
pip install --upgrade -r requirements.txt
```

---

## ⚠️ App démarre mais affiche une erreur

### Problème
```
Error in app.py (line xxx)
```

**Solution:**
1. Arrêter l'app (Ctrl + C)
2. Vérifier que `app.py` n'a pas d'erreur
3. Relancer: `streamlit run app.py`

Si le problème persiste:
```bash
# Réinstaller Python:
python -m pip install --upgrade pip
pip install -r requirements.txt
```

---

## 🌐 Browser n'ouvre pas automatiquement

### Problème
L'app démarre mais le navigateur ne s'ouvre pas

**Solution:**
1. Ouvrir manuellement: http://localhost:8501
2. Ou chercher le lien dans le terminal
```
You can now view your Streamlit app in your browser.
Local URL: http://localhost:8501
```

---

## ❌ "Le fichier spécifié est introuvable"

### Cause possible
Le fichier batch utilise des chemins incorrects

**Solution: Utiliser `start.bat`**
```bash
Double-cliquez: start.bat
```

C'est la version simplifiée qui fonctionne mieux!

---

## 🔄 Si RIEN ne fonctionne

### Plan B: Méthode Manuelle Complète

**Étape 1: Ouvrir PowerShell**
- Appuyez sur: `Win + X`
- Sélectionnez: `Windows PowerShell`

**Étape 2: Aller dans le dossier**
```powershell
cd "D:\SFA Works\T-05"
```

**Étape 3: Créer environnement**
```powershell
python -m venv venv
```

**Étape 4: Activer environnement**
```powershell
.\venv\Scripts\Activate.ps1
```

**Étape 5: Installer dépendances**
```powershell
pip install -r requirements.txt
```

**Étape 6: Lancer l'app**
```powershell
streamlit run app.py
```

Si vous voyez `http://localhost:8501` → **Success!** ✅

---

## 💡 Tests de Diagnostic

### Test 1: Python fonctionne?
```bash
python --version
# Devrait afficher: Python 3.x.x
```

### Test 2: Pip fonctionne?
```bash
pip --version
# Devrait afficher: pip x.x.x from...
```

### Test 3: Virtualenv fonctionne?
```bash
python -m venv test_env
# Devrait créer un dossier test_env
```

### Test 4: Dépendances installées?
```bash
pip list | findstr streamlit
# Devrait afficher streamlit
```

### Test 5: App.py existe?
```bash
dir app.py
# Devrait afficher app.py
```

---

## 📞 Besoin d'Aide Supplémentaire?

### Ressources
- **Installation.md** - Guide installation détaillé
- **QUICK_START.md** - Démarrage rapide
- **ARCHITECTURE.md** - Aide technique

### Sites Utiles
- https://streamlit.io/
- https://docs.streamlit.io/
- https://www.python.org/

### Commandes de Diagnostic
```bash
# Afficher les infos Python
python -c "import sys; print(sys.version)"

# Afficher le chemin Python
python -c "import sys; print(sys.executable)"

# Lister les packages installés
pip list

# Vérifier Streamlit
pip show streamlit
```

---

## ✅ Checklist Dépannage

- [ ] Python 3.8+ installé?
- [ ] Python dans PATH?
- [ ] Dossier correct (D:\SFA Works\T-05)?
- [ ] Fichiers présents (app.py, requirements.txt)?
- [ ] Virtualenv créé?
- [ ] Virtualenv activé (vous voyez `(venv)`)?
- [ ] Dépendances installées?
- [ ] Port 8501 libre?

**Si toutes les cases sont cochées** ✅ → Ça doit fonctionner!

---

## 🎯 Résolution Rapide

| Erreur | Solution Rapide |
|--------|-----------------|
| Caractères spéciaux | Utilisez `start.bat` |
| Python not found | Installez Python 3.10+ |
| Streamlit not found | `pip install streamlit` |
| Port occupied | `streamlit run app.py --server.port 8502` |
| Path not found | Vérifiez le dossier correct |
| Dépendances manquantes | `pip install -r requirements.txt` |
| Venv n'existe pas | `python -m venv venv` |

---

**Vous avez un autre problème? Décrivez-le et on le résout!** 💪
