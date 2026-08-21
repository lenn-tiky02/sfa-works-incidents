import os
import json
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

def categorize_incident(row_data):
    """Catégoriser automatiquement chaque incident"""
    # Convertir toute la ligne en texte
    if isinstance(row_data, pd.Series):
        text = ' '.join(row_data.dropna().astype(str)).lower()
    else:
        text = str(row_data).lower()
    
    # Catégories avec détection stricte
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

ALL_CATEGORIES = [
    'Vols / Cambriolages',
    'Dommages Matériels',
    'Blessures Corporelles',
    'Risques Électriques',
    'Risques Construction',
    'Autres',
]

# ==========================================================================
#  BACKEND GOOGLE SHEETS
#  Le Google Sheet est la source de vérité: on lit les données au démarrage
#  et on réécrit la catégorie dès qu'elle est modifiée dans l'application.
# ==========================================================================
SHEET_ID = "1a7HZ4sBpNm8XrNjN0zSc4smsmPqTEKderM0G80NTFr0"
CREDENTIALS_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "credentials.json")
GS_SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive",
]

def get_service_account_email():
    """Récupérer l'email du compte de service (pour les messages d'aide)."""
    try:
        with open(CREDENTIALS_FILE, encoding="utf-8") as f:
            return json.load(f).get("client_email", "")
    except Exception:
        return ""

_SA_REQUIRED_FIELDS = {"type", "private_key", "client_email", "token_uri"}


def _looks_like_service_account(d):
    """Vrai si le dict ressemble à un compte de service Google."""
    try:
        return _SA_REQUIRED_FIELDS.issubset(set(d.keys()))
    except Exception:
        return False


def _coerce_to_creds_dict(value):
    """Convertir une valeur de secret (string JSON ou mapping) en dict de credentials."""
    import json as json_lib
    if value is None:
        return None
    if isinstance(value, str):
        try:
            return json_lib.loads(value)
        except Exception:
            return None
    try:
        return dict(value)
    except Exception:
        return None


def find_service_account_dict():
    """Détecter automatiquement les credentials du compte de service.

    Recherche, dans l'ordre :
      1. le fichier credentials.json en local ;
      2. une clé de secret nommée explicitement (GOOGLE_CREDENTIALS / google_credentials) ;
      3. n'importe quelle clé/section de st.secrets qui ressemble à un compte de service
         (utile si les champs ont été collés sous une section comme [general]).
    Retourne (creds_dict, source) ou (None, None).
    """
    import json as json_lib

    # 1. Fichier local
    if os.path.exists(CREDENTIALS_FILE):
        try:
            with open(CREDENTIALS_FILE, encoding="utf-8") as f:
                return json_lib.load(f), f"Fichier local: {CREDENTIALS_FILE}"
        except Exception:
            pass

    # Récupérer les clés de secrets de manière sûre
    try:
        secret_keys = list(st.secrets.keys())
    except Exception:
        secret_keys = []

    # 2. Clés explicites connues
    for key in ("GOOGLE_CREDENTIALS", "google_credentials", "gcp_service_account"):
        if key in secret_keys:
            d = _coerce_to_creds_dict(st.secrets[key])
            if d and _looks_like_service_account(d):
                return d, f"Streamlit Secrets [{key}]"

    # 3. Balayage: toute valeur (string JSON ou section) qui ressemble à un compte de service
    for key in secret_keys:
        try:
            value = st.secrets[key]
        except Exception:
            continue
        d = _coerce_to_creds_dict(value)
        if d and _looks_like_service_account(d):
            return d, f"Streamlit Secrets [{key}] (auto-détecté)"
        # 3b. Chercher un niveau plus profond: section contenant une clé/JSON credentials
        #     (ex. [general] avec GOOGLE_CREDENTIALS='''...''' à l'intérieur)
        if d:
            for sub_key, sub_val in d.items():
                sub = _coerce_to_creds_dict(sub_val)
                if sub and _looks_like_service_account(sub):
                    return sub, f"Streamlit Secrets [{key}][{sub_key}] (auto-détecté)"

    # 4. Cas particulier: les champs sont collés directement au niveau racine des secrets
    #    (ex. type=..., private_key=..., client_email=... sans section)
    try:
        root = {k: st.secrets[k] for k in secret_keys}
        if _looks_like_service_account(root):
            return dict(root), "Streamlit Secrets (niveau racine)"
    except Exception:
        pass

    return None, None


@st.cache_resource(show_spinner=False)
def _get_worksheet():
    """Ouvrir la 1re feuille du Google Sheet (connexion mise en cache)."""
    from google.oauth2.service_account import Credentials
    import gspread

    creds_dict, creds_source = find_service_account_dict()

    if not creds_dict:
        try:
            keys_txt = ", ".join(st.secrets.keys())
        except Exception:
            keys_txt = "(aucun secret)"
        raise Exception(
            "Credentials du compte de service introuvables. "
            f"Clés de secrets vues: {keys_txt}. "
            "Collez le contenu de credentials.json dans Settings → Secrets "
            "(les champs type/private_key/client_email doivent être présents)."
        )

    try:
        creds = Credentials.from_service_account_info(creds_dict, scopes=GS_SCOPES)
        client = gspread.authorize(creds)
        sh = client.open_by_key(SHEET_ID)
        return sh.get_worksheet(0)
    except Exception as e:
        raise Exception(f"Erreur lors de la connexion au Google Sheet (source: {creds_source}): {e}")

@st.cache_data(ttl=60, show_spinner=False)
def load_sheet_data():
    """Lire toutes les lignes du Google Sheet dans un DataFrame (cache 60s)."""
    ws = _get_worksheet()
    values = ws.get_all_values()
    if not values:
        return pd.DataFrame()
    # En-têtes propres et uniques (évite les erreurs si colonnes vides/dupliquées)
    raw_header = [str(h).strip() for h in values[0]]
    seen, clean_header = {}, []
    for i, h in enumerate(raw_header):
        name = h if h else f"Colonne_{i + 1}"
        if name in seen:
            seen[name] += 1
            name = f"{name}_{seen[name]}"
        else:
            seen[name] = 0
        clean_header.append(name)
    # Normaliser la longueur de chaque ligne sur le nombre d'en-têtes
    rows = [r + [""] * (len(clean_header) - len(r)) for r in values[1:]]
    rows = [r[:len(clean_header)] for r in rows]
    df = pd.DataFrame(rows, columns=clean_header)
    df = df.replace("", np.nan)
    # Supprimer UNIQUEMENT les lignes vides en fin de feuille.
    # (préserve la correspondance position -> ligne du Sheet = position + 2,
    #  indispensable pour réécrire la bonne cellule Catégorie)
    while len(df) and df.iloc[-1].isna().all():
        df = df.iloc[:-1]
    df = df.reset_index(drop=True)
    return df

def ensure_gs_category_column():
    """Garantir la présence d'une colonne 'Catégorie'. Retourne (index_colonne, existait)."""
    ws = _get_worksheet()
    header = [str(h).strip() for h in ws.row_values(1)]
    if 'Catégorie' in header:
        return header.index('Catégorie') + 1, True
    col_idx = len(header) + 1
    ws.update_cell(1, col_idx, 'Catégorie')
    return col_idx, False

def _col_letter(col_idx):
    """Convertir un index de colonne (1-based) en lettre(s) A1 (1->A, 27->AA)."""
    import gspread
    a1 = gspread.utils.rowcol_to_a1(1, col_idx)  # ex: 'E1'
    return a1[:-1]  # retirer le '1'

def write_all_categories_to_sheet(col_idx, categories):
    """Écrire en une fois toutes les catégories calculées (colonne nouvellement créée)."""
    ws = _get_worksheet()
    letter = _col_letter(col_idx)
    cell_range = f"{letter}2:{letter}{len(categories) + 1}"
    ws.update(cell_range, [[c] for c in categories])

def persist_category_change(row_id, new_category):
    """Écrire la nouvelle catégorie dans le Sheet (ligne Sheet = _ID + 2)."""
    try:
        ws = _get_worksheet()
        col_idx = st.session_state.get('gs_cat_col_index')
        if not col_idx:
            return False
        ws.update_cell(int(row_id) + 2, int(col_idx), new_category)
        load_sheet_data.clear()  # invalider le cache -> rechargement des données à jour
        return True
    except Exception as e:
        st.error(f"❌ Erreur lors de l'écriture dans Google Sheets: {e}")
        return False

def detect_date_column(df):
    """Détecter la colonne date/heure, quel que soit son nom."""
    # 1) Par type déjà datetime
    for c in df.columns:
        if pd.api.types.is_datetime64_any_dtype(df[c]):
            return c
    # 2) Par mot-clé dans le nom
    keywords = ['date', 'heure', 'time', 'jour', 'quand', 'moment', 'horaire']
    for c in df.columns:
        if any(k in str(c).lower() for k in keywords):
            return c
    # 3) Par contenu convertible en dates (>50% valides)
    for c in df.columns:
        if df[c].dtype == object:
            parsed = pd.to_datetime(df[c], errors='coerce')
            if parsed.notna().mean() > 0.5:
                return c
    return None

def detect_dept_column(df, exclude=None):
    """Détecter la colonne département/zone/site, quel que soit son nom."""
    exclude = exclude or []
    keywords = ['depart', 'départ', 'region', 'région', 'zone', 'site', 'lieu',
                'localit', 'secteur', 'agence', 'direction', 'service', 'ville',
                'province', 'district', 'antenne', 'etablissement', 'établissement']
    for c in df.columns:
        if c in exclude:
            continue
        if any(k in str(c).lower() for k in keywords):
            return c
    # Repli: colonne texte à faible cardinalité (catégorielle) la plus probable
    best_col, best_card = None, None
    n = max(len(df), 1)
    for c in df.columns:
        if c in exclude or df[c].dtype != object:
            continue
        nunique = df[c].nunique(dropna=True)
        # entre 2 et 40 valeurs distinctes, pas quasi-unique (pas une description)
        if 2 <= nunique <= 40 and nunique / n < 0.5:
            if best_card is None or nunique < best_card:
                best_card, best_col = nunique, c
    return best_col

def render_editable_table(df_display, key):
    """Afficher un tableau où seule la colonne 'Catégorie' est modifiable."""
    if df_display.empty:
        st.warning("Aucune donnée à afficher")
        return
    disabled_cols = [c for c in df_display.columns if c != 'Catégorie']
    col_order = [c for c in df_display.columns if c != '_ID']
    edited = st.data_editor(
        df_display,
        use_container_width=True,
        hide_index=True,
        column_order=col_order,
        disabled=disabled_cols,
        column_config={
            'Catégorie': st.column_config.SelectboxColumn(
                'Catégorie', options=ALL_CATEGORIES, required=True,
                help="Modifiez la catégorie de la ligne ici"
            )
        },
        key=key,
    )
    # Détecter les changements de catégorie et les persister
    if '_ID' in edited.columns:
        changed = False
        for _, r in edited.iterrows():
            rid = int(r['_ID'])
            new_cat = r['Catégorie']
            match = df_display.loc[df_display['_ID'] == rid, 'Catégorie']
            if len(match) and str(match.iloc[0]) != str(new_cat):
                if st.session_state.get('use_gsheets'):
                    # Source de vérité = Google Sheets: écriture immédiate
                    persist_category_change(rid, new_cat)
                else:
                    # Repli local: mémoire de session
                    st.session_state.cat_overrides[rid] = new_cat
                changed = True
        if changed:
            st.rerun()

# Mémoire des catégories modifiées manuellement (repli si Google Sheets indisponible)
if 'cat_overrides' not in st.session_state:
    st.session_state.cat_overrides = {}

# ---- Chargement des données: Google Sheets prioritaire, Excel en repli ----
use_gsheets = False
df = None
gs_error = None

# Détection automatique des credentials (fichier local OU n'importe quelle clé de secrets)
_creds_dict, _creds_source = find_service_account_dict()
has_credentials = _creds_dict is not None

if has_credentials:
    try:
        df = load_sheet_data().copy()
        if df is not None and not df.empty:
            use_gsheets = True
        else:
            gs_error = "Le Google Sheet est vide ou illisible."
            df = None
    except Exception as e:
        gs_error = f"Erreur lors du chargement: {str(e)}"
        df = None
else:
    try:
        keys_txt = ', '.join(st.secrets.keys())
    except Exception:
        keys_txt = '(aucun secret détecté)'
    gs_error = (
        "❌ Credentials Google non trouvés!\n\n"
        f"**Clés secrètes vues par Streamlit:** {keys_txt}\n\n"
        "Le contenu de `credentials.json` (champs `type`, `private_key`, `client_email`...) "
        "doit être présent dans Settings → Secrets. Format recommandé :\n"
        "```\n"
        "GOOGLE_CREDENTIALS = '''{\n"
        "  \"type\": \"service_account\",\n"
        "  \"project_id\": \"...\",\n"
        "  ... (tout le contenu de credentials.json) ...\n"
        "}'''\n"
        "```\n"
        "Puis clique **Save** et attends le redémarrage.\n\n"
        "**Local:** place credentials.json dans: " + CREDENTIALS_FILE
    )

st.session_state.use_gsheets = use_gsheets

if use_gsheets:
    st.success(f"✅ {len(df)} lignes chargées depuis Google Sheets")
else:
    if gs_error:
        st.warning(f"⚠️ Google Sheets indisponible. Détail: {gs_error}")
        st.info(
            "Vérifiez que : (1) le Sheet est partagé en **Éditeur** avec "
            f"`{get_service_account_email()}` ; (2) c'est un **Google Sheets natif** "
            "(si c'est un .xlsx importé : Fichier → Enregistrer en tant que Google Sheets, "
            "puis utilisez le nouvel identifiant). En attendant, le fichier Excel local est utilisé."
        )
    df = load_excel_data()

# Repli ultime: données d'exemple
if df is None or df.empty:
    st.info("📊 Utilisation des données d'exemple")
    data = {
        'Date': pd.date_range('2023-01-01', periods=100, freq='h'),
        'Description': np.random.choice(['Vol projecteur', 'Blessure chute', 'Surtension', 'Dommage sono', 
                                         'Chantier risque', 'Ordinateur volé', 'Court-circuit'], 100),
        'Département': np.random.choice(['Nord', 'Sud', 'Est', 'Ouest', 'Centre'], 100),
    }
    df = pd.DataFrame(data)
    use_gsheets = False
    st.session_state.use_gsheets = False

# Normaliser les noms de colonnes
df.columns = df.columns.str.strip()

# Identifiant stable par ligne. IMPORTANT: _ID = position -> ligne Sheet = _ID + 2
df = df.reset_index(drop=True)
df['_ID'] = df.index

# Identifier les colonnes importantes (détection robuste, indépendante du nom exact)
date_col = detect_date_column(df.drop(columns=['_ID']))
dept_col = detect_dept_column(df, exclude=['_ID'] + ([date_col] if date_col else []))

# Catégorisation: conserver la catégorie du Sheet si présente, sinon auto-catégoriser
cols_for_text = [c for c in df.columns if c not in ('_ID', 'Catégorie')]
auto_cat = df[cols_for_text].apply(categorize_incident, axis=1)

if 'Catégorie' in df.columns:
    existing = df['Catégorie'].astype(str).str.strip()
    df['Catégorie'] = [
        ex if (ex and ex.lower() != 'nan') else au
        for ex, au in zip(existing, auto_cat)
    ]
else:
    df['Catégorie'] = auto_cat

# Google Sheets: garantir la colonne 'Catégorie' et l'initialiser si elle vient d'être créée
if use_gsheets and 'gs_cat_col_index' not in st.session_state:
    try:
        col_idx, existed = ensure_gs_category_column()
        st.session_state.gs_cat_col_index = col_idx
        if not existed:
            write_all_categories_to_sheet(col_idx, df['Catégorie'].tolist())
            load_sheet_data.clear()
    except Exception as e:
        st.warning(f"⚠️ Impossible de préparer la colonne 'Catégorie' dans le Sheet : {e}")

# Repli local uniquement (si pas de Google Sheets): appliquer les modifs mémorisées
if not use_gsheets and st.session_state.cat_overrides:
    df['Catégorie'] = [
        st.session_state.cat_overrides.get(int(i), c)
        for i, c in zip(df['_ID'], df['Catégorie'])
    ]

# Aperçu / diagnostic
with st.expander("🔍 Aperçu Catégorisation & Colonnes détectées"):
    source = "Google Sheets" if use_gsheets else "Fichier Excel / données locales"
    st.write(f"**Source des données:** {source}")
    st.write(f"**Colonne Date/Heure détectée:** `{date_col}`")
    st.write(f"**Colonne Département détectée:** `{dept_col}`")
    st.write(f"**Colonnes du fichier:** {', '.join(str(c) for c in cols_for_text)}")
    st.write("**Distribution des catégories détectées:**")
    cat_dist = df['Catégorie'].value_counts()
    for cat, count in cat_dist.items():
        st.write(f"- {cat}: {count} incidents")

# NAVIGATION ET FILTRES
with st.sidebar:
    st.title("📊 Navigation")

    # Source de données + rechargement
    if st.session_state.get('use_gsheets'):
        st.success("🟢 Connecté à Google Sheets")
        if st.button("🔄 Recharger depuis Google Sheets"):
            load_sheet_data.clear()
            st.rerun()
    else:
        st.warning("🟠 Mode local (Google Sheets non connecté)")

    st.divider()

    # Pages basées sur les catégories
    categories = ['Vue Générale'] + sorted(df['Catégorie'].unique().tolist())
    page = st.radio("Catégories", categories)
    
    st.divider()
    st.subheader("🔍 Filtres")
    
    # Filtre par département
    if dept_col:
        departements = ['Tous'] + sorted([str(x) for x in df[dept_col].unique() if pd.notna(x)])
        selected_dept = st.selectbox("Département", departements, key="dept_filter")
        
        if selected_dept != 'Tous':
            df_filtered = df[df[dept_col] == selected_dept].reset_index(drop=True)
        else:
            df_filtered = df.copy()
    else:
        st.info("⚠️ Aucune colonne 'Département' trouvée")
        df_filtered = df.copy()
    
    st.divider()
    st.info(f"📊 **{len(df_filtered)} incidents** affichés\n({len(df)} au total)")

    # Modifications manuelles de catégorie
    n_over = len(st.session_state.cat_overrides)
    if n_over > 0:
        st.divider()
        st.caption(f"✏️ {n_over} catégorie(s) modifiée(s) manuellement")
        if st.button("♻️ Annuler les modifications de catégorie"):
            st.session_state.cat_overrides = {}
            st.rerun()

# Vérifier qu'on a des données
if df_filtered.empty:
    st.warning("⚠️ Aucune donnée pour ce département")
else:
    
    # PAGE VUE GÉNÉRALE
    if page == "Vue Générale":
        st.markdown('<h1 class="main-header">📈 Vue Générale - Tous les Incidents</h1>', unsafe_allow_html=True)
        
        # KPIs principaux
        st.subheader("📊 Indicateurs Clés")
        col1, col2, col3, col4 = st.columns(4)
        _cols_no_id = [c for c in df_filtered.columns if c not in ('_ID', 'Catégorie')]
        with col1:
            st.metric("📋 Total Incidents", len(df_filtered))
        with col2:
            st.metric("📊 Incidents Uniques", len(df_filtered[_cols_no_id].drop_duplicates()))
        with col3:
            st.metric("🏷️ Catégories", len(df_filtered['Catégorie'].unique()))
        with col4:
            _n_cells = max(len(df_filtered) * len(_cols_no_id), 1)
            st.metric("✅ Complétude", f"{(df_filtered[_cols_no_id].notna().sum().sum() / _n_cells * 100):.1f}%")
        
        st.divider()
        
        # Distribution par catégorie
        st.subheader("📈 Distribution par Catégorie")
        col_left, col_right = st.columns(2)
        
        with col_left:
            cat_counts = df_filtered['Catégorie'].value_counts()
            st.write("**Nombre d'incidents par catégorie:**")
            for idx, (cat, count) in enumerate(cat_counts.items(), 1):
                pct = (count / len(df_filtered) * 100)
                st.write(f"{idx}. **{cat}**: {count} incidents ({pct:.1f}%)")
        
        with col_right:
            fig = px.pie(values=cat_counts.values, names=cat_counts.index, title="Distribution Catégories")
            st.plotly_chart(fig, use_container_width=True)
        
        st.divider()
        
        # Statistiques par département
        if dept_col:
            st.subheader(f"📊 Incidents par {dept_col}")
            dept_counts = df_filtered[dept_col].value_counts()
            col_left, col_right = st.columns(2)
            
            with col_left:
                for idx, (dept, count) in enumerate(dept_counts.items(), 1):
                    pct = (count / len(df_filtered) * 100)
                    st.write(f"{idx}. **{dept}**: {count} incidents ({pct:.1f}%)")
            
            with col_right:
                fig = px.bar(x=dept_counts.index, y=dept_counts.values, title=f"Distribution {dept_col}")
                st.plotly_chart(fig, use_container_width=True)
        
        st.divider()
        
        # Toutes les données (catégorie modifiable directement)
        st.subheader("📋 Toutes les Données")
        st.caption("💡 Vous pouvez modifier la catégorie de chaque ligne dans la colonne « Catégorie ».")
        render_editable_table(df_filtered, key="editor_general")
    
    # PAGES PAR CATÉGORIE
    else:
        # Filtrer par catégorie
        df_category = df_filtered[df_filtered['Catégorie'] == page].reset_index(drop=True)
        
        if df_category.empty:
            st.warning(f"⚠️ Aucun incident '{page}' pour ce département")
        else:
            st.markdown(f'<h1 class="main-header">📊 {page}</h1>', unsafe_allow_html=True)
            
            # KPIs
            st.subheader("📊 Indicateurs Clés")
            col1, col2, col3, col4 = st.columns(4)
            _cols_no_id = [c for c in df_category.columns if c not in ('_ID', 'Catégorie')]
            with col1:
                st.metric("📋 Total Incidents", len(df_category))
            with col2:
                st.metric("📊 Incidents Uniques", len(df_category[_cols_no_id].drop_duplicates()))
            with col3:
                if dept_col:
                    st.metric("🗺️ Départements", len(df_category[dept_col].unique()))
                else:
                    st.metric("🗺️ Zones", 0)
            with col4:
                _n_cells = max(len(df_category) * len(_cols_no_id), 1)
                st.metric("✅ Complétude", f"{(df_category[_cols_no_id].notna().sum().sum() / _n_cells * 100):.1f}%")
            
            st.divider()
            
            # TOP STATISTIQUES
            st.subheader("🏆 TOP STATISTIQUES")
            
            # Préparer les données temporelles pour les stats
            df_stats = df_category.copy().reset_index(drop=True)
            has_time_stats = False
            
            if date_col and date_col in df_stats.columns and len(df_stats) > 0:
                try:
                    df_stats['Date_Temp'] = pd.to_datetime(df_stats[date_col], errors='coerce')
                    df_stats['Hour'] = df_stats['Date_Temp'].dt.hour
                    
                    # Créer Hour_Range avec gestion sécurisée
                    def safe_hour_range(hour_val):
                        if pd.isna(hour_val):
                            return "N/A"
                        try:
                            h = int(hour_val)
                            if 0 <= h < 24:
                                return f"{h}h-{h+1}h"
                            else:
                                return "N/A"
                        except:
                            return "N/A"
                    
                    df_stats['Hour_Range'] = df_stats['Hour'].apply(safe_hour_range)
                    
                    # Vérifier qu'on a au moins quelques heures valides
                    valid_hours = df_stats[df_stats['Hour_Range'] != 'N/A']
                    if len(valid_hours) > 0:
                        has_time_stats = True
                except Exception as e:
                    st.error(f"Erreur temporelle: {str(e)}")
                    has_time_stats = False
            
            # Top 5 Département et Top 5 Incident Time
            col_top_left, col_top_right = st.columns(2)
            
            with col_top_left:
                if dept_col and dept_col in df_stats.columns and len(df_stats) > 0:
                    st.subheader(f"🗺️ Top 5 {dept_col}")
                    try:
                        dept_counts = df_stats[dept_col].value_counts()
                        if len(dept_counts) > 0:
                            for idx, (dept, count) in enumerate(dept_counts.head(5).items(), 1):
                                pct = (count / len(df_stats) * 100)
                                st.write(f"**{idx}.** {dept}: **{count}** incidents ({pct:.1f}%)")
                        else:
                            st.info("Aucune données de département")
                    except Exception as e:
                        st.error(f"Erreur département: {str(e)}")
                else:
                    st.subheader("🗺️ Top Département")
                    st.info("Aucune colonne « Département » détectée dans le fichier. "
                            "Voir l'aperçu des colonnes détectées en haut de page.")
            
            with col_top_right:
                if has_time_stats and len(df_stats) > 0:
                    st.subheader("⏰ Top 5 Heures")
                    try:
                        hour_counts = df_stats[df_stats['Hour_Range'] != 'N/A']['Hour_Range'].value_counts()
                        if len(hour_counts) > 0:
                            for idx, (hour, count) in enumerate(hour_counts.head(5).items(), 1):
                                pct = (count / len(df_stats) * 100)
                                st.write(f"**{idx}.** {hour}: **{count}** incidents ({pct:.1f}%)")
                        else:
                            st.info("Aucune données d'heures valides")
                    except Exception as e:
                        st.error(f"Erreur heures: {str(e)}")
                else:
                    st.info("⏰ Données temporelles non disponibles")
            
            st.divider()
            
            # Filtre département sur la page
            if dept_col:
                st.subheader(f"🔍 Filtrer par {dept_col}")
                depts_in_category = ['Tous'] + sorted([str(x) for x in df_category[dept_col].unique() if pd.notna(x)])
                selected_dept_page = st.selectbox(f"Sélectionner {dept_col}", depts_in_category, key=f"dept_{page}")
                
                if selected_dept_page != 'Tous':
                    df_category = df_category[df_category[dept_col] == selected_dept_page].reset_index(drop=True)
                
                st.info(f"📊 {len(df_category)} incidents dans cette catégorie")
            
            st.divider()
            
            # Graphiques 1: Département vs Heure
            if dept_col and date_col and len(df_category) > 0:
                st.subheader("📊 Graphiques Détaillés")
                
                # Préparer les données temporelles
                df_category_temp = df_category.copy()
                try:
                    df_category_temp['Date_Temp'] = pd.to_datetime(df_category_temp[date_col], errors='coerce')
                    df_category_temp['Hour'] = df_category_temp['Date_Temp'].dt.hour
                    df_category_temp['Date'] = df_category_temp['Date_Temp'].dt.date
                    has_time = True
                except:
                    has_time = False
                
                # Colonne 1: Distribution par Département
                col_left, col_right = st.columns(2)
                
                with col_left:
                    st.subheader(f"Distribution par {dept_col}")
                    dept_counts = df_category[dept_col].value_counts()
                    
                    # Chiffres
                    st.write("**Chiffres:**")
                    for idx, (dept, count) in enumerate(dept_counts.items(), 1):
                        pct = (count / len(df_category) * 100)
                        st.write(f"{idx}. **{dept}**: {count} ({pct:.1f}%)")
                    
                    # Graphique
                    fig = px.bar(x=dept_counts.index, y=dept_counts.values, 
                                title=f"{page} par {dept_col}",
                                labels={'x': dept_col, 'y': 'Nombre'})
                    st.plotly_chart(fig, use_container_width=True)
                
                # Colonne 2: Distribution par Heure
                with col_right:
                    if has_time:
                        st.subheader("Distribution par Heure")
                        # Filtrer les heures valides uniquement
                        valid_hours = df_category_temp[df_category_temp['Hour'].notna()]['Hour'].value_counts().sort_index()
                        
                        if len(valid_hours) > 0:
                            # Chiffres
                            st.write("**Heures les plus actives:**")
                            top_hours = valid_hours.nlargest(5)
                            for idx, (hour, count) in enumerate(top_hours.items(), 1):
                                pct = (count / len(df_category) * 100)
                                try:
                                    h = int(hour)
                                    st.write(f"{idx}. **{h}h-{h+1}h**: {count} ({pct:.1f}%)")
                                except:
                                    st.write(f"{idx}. Heure invalide: {count} ({pct:.1f}%)")
                            
                            # Graphique - Convertir les heures en strings pour Plotly
                            hour_labels = [f"{int(h)}h-{int(h)+1}h" if pd.notna(h) else "N/A" for h in valid_hours.index]
                            fig = px.bar(x=hour_labels, y=valid_hours.values, 
                                        title=f"{page} par Heure",
                                        labels={'x': 'Heure', 'y': 'Nombre'})
                            st.plotly_chart(fig, use_container_width=True)
                        else:
                            st.info("⏰ Aucune heure valide trouvée")
                    else:
                        st.info("⏰ Données temporelles non disponibles")
                
                st.divider()
            
            # Graphique 3: Timeline
            if date_col and len(df_category) > 0:
                st.subheader("📅 Distribution dans le Temps")
                try:
                    if 'df_category_temp' not in locals() or 'Date_Temp' not in df_category_temp.columns:
                        df_category_temp = df_category.copy()
                        df_category_temp['Date_Temp'] = pd.to_datetime(df_category_temp[date_col], errors='coerce')
                    
                    # Filtrer les dates valides
                    valid_dates = df_category_temp[df_category_temp['Date_Temp'].notna()]
                    if len(valid_dates) > 0:
                        time_counts = valid_dates['Date_Temp'].dt.date.value_counts().sort_index()
                        
                        if len(time_counts) > 0:
                            # Convertir en strings pour Plotly
                            date_strings = [str(d) for d in time_counts.index]
                            fig = px.line(x=date_strings, y=time_counts.values, 
                                         title=f"Évolution de {page} dans le Temps",
                                         labels={'x': 'Date', 'y': 'Nombre'},
                                         markers=True)
                            st.plotly_chart(fig, use_container_width=True)
                        else:
                            st.info("Aucune date valide trouvée")
                    else:
                        st.info("Impossible d'analyser la distribution temporelle")
                except Exception as e:
                    st.warning(f"Erreur timeline: {str(e)}")
                
                st.divider()
            
            # Tableau des données avec filtre
            st.subheader(f"📋 Données - {page} ({len(df_category)} incidents)")
            st.caption("💡 Vous pouvez modifier la catégorie de chaque ligne dans la colonne « Catégorie ». "
                       "Une ligne recatégorisée bascule automatiquement vers sa nouvelle catégorie.")
            
            # Filtre de recherche sur le tableau
            if len(df_category) > 0:
                col_search, col_clear = st.columns([4, 1])
                with col_search:
                    search_text = st.text_input("🔍 Filtrer le tableau (chercher un mot):", "", key=f"search_{page}")
                with col_clear:
                    st.write("")
                    if st.button("🔄 Réinitialiser", key=f"reset_{page}"):
                        st.session_state[f"search_{page}"] = ""
                        st.rerun()
                
                # Appliquer le filtre
                if search_text:
                    mask = df_category.astype(str).apply(
                        lambda x: x.str.contains(search_text, case=False, na=False).any(), axis=1
                    )
                    df_display = df_category[mask].reset_index(drop=True)
                    st.info(f"📊 {len(df_display)} résultats trouvés (sur {len(df_category)} total)")
                else:
                    df_display = df_category.reset_index(drop=True)
                
                render_editable_table(df_display, key=f"editor_{page}")
            else:
                st.warning("Aucune donnée à afficher")

st.divider()
st.markdown("""
    ---
    <div style="text-align: center; color: #888; font-size: 0.9em;">
    <p>SFA Works - Analyseur d'Incidents © 2024</p>
    <p>Données réelles du fichier TO-05.xlsx avec catégorisation automatique</p>
    </div>
""", unsafe_allow_html=True)
