import streamlit as st
import pandas as pd
import plotly.express as px
from streamlit_pneu import pneu_prix


data = pd.read_csv('carter-cash-2.csv')

onglet = st.sidebar.selectbox("Choisissez un onglet", ["recherche de pneu", "analyse des pneu 1", "analyse des pneu 2"])

if onglet == "recherche de pneu":

    pneu_prix()
    
elif onglet == "analyse des pneu 1":
    
    columns = ['marque','Saisonalite', 'type_Véhicule', 'Consommation', 'Indice_Pluie', 'Bruit', 'Largeur',
               'Hauteur', 'Diametre', 'Charge', 'Vitesse', 'Runflat', 'note']
    for column in columns:
        df_filtered = data[(data[column] != "inconnue") & (data[column] != "note inconnue")]
        fig = px.histogram(df_filtered, x=column,title=f"Nombres de pneu par {column}", color=column, category_orders={column: sorted(df_filtered[column].unique())})
        st.plotly_chart(fig)



elif onglet == "analyse des pneu 2":
    
        columns = ['marque','Saisonalite', 'type_Véhicule', 'Consommation', 'Indice_Pluie', 'Bruit', 'Largeur',
               'Hauteur', 'Diametre', 'Charge', 'Vitesse', 'Runflat', 'note']
        for column in columns:
            df_filtered = data[(data[column] != "inconnue") & (data[column] != "note inconnue")]
            fig = px.box(df_filtered, x=column, y="prix", labels={column: column.capitalize(), "prix": "Prix"}, title=f"Boxplot du prix par {column}", color=column, category_orders={column: sorted(df_filtered[column].unique())})            
            st.plotly_chart(fig)