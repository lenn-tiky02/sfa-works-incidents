import pandas as pd

# Charger le fichier
try:
    df = pd.read_excel(r'c:\Users\ANDRIANAIVOSOA Tsiky\Downloads\TO-05.xlsx')
    print("✅ Fichier chargé avec succès!")
    print(f"\n📊 Dimensions: {df.shape[0]} lignes, {df.shape[1]} colonnes")
    print(f"\n📋 Colonnes: {df.columns.tolist()}")
    print(f"\n🔍 Premières lignes:")
    print(df.head())
    print(f"\n📈 Types de données:")
    print(df.dtypes)
    print(f"\n✨ Résumé:")
    print(df.info())
except Exception as e:
    print(f"❌ Erreur: {e}")
