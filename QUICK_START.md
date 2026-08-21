# ⚡ Démarrage Rapide (2 minutes)

## 🎯 Pour Démarrer Maintenant

### Windows - Méthode la Plus Simple

1. **Double-cliquez sur:** `run.bat`

   ![Double clic](https://via.placeholder.com/400x100?text=Double+clic+sur+run.bat)

2. **Une fenêtre s'ouvre?** ✅ C'est bon!
   - Attendez 30 secondes (première installation)
   - Puis votre navigateur s'ouvre automatiquement

3. **Vous voyez le dashboard?** 🎉 **C'est fini!**

---

### Windows (PowerShell) - Si run.bat ne fonctionne pas

```powershell
# 1. Ouvrir PowerShell (Win + X, A)
cd "D:\SFA Works\T-05"

# 2. Autoriser les scripts (une seule fois)
Set-ExecutionPolicy -ExecutionPolicy Bypass -Scope Process

# 3. Lancer
.\run.ps1

# 4. Voilà! L'app se lance
```

---

### macOS/Linux

```bash
cd ~/SFA\ Works/T-05
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
streamlit run app.py
```

---

## 🌐 Accéder à l'Application

Une fois lancée, l'application est accessible à:

```
http://localhost:8501
```

### Naviguer dans le Dashboard

**Sur la gauche:** Menu de sélection des pages

- 📈 **Vue Générale** - KPIs principaux
- 🩹 **Blessures Corporelles** - Analyse blessures
- 🔓 **Analyse des Vols** - Tendances vols
- ⚡ **Analyse Électrique** - Incidents électriques
- 🏗️ **Construction & Maintenance** - Chantier
- 🎯 **Prévention** - Matrice de risque
- 📤 **Upload Données** - Charger votre Excel

---

## 📊 Premier Pas: Charger vos Données

1. **Cliquez** sur la page **"Upload Données"**
2. **Cliquez** sur "Browse files"
3. **Sélectionnez** votre fichier `TO-05.xlsx`
4. **Les données** s'afficheront automatiquement

---

## 🛑 Arrêter l'Application

```
Ctrl + C  (dans la fenêtre du terminal)
```

---

## ⚠️ Problèmes Courants

### "Python not found"
→ Python n'est pas installé ou pas dans le PATH
→ [Installez Python 3.10+](https://www.python.org)

### Application lente au premier lancement
→ C'est normal! Python télécharge les dépendances
→ Ça dure 1-2 minutes

### Port 8501 occupé
```bash
streamlit run app.py --server.port 8502
```

### Besoin d'aide détaillée?
→ Ouvrez `INSTALLATION.md` pour le guide complet

---

## 🎉 Bravo!

Votre dashboard d'analyse d'incidents est maintenant **prêt à l'emploi**!

**Prochaines étapes:**
- ✅ Charger vos données Excel
- 🤖 Configurer l'IA (bientôt)
- 💾 Connecter la BDD (bientôt)

---

**Questions?** Consultez:
- 📖 `README.md` - Vue d'ensemble
- 🚀 `INSTALLATION.md` - Installation détaillée
- 📊 `app.py` - Code source
