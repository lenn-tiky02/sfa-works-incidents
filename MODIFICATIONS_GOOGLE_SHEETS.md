# 📋 Modifications pour Google Sheets - Résumé Complet

## Vue d'ensemble

L'application a été **modifiée pour utiliser Google Sheets comme source de données unique** à la place du fichier Excel local. Les données sont maintenant :
- ✅ Chargées depuis Google Sheets au démarrage
- ✅ Mises à jour en temps réel quand vous changez une catégorie
- ✅ Synchronisées automatiquement avec le Sheet

---

## Fichiers modifiés / créés

### 1. **app.py** (modifié)
**Ajouts :**
- Imports : `os`, `json`
- Bloc **Google Sheets backend** (lignes 65-130) : 
  - `SHEET_ID` = ID du nouveau Sheet natif
  - Fonctions : `load_sheet_data()`, `ensure_gs_category_column()`, `persist_category_change()`
  - Authentification via `credentials.json`

**Changements logiques :**
- Chargement des données : **Google Sheets prioritaire** → Excel local → données d'exemple
- Écriture des catégories : à chaque changement dans le tableau, sauvegarde immédiate dans le Sheet
- Barre latérale : ajout d'un indicateur d'état (🟢 connecté / 🟠 mode local) + bouton de rechargement

### 2. **requirements.txt** (modifié)
Ajout des dépendances Google :
```
gspread==5.12.4
google-auth==2.35.0
```

### 3. **.gitignore** (créé)
Protection des secrets :
```
credentials.json    ⚠️ Contient une clé secrète
.streamlit/secrets.toml
```

### 4. **Documentation** (créée)
- `GOOGLE_SHEETS_SETUP.md` : guide détaillé
- `QUICK_START_GOOGLE_SHEETS.txt` : démarrage rapide
- `PRE_LAUNCH_CHECKLIST.txt` : vérification avant lancement

---

## Logique de synchronisation

### 📥 **À la lecture (démarrage)**
```
1. Essayer de charger depuis Google Sheets
   └─ Si succès → utiliser ces données
2. Si échecGoogle Sheets)
   └─ Charger depuis Excel local (TO-05.xlsx)
3. Si pas de données
   └─ Utiliser données d'exemple
```

### 📤 **À l'écriture (modification)**
```
Utilisateur change une catégorie dans le tableau
    ↓
render_editable_table() détecte le changement
    ↓
Si Google Sheets connecté:
  → persist_category_change() écrit la cellule au Sheet
  → Invalide le cache load_sheet_data()
  → st.rerun() recharge l'app avec les données à jour
    
Si mode local:
  → Mémoriser la modification en st.session_state.cat_overrides
```

---

## Colonne « Catégorie »

**Comportement :**
- Si elle **existe** dans le Sheet : elle est utilisée/mise à jour
- Si elle **n'existe pas** : elle est créée automatiquement + initialisée avec la catégorisation

**Correspondance exacte :**
- Les lignes vides en fin de feuille sont supprimées (sinon décalage des indices)
- `_ID` = position de la ligne dans les données = ligne du Sheet - 2
- Exemple : `_ID=5` → row 7 du Sheet (en-têtes + 2)

---

## Google Sheet requis

**Type :** Google Sheets **natif** (pas un fichier `.xlsx` importé)

**Structure minimale :**
```
| Colonne1    | Colonne2        | ...  | (Catégorie créée automatiquement)
|─────────────|─────────────────|──────|
| Val 1       | Description ... | ...  |
| Val 2       | Description ... | ...  |
```

**Partage :** Email du compte de service en tant qu'**Éditeur** :
```
to-05-649@unique-hour-385920.iam.gserviceaccount.com
```

**Identifiant actuel :**
```
1a7HZ4sBpNm8XrNjN0zSc4smsmPqTEKderM0G80NTFr0
```

---

## Sécurité

### ⚠️ **credentials.json**
- Contient une clé privée
- **Ne JAMAIS le commiter, le partager, ou le publier**
- `.gitignore` l'exclut automatiquement
- ✅ Vérifier : `git status` ne doit pas le lister

### ✅ **Meilleure pratique**
- Garder `credentials.json` **localement uniquement**
- Sur un serveur en production (ex. Streamlit Cloud) : utiliser des secrets (`.streamlit/secrets.toml`)

---

## Étapes pour démarrer

1. **Installer les dépendances :**
   ```bash
   pip install "gspread==5.12.4" "google-auth==2.35.0"
   ```

2. **Partager le Google Sheet :**
   - Email : `to-05-649@unique-hour-385920.iam.gserviceaccount.com`
   - Permission : **Éditeur**

3. **Lancer l'app :**
   ```bash
   streamlit run app.py
   ```

4. **Vérifier le statut :**
   - Barre latérale doit afficher 🟢 Connecté à Google Sheets
   - Tous les changements de catégorie sont immédiatement sauvegardés

---

## Avantages

✅ **Données centralisées** : une seule source de vérité (le Sheet)  
✅ **Collaboratif** : éditable directement dans le Sheet ou via l'app  
✅ **Persistant** : aucune perte de données, synchronisé en temps réel  
✅ **Scalable** : peut gérer des milliers de lignes  
✅ **Historique** : Google Sheets garde la version history  

---

## Limitations / à connaître

⚠️ **Cache 60 s** : les données sont rechargées toutes les 60 secondes  
⚠️ **Débit** : Google impose ~300 écritures/minute (amplement suffisant)  
⚠️ **Dépôt des changements** : quelques secondes entre l'écriture et la relecture

---

## Fichiers de référence

- `GOOGLE_SHEETS_SETUP.md` : guide complet et troubleshooting
- `QUICK_START_GOOGLE_SHEETS.txt` : résumé en 3 étapes
- `PRE_LAUNCH_CHECKLIST.txt` : vérification avant lancement

---

**Status :** ✅ Code prêt  
**Prochaine étape :** Installer les dépendances + lancer l'app
