# 🏗️ Architecture du Système

## 📐 Vue d'Ensemble

```
┌─────────────────────────────────────────────────────────────┐
│                    UTILISATEUR FINAL                         │
│            (Navigateur Web - Chrome, Firefox, etc)           │
└──────────────────────────┬──────────────────────────────────┘
                           │
                  ┌────────▼────────┐
                  │  Streamlit App  │
                  │   (Frontend)    │
                  │  app.py (1 page)│
                  └────────┬────────┘
                           │
        ┌──────────────────┼──────────────────┐
        │                  │                  │
        ▼                  ▼                  ▼
  ┌─────────────┐  ┌──────────────┐  ┌─────────────┐
  │  Données    │  │ Traitement   │  │ Visualisas. │
  │  d'Exemple  │  │  (Pandas)    │  │  (Plotly)   │
  │  (En RAM)   │  │              │  │             │
  └─────────────┘  └──────────────┘  └─────────────┘
```

---

## 📂 Arborescence des Fichiers

```
T-05/                                   # Racine du projet
│
├── app.py                              # 🎯 Application Streamlit principale
│                                       #    - 6 pages de dashboard
│                                       #    - 400+ lignes de code
│                                       #    - Données en RAM (démo)
│
├── requirements.txt                    # 📦 Dépendances Python
│                                       #    - streamlit, pandas, plotly
│                                       #    - numpy, openpyxl
│
├── .streamlit/                         # ⚙️ Configuration Streamlit
│   └── config.toml                     #    - Thème et couleurs
│                                       #    - Paramètres serveur
│
├── .gitignore                          # 🔒 Fichiers ignorés Git
│                                       #    - venv/, *.pyc, *.db
│
├── run.bat                             # 🚀 Lancement Windows (Batch)
├── run.ps1                             # 🚀 Lancement Windows (PowerShell)
├── setup.bat                           # ⚙️ Installation Windows
├── setup.ps1                           # ⚙️ Installation PowerShell
│
├── README.md                           # 📖 Documentation générale
├── QUICK_START.md                      # ⚡ Démarrage rapide (2min)
├── INSTALLATION.md                     # 🔧 Guide installation détaillé
├── ARCHITECTURE.md                     # 🏗️ Ce fichier
├── ROADMAP.md                          # 🛣️ Fonctionnalités futures
│
└── venv/                               # 🐍 Environnement virtuel
    ├── Scripts/                        #    (créé après setup)
    │   ├── python.exe
    │   ├── pip.exe
    │   └── streamlit.exe
    └── Lib/                            #    Dépendances installées
```

---

## 🔄 Flux de Données

### Actuellement (Phase 1 - Démo)

```
┌─────────────────────────────────────┐
│  1. Démarrage de l'Application      │
│     streamlit run app.py            │
└──────────────┬──────────────────────┘
               │
┌──────────────▼──────────────────────┐
│  2. Génération de Données d'Exemple │
│     load_sample_data()              │
│     → 100 incidents fictifs         │
│     → Avec types, causes, gravités  │
└──────────────┬──────────────────────┘
               │
┌──────────────▼──────────────────────┐
│  3. Affichage du Dashboard          │
│     - Navigation en sidebar         │
│     - 6 pages différentes           │
│     - Graphiques interactifs        │
└──────────────┬──────────────────────┘
               │
┌──────────────▼──────────────────────┐
│  4. Interaction Utilisateur         │
│     - Clic sur page                 │
│     - Refresh automatique (F5)      │
└─────────────────────────────────────┘
```

### À Venir (Phase 2-4)

```
┌────────────────────────────────────────┐
│  1. Upload Fichier Excel               │
│     Utilisateur sélectionne TO-05.xlsx │
└──────────────┬─────────────────────────┘
               │
┌──────────────▼─────────────────────────┐
│  2. Validation & Chargement (Pandas)   │
│     - Lecture fichier                  │
│     - Vérification colonnes            │
│     - Détection erreurs               │
└──────────────┬─────────────────────────┘
               │
┌──────────────▼─────────────────────────┐
│  3. Catégorisation IA                  │
│     Hugging Face Inference API         │
│     - Type d'incident                 │
│     - Cause probable                  │
│     - Niveau de gravité               │
└──────────────┬─────────────────────────┘
               │
┌──────────────▼─────────────────────────┐
│  4. Sauvegarde en BDD                  │
│     PostgreSQL (Render.com)            │
│     - Table incidents                 │
│     - Table stats_cache               │
└──────────────┬─────────────────────────┘
               │
┌──────────────▼─────────────────────────┐
│  5. Affichage & Statistiques           │
│     - Dashboard mis à jour             │
│     - KPIs recalculés                 │
│     - Graphiques refreshés             │
└────────────────────────────────────────┘
```

---

## 🎨 Composants de l'Application

### Page 1: Vue Générale
```python
# app.py, lignes 62-115
- 8 KPIs en cartes
- 3 graphiques interactifs
- Évolution temporelle
```

### Page 2: Blessures Corporelles
```python
# app.py, lignes 117-165
- % cas avec blessure
- Top types de blessures
- Top causes (6 principales)
- Distribution par gravité
```

### Page 3: Analyse des Vols
```python
# app.py, lignes 167-208
- Nombre total de vols
- % incidents = vols
- Objets les plus volés (bar chart)
- Vols par année, mois, région
```

### Page 4: Analyse Électrique
```python
# app.py, lignes 210-249
- Nombre incidents électriques
- Causes principales (heatmap)
- Gravité distribution
- 4 actions recommandées
```

### Page 5: Construction & Maintenance
```python
# app.py, lignes 251-289
- Incidents construction
- Blessures chantier
- Top risques
- Lieux de chantier
```

### Page 6: Prévention
```python
# app.py, lignes 291-357
- Matrice de risque (6 risques)
- 4 KPIs clés de suivi
- Top 5 causes & lieux
- Indice de risque par lieu
```

### Page 7: Upload Données
```python
# app.py, lignes 359-395
- Info sur structure attendue
- Instructions upload
- File uploader component
```

---

## 🎨 Palette de Couleurs

```python
# Thème principal (config.toml)
primaryColor    = "#1f77b4"        # Bleu
backgroundColor = "#ffffff"        # Blanc
secondaryBg     = "#f0f2f6"        # Gris clair
textColor       = "#262730"        # Gris foncé

# Couleurs aux graphiques
KPI Graves      = "#8B0000"        # Bordeaux
KPI Graves-Mod  = "#FF6347"        # Tomato
KPI Modérées    = "#FFD700"        # Or
KPI Légères     = "#90EE90"        # Vert clair
```

---

## 📊 Dépendances

### Core (Obligatoire)
```
streamlit>=1.28.0      # Framework web
pandas>=2.0.0          # Manipulation données
numpy>=1.24.0          # Calculs numériques
plotly>=5.15.0         # Graphiques interactifs
openpyxl>=3.10.0       # Lecture Excel
```

### À Ajouter Ultérieurement
```
psycopg2-binary        # PostgreSQL driver
python-dotenv          # Variables d'environnement
transformers           # IA/NLP
huggingface-hub        # API Hugging Face
streamlit-authenticator # Auth/Login
reportlab              # Génération PDF
schedule               # Planification tâches
```

---

## 🔐 Sécurité

### Actuellement
- ✅ Aucune donnée sensible (démo)
- ✅ Pas d'authentification (dev)
- ⚠️ Pas de chiffrement
- ⚠️ Pas de logs d'audit

### À Implémenter
- [ ] Authentification utilisateur
- [ ] Chiffrement des données
- [ ] HTTPS obligatoire (déploiement)
- [ ] Logs d'audit
- [ ] Validation entrées utilisateur
- [ ] Rate limiting API

---

## 📈 Performance

### Optimisations Actuelles
- ✅ Données chargées en RAM (rapide)
- ✅ Graphiques Plotly (interactif, HTML)
- ✅ Caching Streamlit natif
- ✅ Pas de requêtes BDD

### Goulots d'Étranglement Potentiels
- ⚠️ Sans BDD: limitations RAM (1000s rows)
- ⚠️ IA synchrone: 1-2sec par ligne (lent)
- ⚠️ Pas de pagination (limite 10k lignes)

### Optimisations Prévues
- [ ] PostgreSQL avec indexing
- [ ] Caching des stats
- [ ] IA asynchrone (workers)
- [ ] Pagination & lazy loading
- [ ] Compression des données

---

## 🚀 Déploiement Simplifié

### Streamlit Cloud (Recommandé)

```
1. Créer repo GitHub (public ou privé)
   → Push code + requirements.txt

2. Aller sur streamlit.io/cloud
   → Cliquer "New app"
   → Sélectionner repo

3. Configuré automatiquement:
   → URL: xxx.streamlit.app
   → SSL/HTTPS: ✅ Gratuit
   → Auto-redeploy sur git push
```

### Architecture Finale (Production)

```
                Internet Public
                      │
         ┌────────────▼────────────┐
         │  Streamlit Cloud CDN    │
         │   (App served)          │
         └────────────┬────────────┘
                      │
        ┌─────────────┴─────────────┐
        │                           │
    ┌───▼────┐              ┌───────▼──┐
    │ Render │              │ Hugging  │
    │Database│              │ Face API │
    │(Postgr.)              │(IA)      │
    └────────┘              └──────────┘
```

---

## 🧪 Tests & Validation

### Actuellement
- ✅ Données de démo chargent
- ✅ Tous les graphiques s'affichent
- ✅ Navigation multi-pages OK
- ⚠️ Pas de tests unitaires

### À Ajouter
- [ ] Tests unitaires (pytest)
- [ ] Tests d'intégration
- [ ] Tests de performance
- [ ] Tests UI (Selenium)

---

## 📚 Ressources & Documentation

**Dans le Projet:**
- `app.py` - Code source entièrement commenté
- `QUICK_START.md` - 2 minutes pour démarrer
- `INSTALLATION.md` - Guide détaillé
- `ROADMAP.md` - Fonctionnalités à venir

**Externes:**
- [Streamlit Docs](https://docs.streamlit.io)
- [Plotly Docs](https://plotly.com/python/)
- [Pandas Docs](https://pandas.pydata.org/docs/)
- [HuggingFace Docs](https://huggingface.co/docs)

---

## ⚡ TL;DR (Résumé Technique)

| Aspect | Détails |
|--------|---------|
| **Type** | Dashboard Web (SPA) |
| **Framework** | Streamlit (Python) |
| **Frontend** | HTML/CSS/JS (généré) |
| **Backend** | Python 3.12+ |
| **BDD** | À configurer (Postgres) |
| **IA** | Hugging Face (gratuit) |
| **Déploiement** | Streamlit Cloud |
| **Coût** | Gratuit (même en production) |
| **Temps Setup** | 5-10 minutes |

---

**Architecture simple, efficace, et gratuite!** 🚀
