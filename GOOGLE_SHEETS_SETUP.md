# 🚀 Configuration Google Sheets - Prochaines Étapes

## ✅ Étape 1 : Installer les dépendances Google (CRITICAL)

Ouvrez **PowerShell** dans `D:\SFA Works\T-05` et exécutez :

```powershell
cd "D:\SFA Works\T-05"
.\venv\Scripts\python.exe -m pip install "gspread==5.12.4" "google-auth==2.35.0"
```

Attendez que l'installation termine (quelques secondes).

---

## ✅ Étape 2 : Vérifier le partage du Google Sheet

**IMPORTANT** : Le Google Sheet doit être **partagé en Éditeur** avec le compte de service.

1. Ouvrez ce lien : https://docs.google.com/spreadsheets/d/1a7HZ4sBpNm8XrNjN0zSc4smsmPqTEKderM0G80NTFr0/edit
2. Cliquez sur **Partager** (en haut à droite)
3. Cochez que le Sheet est partagé avec cet email en tant qu'**Éditeur** :
   ```
   to-05-649@unique-hour-385920.iam.gserviceaccount.com
   ```
   
   Si ce compte n'apparaît pas, ajoutez-le via « Ajouter des personnes ou des groupes ».

---

## ✅ Étape 3 : Lancer l'application

Toujours dans PowerShell (même répertoire) :

```powershell
.\venv\Scripts\streamlit.exe run app.py
```

Un navigateur s'ouvrira automatiquement sur `http://localhost:8501`.

---

## 🟢 Quand tout fonctionne

Au démarrage, la barre latérale affichera :

```
🟢 Connecté à Google Sheets
🔄 Recharger depuis Google Sheets
```

Cela signifie que l'application a :
- ✅ Chargé les données depuis le Google Sheet
- ✅ Créé ou détecté la colonne `Catégorie`
- ✅ Activé la persistance (tout changement de catégorie est sauvegardé au Sheet)

---

## 🟠 Si vous voyez une erreur

### Erreur : « Fichier credentials.json introuvable »
→ Le fichier `credentials.json` n'est pas dans `D:\SFA Works\T-05\`.
**Action** : Assurez-vous qu'il est là (question de chemin).

### Erreur : « PERMISSION_DENIED »
→ Le compte de service n'a pas accès au Sheet.
**Action** : Vérifiez que le Sheet est partagé avec `to-05-649@unique-hour-385920.iam.gserviceaccount.com` en tant qu'**Éditeur**.

### Erreur : « This operation is not supported for this document »
→ Le Sheet n'est pas un Google Sheets natif (c'est un `.xlsx` importé).
**Action** : Refaites la conversion (Fichier → Enregistrer en tant que Google Sheets).

---

## 💾 Comment ça marche en pratique

### Changer une catégorie dans l'app
1. Ouvrez l'app
2. Allez sur une page (ex: "Vols / Cambriolages")
3. Descendez jusqu'au tableau
4. Modifiez une valeur dans la colonne **Catégorie** via la liste déroulante
5. Le changement est **immédiatement sauvegardé** dans le Google Sheet
6. (Optionnel) Rechargez l'app ou cliquez le bouton 🔄 pour voir les données à jour

### Ajouter une ligne dans le Google Sheet
1. Ouvrez le Sheet (https://docs.google.com/spreadsheets/d/1a7HZ4sBpNm8XrNjN0zSc4smsmPqTEKderM0G80NTFr0/edit)
2. Ajoutez une ligne avec vos données
3. Dans l'app, cliquez **🔄 Recharger depuis Google Sheets** (barre latérale)
4. La nouvelle ligne apparaît avec la catégorisation automatique

---

## 🔐 Sécurité

⚠️ **Ne JAMAIS commiter `credentials.json`** (il contient une clé secrète).

Le fichier `.gitignore` l'exclut déjà. Vérifiez :

```bash
git status
```

Il ne devrait **pas** lister `credentials.json`.

---

## ✨ Récapitulatif

| Étape | Commande | Résultat |
|-------|----------|----------|
| 1️⃣ Installer | `pip install "gspread==5.12.4" "google-auth==2.35.0"` | Dépendances prêtes |
| 2️⃣ Partager | Ajouter `to-05-649@...` en Éditeur au Sheet | Accès confirmé |
| 3️⃣ Lancer | `streamlit run app.py` | App connectée au Sheet |

Une fois ces 3 étapes faites, **le système est opérationnel** : données synchronisées, modifications persistantes, ajout de lignes en temps réel.

---

**Questions ou erreurs ?** Décrivez ce que vous voyez dans la console (après `streamlit run app.py`) et je corrige ! 🚀
