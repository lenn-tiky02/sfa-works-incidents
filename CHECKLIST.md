# ✅ CHECKLIST - Analyseur d'Incidents SFA Works

## 📋 Avant de Commencer

- [ ] Python 3.8+ installé (`python --version`)
- [ ] Internet accessible (pour télécharger les dépendances)
- [ ] Dossier `D:\SFA Works\T-05` créé

---

## 🚀 Démarrage Rapide

### Option A: Lanceur Automatique (Recommandé)
- [ ] Allez dans `D:\SFA Works\T-05`
- [ ] Double-cliquez sur **`run.bat`**
- [ ] Attendez 30-60 secondes (première fois)
- [ ] Votre navigateur s'ouvre? ✅ **C'est bon!**
- [ ] Dashboard visible à http://localhost:8501? ✅ **Succès!**

### Option B: Installation Manuelle
- [ ] Ouvrir PowerShell/CMD
- [ ] Aller dans le dossier: `cd "D:\SFA Works\T-05"`
- [ ] Créer env virtuel: `python -m venv venv`
- [ ] Activer env: `.\venv\Scripts\activate` (PS) ou `venv\Scripts\activate.bat` (CMD)
- [ ] Installer dépendances: `pip install -r requirements.txt`
- [ ] Lancer app: `streamlit run app.py`
- [ ] Dashboard visible? ✅ **Succès!**

---

## 📊 Interface du Dashboard

### Navigation Principale
- [ ] Sidebar visible à gauche? ✅
- [ ] Boutons de sélection de pages? ✅
- [ ] Vous pouvez cliquer et changer de page? ✅

### Page 1: Vue Générale
- [ ] 8 cartes KPI affichées? ✅
- [ ] "Total Incidents: XXX"? ✅
- [ ] 3 graphiques: Pie, Bar, Line? ✅
- [ ] Légendes et axes visibles? ✅

### Page 2: Blessures Corporelles
- [ ] % cas avec blessure affiché? ✅
- [ ] Bar chart des types de blessures? ✅
- [ ] Top causes (6 items)? ✅
- [ ] Distribution gravité (pie chart)? ✅

### Page 3: Analyse des Vols
- [ ] KPI "Nombre Total de Vols"? ✅
- [ ] KPI "% Incidents = Vols"? ✅
- [ ] Bar chart objets volés? ✅
- [ ] Line chart vols par mois? ✅

### Page 4: Analyse Électrique
- [ ] KPI "Incidents Électriques"? ✅
- [ ] Bar chart causes principales? ✅
- [ ] Actions recommandées visibles? ✅
- [ ] Au moins 4 actions listées? ✅

### Page 5: Construction & Maintenance
- [ ] 3 KPIs: incidents, blessures, taux? ✅
- [ ] Bar chart top risques? ✅
- [ ] Pie chart lieux de chantier? ✅
- [ ] Avertissement sur risques? ✅

### Page 6: Prévention
- [ ] Tableau matrice de risque? ✅
- [ ] 6 lignes (risques)? ✅
- [ ] 4 indicateurs KPI? ✅
- [ ] Top 5 causes et lieux? ✅
- [ ] Indice risque par lieu (bar chart)? ✅

### Page 7: Upload Données
- [ ] Structure attendue listée? ✅
- [ ] Bouton "Browse files"? ✅
- [ ] Texte informatif? ✅

---

## 🎨 Vérifications Visuelles

- [ ] Couleurs cohérentes (bleu/blanc/gris)? ✅
- [ ] Texte lisible? ✅
- [ ] Graphiques bien espacés? ✅
- [ ] Pas d'erreurs affichées? ✅
- [ ] Responsive (redimensionnez la fenêtre)? ✅

---

## ⚙️ Vérifications Techniques

### Fichiers Créés
- [ ] `app.py` existe? ✅
- [ ] `requirements.txt` existe? ✅
- [ ] `.streamlit/config.toml` existe? ✅
- [ ] `run.bat` existe? ✅
- [ ] `run.ps1` existe? ✅
- [ ] Documentation complète? ✅

### Dépendances Installées
- [ ] streamlit? `pip list | findstr streamlit`
- [ ] pandas? `pip list | findstr pandas`
- [ ] plotly? `pip list | findstr plotly`
- [ ] numpy? `pip list | findstr numpy`

### Environnement Virtuel
- [ ] Dossier `venv/` créé? ✅
- [ ] Dossier `venv/Scripts/` existe? ✅
- [ ] Fichier `venv/Scripts/activate.bat` existe? ✅

---

## 🧪 Tests Interactifs

### Interaction avec les Graphiques
- [ ] Cliquez sur un graphique → Zoom fonctionne? ✅
- [ ] Hovez sur les barres → Infobulles apparaissent? ✅
- [ ] Double-cliquez pour reset zoom? ✅
- [ ] Cliquez droit sur graphique → "Save image"? ✅

### Navigation
- [ ] Cliquez sur une autre page → Contenu change? ✅
- [ ] Retour première page → KPIs se rechargent? ✅
- [ ] Refresh page (F5) → Données de demo se régénèrent? ✅

### Sidebar
- [ ] Expand/Collapse sidebar (en haut à gauche)? ✅
- [ ] Message "Tip" visible? ✅
- [ ] Lien vers documentation? ✅

---

## 📁 Structure de Dossier

```
D:\SFA Works\T-05\
├── app.py                      ✅
├── requirements.txt            ✅
├── run.bat                     ✅
├── run.ps1                     ✅
├── test_setup.py               ✅
├── README.md                   ✅
├── QUICK_START.md              ✅
├── INSTALLATION.md             ✅
├── ARCHITECTURE.md             ✅
├── ROADMAP.md                  ✅
├── SUMMARY.md                  ✅
├── CHECKLIST.md                ✅ (ce fichier)
├── setup.bat                   ✅
├── setup.ps1                   ✅
├── .gitignore                  ✅
└── .streamlit/
    └── config.toml             ✅
```

- [ ] Tous ces fichiers sont présents? ✅

---

## 🚨 Troubleshooting

### L'app ne démarre pas
- [ ] Python 3.8+? `python --version`
- [ ] Dépendances installées? `pip list`
- [ ] Aucun message d'erreur? (Capturez-le)
- [ ] Port 8501 libre? `netstat -an | findstr 8501`

### Erreur "Module not found"
- [ ] Env virtuel activé? (Cherchez `(venv)` au début)
- [ ] Réinstallez: `pip install -r requirements.txt`

### Graphiques ne s'affichent pas
- [ ] Plotly installé? `pip list | findstr plotly`
- [ ] Navigateur moderne? (Chrome, Firefox, Edge)
- [ ] JavaScript activé?

### Données d'exemple ne se génèrent pas
- [ ] Pandas installé? `pip list | findstr pandas`
- [ ] Numpy installé? `pip list | findstr numpy`

---

## 📚 Documentation

- [ ] Avez-vous lu `QUICK_START.md`? ✅
- [ ] Avez-vous lu `README.md`? ✅
- [ ] Comprenez-vous l'architecture? (voir `ARCHITECTURE.md`) ✅
- [ ] Savez-vous ce qui vient après? (voir `ROADMAP.md`) ✅

---

## ✨ Fonctionnalités Testées

### Dashboard
- [ ] 7 pages de contenu? ✅
- [ ] 15+ graphiques interactifs? ✅
- [ ] 8 KPIs sur page 1? ✅
- [ ] Matrice de risque? ✅
- [ ] Données d'exemple cohérentes? ✅

### UI/UX
- [ ] Professionnel et moderne? ✅
- [ ] Facile à naviguer? ✅
- [ ] Responsive? ✅
- [ ] Pas d'erreurs visuelles? ✅

### Performance
- [ ] App se charge en < 5 secondes? ✅
- [ ] Changement page en < 1 seconde? ✅
- [ ] Graphiques fluides? ✅
- [ ] Aucun lag en interaction? ✅

---

## 🎯 Prêt pour la Phase 2?

Avant de continuer, confirmez:

- [ ] Dashboard fonctionne parfaitement? ✅
- [ ] Vous comprenez le code? (voir `app.py`)
- [ ] Vous avez votre fichier `TO-05.xlsx`? ✅
- [ ] Vous êtes prêt pour upload + IA? ✅

**Si tout est coché ✅, vous êtes prêt pour la phase 2!** 🚀

---

## 📞 Questions?

- ❓ Lire `QUICK_START.md` (2 min)
- ❓ Lire `INSTALLATION.md` (détaillé)
- ❓ Lire `ARCHITECTURE.md` (technique)
- ❓ Regarder les commentaires dans `app.py`

---

## 🎉 Résumé Final

- ✅ **Dashboard créé** avec 7 pages
- ✅ **Interface moderne** et interactive
- ✅ **Graphiques professionnels** (Plotly)
- ✅ **Données d'exemple** pour tester
- ✅ **Documentation complète** (5 fichiers MD)
- ✅ **Prêt pour production** (à déployer)

### Prochaines étapes:
1. Upload votre fichier Excel
2. Configurer l'IA (phase 2)
3. Connecter la BDD (phase 3)
4. Déployer sur Streamlit Cloud (phase 5)

**Bon développement!** 💪
