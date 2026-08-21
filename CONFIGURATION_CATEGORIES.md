# 🔧 CONFIGURATION - MOTS-CLÉS DE CATÉGORISATION

## ⚠️ PROBLÈME DÉTECTÉ

Seules "Vue Générale" et "Autres" s'affichent → Les mots-clés ne correspondent pas aux données réelles!

## 🔍 DIAGNOSTIC

**Étapes pour vérifier:**

1. **Lancer l'app et chercher l'expander:**
   - Chercher "🔍 Aperçu Catégorisation"
   - Cliquer pour développer
   - Voir la distribution des catégories

2. **Vérifier les premières lignes:**
   - Voir quels incidents reçoivent quelle catégorie
   - Vérifier si beaucoup vont dans "Autres"

3. **Examiner le fichier Excel:**
   - Ouvrir `TO-05.xlsx`
   - Voir quels mots réels contiennent les données
   - Noter les termes utilisés

## 🔧 COMMENT MODIFIER LES MOTS-CLÉS

**Localisation dans le code (app.py, ligne ~20):**

```python
def categorize_incident(row_data):
    # ...
    if any(word in text for word in ['vol', 'cambriolage', ...]):
        return 'Vols / Cambriolages'
    elif any(word in text for word in ['sono', 'projecteur', ...]):
        return 'Dommages Matériels'
    # etc.
```

**Exemple de modification:**

**AVANT (mots-clés incorrects):**
```python
elif any(word in text for word in ['sono', 'projecteur']):
    return 'Dommages Matériels'
```

**APRÈS (mots-clés corrects):**
```python
elif any(word in text for word in ['sono', 'projecteur', 'vol_sono', 'dommage_équipement']):
    return 'Dommages Matériels'
```

## 📝 ÉTAPES COMPLÈTES

### 1. **Vérifier les données réelles**

Ouvrir le fichier Excel et noter les termes utilisés:
- Pour les **vols**: Qu'écrit-on? "Vol de...", "Cambriolage", "Volé"?
- Pour les **dommages**: "Sono cassée", "Projecteur endommagé", "Équipement dégradé"?
- Pour les **blessures**: "Blessure", "Accident", "Chute", "Traumatisme"?
- Pour l'**électrique**: "Surtension", "Foudre", "Court-circuit", "Problème électrique"?
- Pour la **construction**: "Chantier", "Travaux", "Maintenance", "Échafaudage"?

### 2. **Mettre à jour app.py**

Ouvrir `app.py` et modifier les mots-clés (lignes ~20-40):

```python
def categorize_incident(row_data):
    """Catégoriser automatiquement chaque incident"""
    if isinstance(row_data, pd.Series):
        text = ' '.join(row_data.dropna().astype(str)).lower()
    else:
        text = str(row_data).lower()
    
    # VOLS
    if any(word in text for word in ['YOUR_KEYWORDS_HERE']):
        return 'Vols / Cambriolages'
    
    # DOMMAGES
    elif any(word in text for word in ['YOUR_KEYWORDS_HERE']):
        return 'Dommages Matériels'
    
    # BLESSURES
    elif any(word in text for word in ['YOUR_KEYWORDS_HERE']):
        return 'Blessures Corporelles'
    
    # ÉLECTRIQUE
    elif any(word in text for word in ['YOUR_KEYWORDS_HERE']):
        return 'Risques Électriques'
    
    # CONSTRUCTION
    elif any(word in text for word in ['YOUR_KEYWORDS_HERE']):
        return 'Risques Construction'
    
    else:
        return 'Autres'
```

### 3. **Relancer l'app**

```bash
Double-cliquez: clean_and_restart.bat
```

### 4. **Vérifier la catégorisation**

- Chercher l'expander "🔍 Aperçu Catégorisation"
- Vérifier que toutes les catégories apparaissent
- Vérifier que peu d'incidents vont dans "Autres"

## 📋 EXEMPLE DE MOTS-CLÉS

Si vos données contiennent:
- "Vol de projecteur", "Cambriolage magasin", "Volé équipement"
  → Ajouter: `['vol', 'cambriolage', 'volé']`

- "Sono endommagée", "Projecteur cassé", "Ampli dégradé"
  → Ajouter: `['endommagé', 'cassé', 'dégradé', 'sono', 'projecteur', 'ampli']`

- "Accident chute", "Blessure construction", "Fracture"
  → Ajouter: `['accident', 'chute', 'blessure', 'fracture', 'plaie']`

- "Surtension électrique", "Coup de foudre", "Panne courant"
  → Ajouter: `['surtension', 'foudre', 'panne', 'courant', 'électrique']`

- "Travaux chantier", "Maintenance structure", "Échafaudage effondré"
  → Ajouter: `['travaux', 'chantier', 'maintenance', 'échafaudage', 'construction']`

## ✅ CHECKLIST

- [ ] Ouvrir TO-05.xlsx et noter les termes réels
- [ ] Modifier app.py avec les bons mots-clés
- [ ] Relancer l'app
- [ ] Vérifier que toutes les catégories apparaissent
- [ ] Vérifier que peu vont dans "Autres"

## 🆘 SI TOUJOURS PROBLÈME

1. **Vérifier la casse (majuscules/minuscules)**
   - Les mots-clés sont convertis en minuscules
   - Utiliser toujours des minuscules

2. **Vérifier les espaces**
   - "court-circuit" vs "court circuit"
   - Essayer les deux variantes

3. **Vérifier les accents**
   - "électrique" vs "electrique"
   - Essayer les deux

4. **Déboguer**
   - Lancer `debug_categories.py` pour voir les données réelles
   - Copier-coller des termes dans les mots-clés

**Besoin d'aide? Consultez les données dans TO-05.xlsx!**
