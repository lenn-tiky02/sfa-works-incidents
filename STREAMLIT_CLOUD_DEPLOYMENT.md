# 🚀 Déploiement sur Streamlit Cloud - Guide Complet

Streamlit Cloud = **gratuit, officiellement supporté, déploiement en 5 minutes**.

---

## Étape 1 : Initialiser Git (si pas encore fait)

### Dans PowerShell (D:\SFA Works\T-05) :

```powershell
cd "D:\SFA Works\T-05"
git init
git add -A
git commit -m "Initial commit: SFA Works incidents dashboard with Google Sheets integration"
```

**Vérifier :** `git status` doit afficher « On branch master, nothing to commit »

---

## Étape 2 : Créer un dépôt GitHub

### 2.1 Créer un compte GitHub (si pas encore)
- Allez sur https://github.com
- Inscrivez-vous (gratuit)
- Confirmez votre email

### 2.2 Créer un nouveau dépôt
- Cliquez **« + »** en haut à droite → **« New repository »**
- Nom : `sfa-works-incidents` (ou votre choix)
- Privé ou public (conseillé : **Privé** pour les données sensibles)
- **NE cochez PAS** « Initialize with README » (on va pusher depuis local)
- Cliquez **« Create repository »**

### 2.3 Pousser le code vers GitHub

Dans PowerShell :

```powershell
cd "D:\SFA Works\T-05"
git remote add origin https://github.com/VOTRE_USERNAME/sfa-works-incidents.git
git branch -M main
git push -u origin main
```

**⚠️ Important :** Remplacez `VOTRE_USERNAME` par votre nom d'utilisateur GitHub.

**Vérifier :** Allez sur https://github.com/VOTRE_USERNAME/sfa-works-incidents — votre code doit être là.

---

## Étape 3 : Secrets Streamlit Cloud

### ⚠️ CRITIAL : `credentials.json` n'ira PAS sur GitHub

Le fichier `.gitignore` l'exclut déjà. **Vérifiez :**

```powershell
git status
```

`credentials.json` ne doit **pas** apparaître.

### À la place, utiliser les Secrets de Streamlit Cloud

Sur Streamlit Cloud, vous allez copier le contenu de `credentials.json` dans un secret appelé `GOOGLE_CREDENTIALS`.

**Étape :**
1. Allez sur https://share.streamlit.io/
2. Connectez-vous avec votre compte GitHub
3. Une fois l'app déployée, accédez à ses **paramètres** (⚙️)
4. Allez à **« Secrets »**
5. Collez le contenu de `credentials.json` avec la clé `GOOGLE_CREDENTIALS`

---

## Étape 4 : Modifier app.py pour utiliser les Secrets

Streamlit Cloud lit les secrets via `st.secrets`.

### 4.1 Modifier le chargement de credentials.json

Actuellement dans `app.py` :
```python
CREDENTIALS_FILE = os.path.join(...)
creds = Credentials.from_service_account_file(CREDENTIALS_FILE, ...)
```

Changer pour :
```python
import json
import streamlit as st

# En production (Streamlit Cloud)
if 'GOOGLE_CREDENTIALS' in st.secrets:
    creds_dict = st.secrets['GOOGLE_CREDENTIALS']
    creds = Credentials.from_service_account_info(creds_dict, scopes=GS_SCOPES)
# En local (avec credentials.json)
else:
    creds = Credentials.from_service_account_file(CREDENTIALS_FILE, scopes=GS_SCOPES)
```

---

## Étape 5 : Déployer sur Streamlit Cloud

### 5.1 Aller sur https://share.streamlit.io/

Cliquez **« New app »**

### 5.2 Connecter à GitHub

- **Repository :** `https://github.com/VOTRE_USERNAME/sfa-works-incidents`
- **Branch :** `main`
- **Main file path :** `app.py`

Cliquez **« Deploy »** → ⏳ L'app se déploie (quelques minutes)

### 5.3 Configurer les Secrets

1. Une fois l'app en ligne, cliquez sur votre profil (⚙️) en haut à droite
2. **« Edit secrets »**
3. Collez le contenu complet de `credentials.json` :
   ```
   [general]
   GOOGLE_CREDENTIALS = """
   {
     "type": "service_account",
     "project_id": "...",
     ...
   }
   """
   ```
   (Collez le JSON complet entre les triples guillemets)
4. Sauvegardez → L'app redémarre automatiquement

---

## Étape 6 : Partager le Google Sheet

Assurez-vous que le Sheet est **toujours partagé** avec le service account en tant qu'**Éditeur** :

```
to-05-649@unique-hour-385920.iam.gserviceaccount.com
```

---

## Vérification

Après le déploiement, allez sur votre app Streamlit Cloud :
- **URL :** `https://share.streamlit.io/VOTRE_USERNAME/sfa-works-incidents`
- Vérifiez que la barre latérale affiche 🟢 **Connecté à Google Sheets**
- Testez un changement de catégorie → doit être sauvegardé au Sheet

---

## Mettre à jour l'app après déploiement

Chaque fois que vous faites un changement local :

```powershell
cd "D:\SFA Works\T-05"
git add -A
git commit -m "Description du changement"
git push origin main
```

Streamlit Cloud redéploiera **automatiquement** en quelques secondes.

---

## Dépannage

### Erreur « No module named 'gspread' »
→ `requirements.txt` n'inclut pas les dépendances. **Vérifiez** qu'il contient :
```
gspread==5.12.4
google-auth==2.35.0
```

### Erreur « PERMISSION_DENIED » ou « not found »
→ Le service account n'a pas accès au Sheet.
1. Vérifiez que le Sheet est partagé avec `to-05-649@...` en Éditeur
2. Vérifiez que le secret `GOOGLE_CREDENTIALS` est correctement configuré

### L'app affiche une page blanche
→ Erreur Python. Cliquez **« Manage app »** → **« Settings »** → **« View logs »** pour voir l'erreur.

---

## Récapitulatif des URLs

| Élément | URL |
|---------|-----|
| Code source | https://github.com/VOTRE_USERNAME/sfa-works-incidents |
| App en ligne | https://share.streamlit.io/VOTRE_USERNAME/sfa-works-incidents |
| Google Sheet | https://docs.google.com/spreadsheets/d/1a7HZ4sBpNm8XrNjN0zSc4smsmPqTEKderM0G80NTFr0/edit |
| Streamlit Cloud | https://share.streamlit.io |

---

## Coûts

- **Streamlit Cloud** : **100% GRATUIT** (limité à 1 GPU/1 CPU, amplement suffisant)
- **Google Sheets** : **GRATUIT** (illimité)
- **GitHub** : **GRATUIT** (dépôts privés inclus)

**Total : 0 €/mois** 🎉

---

## Points importants

✅ **Sécurité :**
- `credentials.json` reste **local** (pas sur GitHub)
- Secrets stockés **chiffrés** sur Streamlit Cloud
- `.gitignore` protège les fichiers sensibles

✅ **Synchronisation :**
- `git push` → redéploiement automatique
- Modifications au Sheet → visibles immédiatement dans l'app

✅ **Maintenance :**
- Logs accessibles via Streamlit Cloud
- Vous pouvez tester localement avant de pousser

---

## Prochaines étapes

1. ✅ Initialiser Git locally
2. ✅ Créer dépôt GitHub
3. ✅ Pousser le code
4. ✅ Adapter `app.py` pour les secrets
5. ✅ Déployer sur Streamlit Cloud
6. ✅ Configurer les secrets dans le cloud
7. ✅ Partager l'URL de l'app

---

**Questions ? Dites-moi où vous êtes bloqué !** 🚀
