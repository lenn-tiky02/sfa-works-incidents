#!/usr/bin/env python3
"""
Script de debug pour vérifier les données et les stats
"""
import pandas as pd
import os

# Chemin du fichier Excel
excel_path = r"c:\Users\ANDRIANAIVOSOA Tsiky\Downloads\TO-05.xlsx"

if not os.path.exists(excel_path):
    print(f"❌ Fichier non trouvé: {excel_path}")
    exit(1)

print("=" * 80)
print("ANALYSE DES DONNÉES EXCEL")
print("=" * 80)

# Charger les données
try:
    df = pd.read_excel(excel_path)
    print(f"✅ Fichier chargé avec succès")
    print(f"   • Nombre de lignes: {len(df)}")
    print(f"   • Nombre de colonnes: {len(df.columns)}")
except Exception as e:
    print(f"❌ Erreur lors du chargement: {e}")
    exit(1)

# Normaliser les colonnes
df.columns = df.columns.str.strip()

print("\n" + "=" * 80)
print("COLONNES DISPONIBLES")
print("=" * 80)
for i, col in enumerate(df.columns, 1):
    print(f"{i}. {col}")

print("\n" + "=" * 80)
print("APERÇU DES DONNÉES (5 premières lignes)")
print("=" * 80)
print(df.head())

print("\n" + "=" * 80)
print("TYPES DE DONNÉES")
print("=" * 80)
print(df.dtypes)

print("\n" + "=" * 80)
print("ANALYSE DES COLONNES DATE/HEURE")
print("=" * 80)

# Chercher les colonnes date/heure
date_columns = [col for col in df.columns if any(x in col.lower() for x in ['date', 'time', 'heure', 'jour'])]
print(f"Colonnes potentielles de date/heure: {date_columns}")

if date_columns:
    date_col = date_columns[0]
    print(f"\nAnalyse de la colonne: {date_col}")
    print(f"Type: {df[date_col].dtype}")
    print(f"Exemples:")
    for i, val in enumerate(df[date_col].head(10)):
        print(f"  {i+1}. {val} (type: {type(val).__name__})")
    
    # Essayer de convertir en datetime
    print(f"\nConversion en datetime:")
    try:
        dates_converted = pd.to_datetime(df[date_col], errors='coerce')
        valid_dates = dates_converted.notna().sum()
        invalid_dates = dates_converted.isna().sum()
        print(f"  ✅ {valid_dates} dates valides")
        print(f"  ❌ {invalid_dates} dates invalides")
        
        if valid_dates > 0:
            print(f"\nHeures trouvées:")
            hours = dates_converted.dt.hour.value_counts().sort_index()
            for hour, count in hours.items():
                if pd.notna(hour):
                    print(f"  {int(hour)}h-{int(hour)+1}h: {count} incidents")
    except Exception as e:
        print(f"  ❌ Erreur: {e}")

print("\n" + "=" * 80)
print("ANALYSE DES COLONNES DÉPARTEMENT")
print("=" * 80)

# Chercher les colonnes département
dept_columns = [col for col in df.columns if any(x in col.lower() for x in ['dept', 'region', 'zone', 'site', 'location'])]
print(f"Colonnes potentielles de département: {dept_columns}")

if dept_columns:
    dept_col = dept_columns[0]
    print(f"\nAnalyse de la colonne: {dept_col}")
    print(f"Valeurs uniques: {df[dept_col].nunique()}")
    print(f"\nTop 10 départements:")
    dept_counts = df[dept_col].value_counts().head(10)
    for dept, count in dept_counts.items():
        pct = (count / len(df) * 100)
        print(f"  {dept}: {count} ({pct:.1f}%)")

print("\n" + "=" * 80)
print("ANALYSE DES CATÉGORIES")
print("=" * 80)

# Fonction de catégorisation
def categorize_incident(row_data):
    if isinstance(row_data, pd.Series):
        text = ' '.join(row_data.dropna().astype(str)).lower()
    else:
        text = str(row_data).lower()
    
    if any(word in text for word in ['vol', 'cambriolage', 'volé', 'cambriolé', 'voler', 'cambrioler']):
        return 'Vols / Cambriolages'
    elif any(word in text for word in ['sono', 'projecteur', 'ordinateur', 'ampli', 'amplificateur', 'dommage', 'matériel', 'équipement', 'cassé', 'cassée', 'détérioré']):
        return 'Dommages Matériels'
    elif any(word in text for word in ['blessure', 'blessé', 'blessée', 'chute', 'écrasé', 'écrasée', 'coupure', 'fracture', 'morsure', 'accident', 'plaie', 'traumatisme']):
        return 'Blessures Corporelles'
    elif any(word in text for word in ['électrique', 'électricité', 'surtension', 'foudre', 'court-circuit', 'tension', 'courant', 'électrocution', 'jirama', 'coupure']):
        return 'Risques Électriques'
    elif any(word in text for word in ['construction', 'maintenance', 'chantier', 'échafaudage', 'outils', 'marteau', 'travaux', 'bâtiment', 'structure', 'toiture']):
        return 'Risques Construction'
    else:
        return 'Autres'

df['Catégorie'] = df.apply(categorize_incident, axis=1)

print("\nDistribution des catégories:")
cat_counts = df['Catégorie'].value_counts()
for cat, count in cat_counts.items():
    pct = (count / len(df) * 100)
    print(f"  {cat}: {count} ({pct:.1f}%)")

print("\n" + "=" * 80)
print("ANALYSE PAR CATÉGORIE")
print("=" * 80)

for cat in sorted(df['Catégorie'].unique()):
    df_cat = df[df['Catégorie'] == cat]
    print(f"\n{cat}")
    print(f"  Total: {len(df_cat)}")
    
    if dept_col:
        dept_top = df_cat[dept_col].value_counts().head(3)
        print(f"  Top 3 Département:")
        for dept, count in dept_top.items():
            pct = (count / len(df_cat) * 100)
            print(f"    • {dept}: {count} ({pct:.1f}%)")

print("\n" + "=" * 80)
print("✅ ANALYSE COMPLÈTE")
print("=" * 80)
