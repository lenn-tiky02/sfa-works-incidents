# 📊 Analyseur d'Incidents - SFA Works

Application de dashboard d'analyse des incidents et des risques pour SFA Works.

## 🎯 Fonctionnalités

### Pages Disponibles

1. **Vue Générale** - Vue d'ensemble de tous les incidents avec KPIs principaux
2. **Blessures Corporelles** - Analyse détaillée des blessures et leurs causes
3. **Analyse des Vols** - Tendances et objets volés les plus fréquents
4. **Analyse Électrique** - Incidents électriques et recommandations
5. **Construction & Maintenance** - Risques spécifiques au chantier
6. **Prévention** - Matrice de risque et indicateurs clés
7. **Upload Données** - Interface pour charger vos données Excel

## 🚀 Démarrage Rapide

### Prérequis
- Python 3.8 ou supérieur
- pip (gestionnaire de paquets Python)

### Installation

1. **Cloner ou créer le projet**
```bash
cd "D:\SFA Works\T-05"
```

2. **Créer un environnement virtuel**
```bash
python -m venv venv
venv\Scripts\activate
```

3. **Installer les dépendances**
```bash
pip install -r requirements.txt
```

4. **Lancer l'application**
```bash
streamlit run app.py
```

L'application s'ouvrira automatiquement dans votre navigateur à `http://localhost:8501`

## 📊 Structure du Projet

```
T-05/
├── app.py                 # Application principale
├── requirements.txt       # Dépendances Python
├── README.md             # Documentation
├── .gitignore            # Fichiers à ignorer
└── .streamlit/
    └── config.toml       # Configuration Streamlit
```

## 📋 Catégories d'Incidents

- 🩹 **Blessure** - Incidents ayant causé une blessure
- 🔓 **Vol** - Vols d'équipements ou d'objets
- 💔 **Dommage matériel** - Dommages à la propriété
- ⚠️ **Quasi-accident** - Incidents sans conséquence mais potentiellement dangereux
- ⚡ **Électrique** - Incidents liés aux problèmes électriques
- 🚗 **Véhicule** - Accidents de véhicules
- 🏗️ **Construction** - Incidents de chantier
- 🌩️ **Catastrophe naturelle** - Foudre, intempéries, etc.

## 🤖 Catégorisation IA

La future version intégrera:
- Classification automatique des incidents
- Extraction de causes depuis le texte libre
- Détection de patterns de risque
- Recommandations automatiques

## 💾 Base de Données

Configuration à venir - supporte:
- PostgreSQL
- SQLite
- Firebase Firestore

## 📝 Format des Données

Votre fichier Excel doit contenir ces colonnes:
| Colonne | Type | Exemple |
|---------|------|---------|
| Date | Date | 2024-01-15 |
| Type | Texte | Blessure |
| Cause | Texte | Chute |
| Gravité | Texte | Grave |
| Lieu | Texte | Atelier |
| Blessure | Texte | Coupure |
| Vol | Texte | Projecteur |
| Année | Nombre | 2024 |
| Mois | Nombre | 1 |

## 🔒 Sécurité

- Les données d'exemple sont fictives
- Aucune donnée sensible stockée en clair
- Secrets à configurer dans `.streamlit/secrets.toml`

## 📞 Support

Pour toute question ou amélioration, contactez l'équipe SFA Works.

## 📄 Licence

Projet interne SFA Works © 2024
