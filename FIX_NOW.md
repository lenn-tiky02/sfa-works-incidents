# 🔧 FIX IMMÉDIAT - Erreurs Batch

## ❌ Problème que Vous Avez

Le fichier `run.bat` contient des caractères spéciaux non reconnus par Windows.

Les erreurs:
```
'~dp0"' n'est pas reconnu...
'Vérifier' n'est pas reconnu...
'Activer' n'est pas reconnu...
```

## ✅ Solution 1: Utiliser `start.bat` (Le Plus Simple)

**Double-cliquez sur:** `start.bat`

C'est la version simplifiée qui fonctionne! Pas d'erreur.

---

## ✅ Solution 2: Utiliser `run_simple.bat` (Alternative)

**Double-cliquez sur:** `run_simple.bat`

Même chose, version ultra-simple.

---

## ✅ Solution 3: Méthode Manuelle (Si les .bat ne fonctionnent pas)

### Étape 1: Ouvrir PowerShell
- Appuyez sur: `Win + X`
- Sélectionnez: `Windows PowerShell` (pas Windows Terminal)

### Étape 2: Aller dans le dossier
```powershell
cd "D:\SFA Works\T-05"
```

### Étape 3: Créer l'environnement
```powershell
python -m venv venv
```

Attendez 1-2 minutes...

### Étape 4: Activer l'environnement
```powershell
.\venv\Scripts\Activate.ps1
```

Vous devez voir `(venv)` au début de la ligne.

### Étape 5: Installer les dépendances
```powershell
pip install -r requirements.txt
```

Attendez 2-3 minutes...

### Étape 6: Lancer l'app
```powershell
streamlit run app.py
```

Attendez que vous voyez:
```
You can now view your Streamlit app in your browser.
Local URL: http://localhost:8501
```

---

## 🌐 Résultat Attendu

Une fenêtre de navigateur s'ouvre à:
```
http://localhost:8501
```

Vous voyez le dashboard avec les 7 pages. ✅

---

## ⚠️ Si Vous Avez Encore des Erreurs

### Erreur: "python not found"
**Solution:** Python n'est pas installé
- Installer Python 3.10+ de https://www.python.org
- **Important:** Cocher "Add Python to PATH" lors de l'installation
- Redémarrer l'ordinateur
- Retenter

### Erreur: "Le dossier est introuvable"
**Solution:** Vous n'êtes pas dans le bon dossier
```powershell
# Vérifiez que vous voyez:
dir
# app.py, requirements.txt, start.bat, etc.
```

### Erreur: "venv" n'existe pas
**Solution:** Créer le dossier venv
```powershell
python -m venv venv
```

---

## 🎯 Résumé

**Si les .bat ne fonctionnent pas:**

→ Utilisez la méthode manuelle ci-dessus (PowerShell)

**C'est plus de travail mais c'est fiable!**

---

## 📋 Checklist Avant de Relancer

- [ ] Python installé? (`python --version`)
- [ ] Dans le bon dossier? (D:\SFA Works\T-05)
- [ ] Fichiers présents? (app.py, requirements.txt, etc.)
- [ ] Virtualenv créé? (dossier `venv` existe?)
- [ ] Virtualenv activé? (vous voyez `(venv)` dans PowerShell?)
- [ ] Dépendances installées? (`pip list` affiche streamlit, pandas, etc.)

**Si tout est OK** → `streamlit run app.py`

---

## 💡 Astuce

Si vous avez toujours des problèmes:

```powershell
# Recommencer à zéro:
python -m venv venv_new
.\venv_new\Scripts\Activate.ps1
pip install streamlit pandas plotly numpy openpyxl
streamlit run app.py
```

---

**Ça fonctionne maintenant?** ✅ Bienvenue au dashboard!

**Toujours des problèmes?** Consultez `TROUBLESHOOTING.md` pour plus d'aide.
