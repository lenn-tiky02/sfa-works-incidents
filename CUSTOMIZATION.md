# 🎨 Guide de Personnalisation - Analyseur d'Incidents

Ce guide vous montre comment modifier et personnaliser l'application selon vos besoins.

---

## 🎨 Modifier les Couleurs

### Palettes Actuelles

Dans `.streamlit/config.toml`:

```toml
[theme]
primaryColor = "#1f77b4"        # Bleu (SFA Works)
backgroundColor = "#ffffff"    # Blanc
secondaryBackgroundColor = "#f0f2f6"  # Gris clair
textColor = "#262730"          # Gris foncé
```

### Exemples de Palettes

**Option 1: Vert (Sécurité)**
```toml
primaryColor = "#2ecc71"        # Vert clair
backgroundColor = "#ffffff"
secondaryBackgroundColor = "#ecf0f1"
textColor = "#2c3e50"
```

**Option 2: Orange (Alerte)**
```toml
primaryColor = "#e74c3c"        # Rouge-orange
backgroundColor = "#ffffff"
secondaryBackgroundColor = "#fde8e0"
textColor = "#c0392b"
```

**Option 3: Violet (Premium)**
```toml
primaryColor = "#9b59b6"        # Violet
backgroundColor = "#f8f9fa"
secondaryBackgroundColor = "#ecf0f1"
textColor = "#2c3e50"
```

---

## 📝 Modifier le Titre et l'En-tête

Dans `app.py`, ligne 22:

```python
# AVANT:
st.set_page_config(
    page_title="Analyseur d'Incidents - SFA Works",
    page_icon="📊",
    layout="wide",
)

# APRÈS:
st.set_page_config(
    page_title="Votre Nouveau Titre",
    page_icon="🏢",  # Changez l'emoji
    layout="wide",
)
```

### Emojis Utiles
```
📊 Dashboard      🎯 Target
🔓 Sécurité       ⚡ Électrique
🏗️ Construction   🩹 Santé
📈 Statistiques   🚗 Transport
⚠️ Alerte         ✅ Succès
```

---

## 📋 Ajouter une Nouvelle Page

### Étape 1: Ajouter à la Navigation

Dans `app.py`, ligne 35:

```python
# AVANT:
page = st.radio("Sélectionnez une page", 
                ["Vue Générale", "Blessures Corporelles", ...])

# APRÈS:
page = st.radio("Sélectionnez une page", 
                ["Vue Générale", "Blessures Corporelles", ..., "Ma Nouvelle Page"])
```

### Étape 2: Créer le Contenu

À la fin de `app.py`, avant le footer (avant la ligne 410):

```python
elif page == "Ma Nouvelle Page":
    st.markdown('<h1 class="main-header">🆕 Ma Nouvelle Page</h1>', unsafe_allow_html=True)
    
    # Contenu 1: KPI
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("📊 Métrique 1", 123)
    with col2:
        st.metric("📊 Métrique 2", 456)
    with col3:
        st.metric("📊 Métrique 3", 789)
    
    # Contenu 2: Graphique
    st.subheader("Visualisation")
    fig = px.bar(x=['A', 'B', 'C'], y=[10, 20, 15])
    st.plotly_chart(fig, use_container_width=True)
    
    # Contenu 3: Texte
    st.info("ℹ️ **Information importante** ici")
```

---

## 📊 Modifier les Données d'Exemple

### Changer le Nombre de Lignes

Dans `app.py`, ligne 53:

```python
# AVANT:
data = {
    'Date': pd.date_range('2023-01-01', periods=100, freq='D'),
    ...
}

# APRÈS:
data = {
    'Date': pd.date_range('2023-01-01', periods=1000, freq='D'),  # 1000 lignes
    ...
}
```

### Ajouter une Nouvelle Colonne

```python
# DANS data = {...}:
'Region': np.random.choice(['Nord', 'Sud', 'Est', 'Ouest'], 100),

# PUIS L'UTILISER:
df['Region'].value_counts()
```

---

## 🎨 Modifier les Graphiques

### Changer les Couleurs d'un Graphique

```python
# AVANT:
fig = px.bar(x=causes.index, y=causes.values)

# APRÈS (avec dégradé rouge):
fig = px.bar(x=causes.index, y=causes.values,
            color=causes.values,
            color_continuous_scale='Reds')
```

### Couleurs Disponibles
```
'Blues', 'Reds', 'Greens', 'Oranges', 'Purples'
'Blues_r', 'Reds_r'  (inversé)
'Viridis', 'Plasma', 'Turbo'
```

### Ajouter des Étiquettes

```python
fig = px.bar(...)
fig.update_layout(
    title="Mon Titre",
    xaxis_title="Axe X",
    yaxis_title="Axe Y",
    showlegend=False
)
```

### Ajouter des Annotations

```python
fig.add_annotation(
    text="Important: Vérifiez les données",
    xref="paper", yref="paper",
    x=0.5, y=0.5,
    font=dict(size=14, color="red")
)
```

---

## 📈 Ajouter des KPIs

### Métrique Simple

```python
st.metric("Titre", valeur)
st.metric("Titre", valeur, delta="Changement")
```

### Colonne de Métriques

```python
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("KPI 1", 100)
with col2:
    st.metric("KPI 2", 200)
with col3:
    st.metric("KPI 3", 300)
```

### Avec Couleur de Fond

```python
st.markdown("""
    <div style="background: #e8f4f8; padding: 15px; border-radius: 8px;">
    <h3>Ma Métrique Stylisée</h3>
    <p>Valeur: <b>12345</b></p>
    </div>
""", unsafe_allow_html=True)
```

---

## 📋 Modifier les Listes et Tableaux

### Tableau Simple

```python
data = {
    'Colonne A': [1, 2, 3],
    'Colonne B': ['a', 'b', 'c']
}
df = pd.DataFrame(data)
st.dataframe(df)
```

### Tableau Stylisé

```python
st.dataframe(
    df,
    use_container_width=True,
    hide_index=True,
    column_config={
        "Colonne A": st.column_config.NumberColumn("A", format="$%d"),
        "Colonne B": st.column_config.TextColumn("B", width="medium"),
    }
)
```

### Listes à Puces

```python
st.write("""
- Item 1
- Item 2
- Item 3
""")
```

---

## 🎯 Modifier les Messages d'Information

### Types de Messages

```python
st.info("💡 Information - couleur bleue")
st.warning("⚠️ Attention - couleur orange")
st.error("❌ Erreur - couleur rouge")
st.success("✅ Succès - couleur verte")
```

### Divider (Ligne de Séparation)

```python
st.divider()  # Crée une ligne de séparation
```

### Texte Formaté

```python
st.markdown("**Texte gras**")
st.markdown("*Texte italique*")
st.markdown("[Lien](https://example.com)")
st.markdown("# Titre H1")
st.markdown("## Titre H2")
st.markdown("> Citation")
```

---

## 🔧 Modifier l'En-tête HTML/CSS

Au début de `app.py` (ligne 26):

```python
# AVANT:
st.markdown("""
    <style>
    .main-header { font-size: 2.5em; color: #1f77b4; margin-bottom: 30px; }
    ...
    </style>
""", unsafe_allow_html=True)

# APRÈS:
st.markdown("""
    <style>
    .main-header { 
        font-size: 3em;              /* Plus grand */
        color: #e74c3c;              /* Couleur rouge */
        margin-bottom: 30px; 
        font-weight: bold;           /* Plus gras */
        text-shadow: 2px 2px 4px rgba(0,0,0,0.1);  /* Ombre */
    }
    </style>
""", unsafe_allow_html=True)
```

---

## 🌐 Modifier le Contenu d'une Page Existante

### Exemple: Changer le Contenu de "Vue Générale"

Trouvez la section (environ ligne 62):

```python
if page == "Vue Générale":
    # Votre code ici
```

Vous pouvez:
- Ajouter plus de KPIs
- Changer les graphiques
- Ajouter du texte explicatif
- Réorganiser les éléments

---

## 🚀 Avant/Après: Exemple Complet

### ❌ Avant (Simple)
```python
if page == "Test":
    st.title("Test")
    st.write("Coucou")
```

### ✅ Après (Professionnel)
```python
if page == "Test":
    st.markdown('<h1 class="main-header">🆕 Test Page</h1>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Métrique 1", 100, delta="+10%")
    with col2:
        st.metric("Métrique 2", 200, delta="-5%")
    
    st.divider()
    
    st.subheader("Visualisation")
    fig = px.bar(x=['A', 'B', 'C'], y=[10, 20, 15],
                color_discrete_sequence=['#1f77b4'])
    st.plotly_chart(fig, use_container_width=True)
    
    st.info("💡 **Info**: Ceci est un exemple personnalisé")
```

---

## 📚 Ressources Utiles

- **Streamlit Docs**: https://docs.streamlit.io
- **Plotly Docs**: https://plotly.com/python/
- **Pandas Docs**: https://pandas.pydata.org/docs/
- **Colors**: https://www.w3schools.com/colors/colors_hex.asp

---

## 🐛 Déboguer les Erreurs

### Erreur: "NameError: name 'df' is not defined"
```python
# Vérifiez que la variable 'df' est définie avant utilisation
# Ou utilisez: df = load_sample_data()
```

### Erreur: "AttributeError: 'xxx' object has no attribute 'yyy'"
```python
# Vérifiez que vous utilisez la bonne méthode
# pandas: df.groupby(), df.value_counts()
# plotly: px.bar(), px.pie()
```

### Le graphique ne s'affiche pas
```python
# Vérifiez:
1. import plotly.express as px
2. Données valides
3. Noms de colonnes corrects
```

---

## 🎯 Bonnes Pratiques

### À Faire ✅
- Toujours commenter votre code
- Utiliser des noms variables explicites
- Tester après chaque modification
- Sauvegarder régulièrement

### À Éviter ❌
- Modifier sans sauvegarder
- Changer tous les styles en même temps
- Ajouter trop de graphiques
- Ignorer les erreurs

---

## 💾 Sauvegarder et Tester

Après une modification:

```bash
# 1. Sauvegarder le fichier (Ctrl + S)
# 2. Redémarrer Streamlit
#    - Ctrl + C dans le terminal
#    - streamlit run app.py
# 3. Vérifier le changement dans le navigateur
```

---

## 🎉 Conclusion

Vous pouvez maintenant:
- ✅ Modifier les couleurs et styles
- ✅ Ajouter des pages
- ✅ Changer les graphiques
- ✅ Personnaliser le contenu
- ✅ Adapter pour vos besoins

**Happy Customizing!** 🚀
