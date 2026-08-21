import pandas as pd

# Charger le fichier
try:
    excel_path = r'c:\Users\ANDRIANAIVOSOA Tsiky\Downloads\TO-05.xlsx'
    df = pd.read_excel(excel_path)
    
    print("✅ Fichier chargé!")
    print(f"\n📊 Dimensions: {df.shape[0]} lignes, {df.shape[1]} colonnes")
    print(f"\n📋 Colonnes: {df.columns.tolist()}")
    
    print(f"\n🔍 Premières lignes:")
    print(df.head())
    
    # Afficher le contenu pour analyse
    print(f"\n📝 Contenu pour catégorisation (premiers 20 lignes):")
    for idx, row in df.head(20).iterrows():
        print(f"\nLigne {idx+1}:")
        for col, val in row.items():
            if pd.notna(val):
                print(f"  {col}: {val}")
    
except Exception as e:
    print(f"❌ Erreur: {e}")
