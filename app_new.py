import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np

st.set_page_config(
    page_title="Analyseur d'Incidents - SFA Works",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
    <style>
    .main-header { font-size: 2.5em; color: #1f77b4; margin-bottom: 30px; }
    </style>
""", unsafe_allow_html=True)

def load_excel_data():
    """Charger les données du fichier Excel TO-05.xlsx"""
    try:
        excel_path = r'c:\Users\ANDRIANAIVOSOA Tsiky\Downloads\TO-05.xlsx'
        df = pd.read_excel(excel_path)
        st.success(f"✅ {len(df)} incidents chargés depuis TO-05.xlsx")
        return df
    except Exception as e:
        st.warning(f"⚠️ Impossible de charger le fichier Excel: {e}")
        return None

# Charger les données
df = load_excel_data()

# Fallback: données d'exemple si le fichier n'existe pas
if df is None or df.empty:
    st.info("📊 Utilisation des données d'exemple")
    data = {
        'Date': pd.date_range('2023-01-01', periods=100, freq='D'),
        'Type': np.random.choice(['Blessure', 'Vol', 'Dommage matériel', 'Quasi-accident', 
                                   'Électrique', 'Véhicule', 'Construction', 'Catastrophe naturelle'], 100),
        'Cause': np.random.choice(['Chute', 'Vol projecteur', 'Foudre', 'Travail construction', 
                                    'Manipulation matériaux', 'Escaliers', 'Surtension', 'Morsure chien'], 100),
        'Gravité': np.random.choice(['Légère', 'Modérée', 'Grave', 'Très grave'], 100),
        'Lieu': np.random.choice(['Atelier', 'Chantier', 'Bureau', 'Entrepôt', 'Toiture', 'Zone technique'], 100),
        'Département': np.random.choice(['Nord', 'Sud', 'Est', 'Ouest', 'Centre'], 100),
    }
    df = pd.DataFrame(data)

# Normaliser les noms de colonnes
df.columns = df.columns.str.strip()

# Navigation et filtres dans la sidebar
with st.sidebar:
    st.title("📊 Navigation")
    page = st.radio("Sélectionnez une page", 
                    ["Vue Générale", "Blessures Corporelles", "Analyse des Vols", 
                     "Analyse Électrique", "Construction & Maintenance", "Prévention"])
    
    st.divider()
    st.subheader("🔍 Filtres")
    
    # Filtre par département
    dept_col = None
    for col in df.columns:
        if 'département' in col.lower() or 'region' in col.lower():
            dept_col = col
            break
    
    if dept_col:
        departements = ['Tous'] + sorted([str(x) for x in df[dept_col].unique() if pd.notna(x)])
        selected_dept = st.selectbox("Département/Région", departements, key="dept_filter")
        
        if selected_dept != 'Tous':
            df_filtered = df[df[dept_col] == selected_dept].reset_index(drop=True)
        else:
            df_filtered = df.copy()
    else:
        st.info("⚠️ Aucune colonne 'Département' trouvée")
        df_filtered = df.copy()
    
    st.divider()
    st.info(f"📊 **{len(df_filtered)} incidents** affichés\n({len(df)} au total)")

# Vérifier qu'on a des données
if df_filtered.empty:
    st.warning("⚠️ Aucune donnée pour ce département")
else:
    # PAGE 1: VUE GÉNÉRALE
    if page == "Vue Générale":
        st.markdown('<h1 class="main-header">📈 Vue Générale des Incidents</h1>', unsafe_allow_html=True)
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("📋 Total Incidents", len(df_filtered))
        with col2:
            blessures_pct = (df_filtered['Type'] == 'Blessure').sum() / len(df_filtered) * 100
            st.metric("🩹 Blessures", f"{blessures_pct:.1f}%")
        with col3:
            vols_pct = (df_filtered['Type'] == 'Vol').sum() / len(df_filtered) * 100
            st.metric("🔓 Vols", f"{vols_pct:.1f}%")
        
        st.divider()
        
        col_left, col_right = st.columns(2)
        with col_left:
            st.subheader("Distribution des Types")
            try:
                type_counts = df_filtered['Type'].value_counts()
                fig = px.pie(values=type_counts.values, names=type_counts.index)
                st.plotly_chart(fig, use_container_width=True)
            except:
                st.info("Pas assez de données pour créer le graphique")
        
        with col_right:
            st.subheader("Incidents par Gravité")
            try:
                gravite_counts = df_filtered['Gravité'].value_counts()
                fig = px.bar(x=gravite_counts.index, y=gravite_counts.values)
                st.plotly_chart(fig, use_container_width=True)
            except:
                st.info("Colonne 'Gravité' non trouvée")
    
    # PAGE 2: BLESSURES
    elif page == "Blessures Corporelles":
        st.markdown('<h1 class="main-header">🩹 Analyse des Blessures Corporelles</h1>', unsafe_allow_html=True)
        
        blessures_df = df_filtered[df_filtered['Type'] == 'Blessure']
        blessures_pct = len(blessures_df) / len(df_filtered) * 100
        
        st.metric("📊 % Cas avec Blessure", f"{blessures_pct:.1f}%")
        
        if not blessures_df.empty:
            st.subheader("Analyse des Blessures")
            st.dataframe(blessures_df, use_container_width=True)
        else:
            st.info("Aucune blessure enregistrée pour ce département")
    
    # PAGE 3: VOLS
    elif page == "Analyse des Vols":
        st.markdown('<h1 class="main-header">🔓 Analyse des Vols</h1>', unsafe_allow_html=True)
        
        vols_df = df_filtered[df_filtered['Type'] == 'Vol']
        vols_count = len(vols_df)
        vols_pct = vols_count / len(df_filtered) * 100
        
        col1, col2 = st.columns(2)
        with col1:
            st.metric("🔓 Nombre de Vols", vols_count)
        with col2:
            st.metric("📊 % Incidents = Vols", f"{vols_pct:.1f}%")
        
        if not vols_df.empty:
            st.subheader("Vols Enregistrés")
            st.dataframe(vols_df, use_container_width=True)
        else:
            st.info("Aucun vol enregistré pour ce département")
    
    # PAGE 4: ÉLECTRIQUE
    elif page == "Analyse Électrique":
        st.markdown('<h1 class="main-header">⚡ Incidents Électriques</h1>', unsafe_allow_html=True)
        
        elec_df = df_filtered[df_filtered['Type'] == 'Électrique']
        elec_count = len(elec_df)
        
        st.metric("⚡ Incidents Électriques", elec_count)
        
        if not elec_df.empty:
            st.subheader("Incidents Électriques Détaillés")
            st.dataframe(elec_df, use_container_width=True)
        else:
            st.info("Aucun incident électrique pour ce département")
    
    # PAGE 5: CONSTRUCTION
    elif page == "Construction & Maintenance":
        st.markdown('<h1 class="main-header">🏗️ Construction & Maintenance</h1>', unsafe_allow_html=True)
        
        const_df = df_filtered[df_filtered['Type'] == 'Construction']
        const_count = len(const_df)
        
        st.metric("🏗️ Incidents Construction", const_count)
        
        if not const_df.empty:
            st.subheader("Incidents de Construction")
            st.dataframe(const_df, use_container_width=True)
        else:
            st.info("Aucun incident de construction pour ce département")
    
    # PAGE 6: PRÉVENTION
    elif page == "Prévention":
        st.markdown('<h1 class="main-header">🎯 Stratégie de Prévention</h1>', unsafe_allow_html=True)
        
        st.subheader("📊 Résumé par Type d'Incident")
        
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            blessures = len(df_filtered[df_filtered['Type'] == 'Blessure'])
            st.metric("🩹 Blessures", blessures)
        with col2:
            vols = len(df_filtered[df_filtered['Type'] == 'Vol'])
            st.metric("🔓 Vols", vols)
        with col3:
            dommages = len(df_filtered[df_filtered['Type'] == 'Dommage matériel'])
            st.metric("💔 Dommages", dommages)
        with col4:
            quasi = len(df_filtered[df_filtered['Type'] == 'Quasi-accident'])
            st.metric("⚠️ Quasi-accidents", quasi)
        
        st.divider()
        
        st.subheader("📊 Données Complètes")
        st.dataframe(df_filtered, use_container_width=True)

st.divider()
st.markdown("""
    ---
    <div style="text-align: center; color: #888; font-size: 0.9em;">
    <p>SFA Works - Analyseur d'Incidents © 2024</p>
    <p>Données réelles du fichier TO-05.xlsx</p>
    </div>
""", unsafe_allow_html=True)
