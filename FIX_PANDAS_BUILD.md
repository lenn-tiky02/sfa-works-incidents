# 🔧 FIX - Erreur ModuleNotFoundError: pkg_resources

## ❌ Problème

```
ModuleNotFoundError: No module named 'pkg_resources'
× Getting requirements to build wheel did not run successfully.
```

Cela se produit quand pip essaie de compiler pandas depuis les sources au lieu d'utiliser une version pré-compilée (wheel).

## 🔍 Raison

- `pandas==2.0.3` demande une compilation
- Python 3.12 a besoin de `pkg_resources` pour compiler
- Le wheel pré-compilé n'est pas disponible pour cette version
- Solution: Utiliser une version plus récente de pandas qui a un wheel

## ✅ Solution 1: Fichier requirements.txt Mis à Jour (Recommandé)

Le fichier `requirements.txt` a été mis à jour:

```
streamlit==1.28.1
pandas==2.1.4       ← CHANGÉ (avait 2.0.3)
openpyxl==3.1.5
plotly==5.17.0
```

`pandas==2.1.4` a un wheel pré-compilé pour Python 3.12 → Pas de compilation!

## ✅ Solution 2: Nettoyer et Recommencer (Recommandé)

```powershell
cd "D:\SFA Works\T-05"

# Supprimer l'ancien environnement (qui a l'erreur):
Remove-Item -Recurse -Force venv

# Relancer avec le nouveau fichier:
.\launch.ps1
```

Ou simplement:
```bash
start.bat
```

## ✅ Solution 3: Utiliser requirements_minimal.txt

Le fichier `requirements_minimal.txt` utilise les **dernières versions stables** sans version fixe:

```
streamlit
pandas
plotly
openpyxl
```

Pour l'utiliser:
```powershell
pip install -r requirements_minimal.txt
streamlit run app.py
```

## ✅ Solution 4: Installation Manuelle (Si rien ne fonctionne)

```powershell
cd "D:\SFA Works\T-05"
python -m venv venv
.\venv\Scripts\Activate.ps1

# Installer les dépendances une par une:
pip install --upgrade pip setuptools wheel
pip install streamlit
pip install pandas
pip install plotly
pip install openpyxl

# Lancer:
streamlit run app.py
```

---

## 📋 Résumé des Fichiers

### requirements.txt (Standard)
```
✅ streamlit==1.28.1
✅ pandas==2.1.4       (CORRIGÉ)
✅ openpyxl==3.1.5
✅ plotly==5.17.0
```

### requirements_minimal.txt (Flexible)
```
✅ streamlit
✅ pandas
✅ plotly
✅ openpyxl
```

Utilisez celui qui fonctionne pour vous!

---

## 🚀 Prochaines Étapes

### Option 1: Recommencé à Zéro (Safest)
```powershell
Remove-Item -Recurse -Force venv
.\launch.ps1
```

### Option 2: Mettre à Jour l'Environnement Existant
```powershell
cd "D:\SFA Works\T-05"
.\venv\Scripts\Activate.ps1
pip install --upgrade pip setuptools wheel
pip install -r requirements.txt --upgrade
streamlit run app.py
```

### Option 3: Utiliser la Version Minimale
```powershell
pip install -r requirements_minimal.txt
streamlit run app.py
```

---

## ✅ Vérification

Après installation, vérifiez:

```powershell
pip list | findstr pandas
# Devrait afficher: pandas 2.1.4 ou plus récent

pip list | findstr streamlit
# Devrait afficher: streamlit 1.28.1
```

---

## 🎯 Résumé

| Avant | Après |
|-------|-------|
| ❌ pandas==2.0.3 | ✅ pandas==2.1.4 |
| ❌ Compilation échoue | ✅ Wheel pré-compilé |
| ❌ ModuleNotFoundError | ✅ Installation OK |

---

## 💡 Pourquoi ça fonctionne maintenant?

- `pandas==2.1.4` a un wheel pré-compilé pour Windows + Python 3.12
- Pas besoin de compiler → pas besoin de `pkg_resources` → Pas d'erreur!
- Installation 10x plus rapide

---

## 🎉 Prêt?

Relancez avec:
```bash
start.bat
```

Ou:
```powershell
.\launch.ps1
```

Le dashboard devrait s'afficher cette fois! ✅
