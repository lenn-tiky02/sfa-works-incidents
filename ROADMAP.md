# 🛣️ Roadmap - Fonctionnalités à Venir

## 📅 Phase 1: Dashboard Basique ✅ (Actuellement)

### Statut: ✅ COMPLÉTÉ

- ✅ 6 pages de dashboard avec visualisations
- ✅ KPIs principaux
- ✅ Graphiques interactifs (Plotly)
- ✅ Données d'exemple pour la démo
- ✅ Interface utilisateur moderne et responsive

---

## 📅 Phase 2: Gestion des Données (À Faire)

### Upload de Fichiers Excel

**Fonctionnalités:**
- [ ] Upload fichiers Excel/CSV
- [ ] Validation des colonnes
- [ ] Prévisualisation des données
- [ ] Détection des erreurs/données manquantes
- [ ] Sauvegarde temporaire

**Fichiers à créer:**
```
data_processing.py  # Traitement Excel
```

---

## 📅 Phase 3: Catégorisation IA (À Faire)

### Classification Automatique

**Utiliser:** Hugging Face ou Transformers.js

**Catégories à détecter:**
```
1. Type d'incident (Blessure, Vol, Électrique, etc.)
2. Cause (Chute, Surcharge électrique, etc.)
3. Gravité (Légère, Modérée, Grave)
4. Lieu/Zone affectée
5. Type de blessure spécifique
```

**Code à développer:**
```python
# ai_categorization.py
from transformers import pipeline

classifier = pipeline("zero-shot-classification")

def categorize_incident(text):
    # Détecter le type
    # Détecter la cause
    # Estimer la gravité
    pass
```

**Coût:** ⭐ Gratuit (Hugging Face Inference API)

---

## 📅 Phase 4: Base de Données (À Faire)

### Choix de la BDD

**Option 1: SQLite (Gratuit, Local)**
```python
import sqlite3
conn = sqlite3.connect('incidents.db')
```
✅ Gratuit | ❌ Pas d'accès remote

**Option 2: PostgreSQL (Gratuit Cloud)**
```python
import psycopg2
conn = psycopg2.connect("postgresql://...")
```
✅ Gratuit Render.com | ✅ Professionnel

**Option 3: Firebase (Gratuit Cloud)**
```python
import firebase_admin
db = firestore.client()
```
✅ Gratuit 512MB | ✅ Facile

**Recommandation:** PostgreSQL + Render.com

### Schéma de Base de Données

```sql
CREATE TABLE incidents (
    id SERIAL PRIMARY KEY,
    date TIMESTAMP,
    type VARCHAR(50),
    cause VARCHAR(255),
    gravite VARCHAR(20),
    lieu VARCHAR(100),
    description TEXT,
    blessure VARCHAR(100),
    vol VARCHAR(100),
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE stats_cache (
    id SERIAL PRIMARY KEY,
    metric_key VARCHAR(50),
    value FLOAT,
    updated_at TIMESTAMP
);
```

**Fichiers à créer:**
```
database.py      # Connexion & requêtes
models.py        # ORM/Schémas
db_init.sql      # Initialisation
```

---

## 📅 Phase 5: Intégration Complète (À Faire)

### Authentification

- [ ] Système de login/auth
- [ ] Rôles et permissions (Viewer, Editor, Admin)
- [ ] Sessions utilisateur

**Outil:** Streamlit-authenticator

```python
import streamlit_authenticator as stauth

authenticator = stauth.Authenticate(...)
name, authentication_status, username = authenticator.login()
```

### Export & Rapports

- [ ] Export PDF des rapports
- [ ] Export Excel des données
- [ ] Email automatique de rapports
- [ ] Planification des rapports

**Bibliothèques:**
- `reportlab` - Export PDF
- `python-pptx` - PowerPoint
- `schedule` - Planification

### Alertes en Temps Réel

- [ ] Alerte quand un incident grave est entré
- [ ] Notification dashboard
- [ ] Email/SMS alerts (optionnel)

---

## 📅 Phase 6: Déploiement (À Faire)

### Options de Déploiement

**Option 1: Streamlit Cloud (Recommandé)**
```bash
# 1. Push sur GitHub
git push origin main

# 2. Sur streamlit.io/cloud, déployer
# 3. URL automatique: xxx.streamlit.app
```
✅ Gratuit | ✅ 1 clic | ✅ Auto-scaling

**Option 2: Vercel + FastAPI**
```bash
# Frontend sur Vercel (gratuit)
# Backend sur Render (gratuit)
```

**Option 3: Railway ou Fly.io**
```bash
railway up
# ou
flyctl deploy
```

**Processus:**
- [ ] Créer repo GitHub
- [ ] Configurer secrets (.env)
- [ ] Déployer automatiquement
- [ ] Domaine personnalisé (optionnel)

---

## 🎯 Priorités d'Implémentation

### Haute Priorité 🔴
1. **Upload Excel + Catégorisation IA** - Base du système
2. **Base de Données PostgreSQL** - Persistence
3. **Authentification** - Sécurité
4. **Déploiement Streamlit Cloud** - Accès public

### Moyenne Priorité 🟡
5. Export PDF
6. Alertes temps réel
7. Graphiques avancés (carte géographique)

### Basse Priorité 🟢
8. Email automatique
9. Mobile app
10. API REST publique

---

## 📊 Estimation de Temps

| Phase | Durée | Effort |
|-------|-------|--------|
| Dashboard | ✅ 2h | Fait |
| Upload + IA | 3-4h | Moyenne |
| BDD | 2-3h | Moyenne |
| Auth | 1-2h | Faible |
| Déploiement | 1h | Très faible |
| **TOTAL** | **10h** | - |

---

## 🔗 Ressources Utiles

### Documentation
- 📖 [Streamlit Docs](https://docs.streamlit.io)
- 🤖 [Hugging Face Transformers](https://huggingface.co/transformers/)
- 🗄️ [PostgreSQL + Render](https://render.com/docs/deploy-postgres)
- 🔐 [Streamlit-Authenticator](https://github.com/mkhorasani/Streamlit-Authenticator)

### Librairies Recommandées
```python
# Déjà installées:
streamlit, pandas, plotly, numpy

# À ajouter plus tard:
transformers          # IA
psycopg2             # PostgreSQL
python-dotenv        # Variables d'env
streamlit-authenticator # Auth
reportlab            # PDF
schedule             # Planification
```

### Commandes Utiles
```bash
# Ajouter une dépendance
pip install nom_package
pip freeze > requirements.txt

# Mettre à jour
pip install --upgrade -r requirements.txt

# Vérifier les packages
pip list
```

---

## ✨ Prochaine Étape Recommandée

**👉 Phase 2: Upload Excel + AI Categorization**

1. Créer `data_processing.py` pour traiter Excel
2. Ajouter l'upload dans `app.py`
3. Intégrer Hugging Face pour la catégorisation
4. Afficher les résultats et permettre les corrections

**Durée estimée:** 3-4 heures

---

## 📝 Notes

- Le dashboard actuel utilise des données d'exemple
- Aucune donnée n'est persistée (tout reset à chaque refresh)
- Les performances seront limitées sans BDD
- L'IA gratuite est lente (1-2 secondes par ligne)

---

**Prêt à continuer? Commençons par la Phase 2!** 🚀
