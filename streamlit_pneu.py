import streamlit as st
import pandas as pd
import plotly.express as px

data = pd.read_csv('carter-cash-2.csv')

def pneu_prix():
        st.markdown('<h1 style="color: white ;">Plus de <span style="color: red;">7000</span> références de pneus disponibles chez Carter-Cash</h1>', unsafe_allow_html=True)
        st.markdown('<h3 style="color: rgb(14, 17, 23);"> Plus de 7000 références de pneus disponibles chez Carter-Cash </h3>', unsafe_allow_html=True)

    

        col1, col2, col3, col4 = st.columns(4)
        col5, col6, col7, col8 = st.columns(4)
        col9, col10, col11, col12 = st.columns(4)

        largeur_options = sorted(data['Largeur'].unique())
        largeur = col1.selectbox('Largeur', largeur_options)

        hauteur_options = sorted(data['Hauteur'].unique())
        hauteur = col2.selectbox('Hauteur', hauteur_options)

        diametre_options = sorted(data['Diametre'].unique())
        diametre = col3.selectbox('Diametre', diametre_options)

        if largeur and hauteur and diametre:
            filtered_data = data[(data['Largeur'] == largeur) & (data['Hauteur'] == hauteur) & (data['Diametre'] == diametre)]
            marque_options = list(filtered_data['marque'].unique())
            marque_options.insert(0, 'Tous')
            marque = col4.selectbox('Marque', marque_options)

            indice_pluie_options = list(filtered_data['Indice_Pluie'].unique())
            indice_pluie_options.insert(0, 'Tous')
            indice_pluie = col5.selectbox('Indice Pluie', indice_pluie_options)

            saisonalite_options = list(filtered_data['Saisonalite'].unique())
            saisonalite_options.insert(0, 'Tous')
            saisonalite = col7.selectbox('Saison', saisonalite_options)

            type_vehicule_options = list(filtered_data['type_Véhicule'].unique())
            type_vehicule_options.insert(0, 'Tous')
            type_vehicule = col8.selectbox('Type de véhicule', type_vehicule_options)

            consommation_options = list(filtered_data['Consommation'].unique())
            consommation_options.insert(0, 'Tous')
            consommation = col6.selectbox('Consommation', consommation_options)

            min_price, max_price = st.slider('Sélectionnez une plage de prix', int(data['prix'].min()), int(data['prix'].max()), (int(data['prix'].min()), int(data['prix'].max())))

            filter_conditions = []
            if marque != 'Tous':
                filter_conditions.append(filtered_data['marque'] == marque)
            if indice_pluie != 'Tous':
                filter_conditions.append(filtered_data['Indice_Pluie'] == indice_pluie)
            if saisonalite != 'Tous':
                filter_conditions.append(filtered_data['Saisonalite'] == saisonalite)
            if type_vehicule != 'Tous':
                filter_conditions.append(filtered_data['type_Véhicule'] == type_vehicule)
            if consommation != 'Tous':
                filter_conditions.append(filtered_data['Consommation'] == consommation)
            
            final_filtered_data = filtered_data[(filtered_data['prix'] >= min_price) & (filtered_data['prix'] <= max_price)]
            
            for condition in filter_conditions:
                final_filtered_data = final_filtered_data[condition]
            # # # Display filtered data  --> sous forme de tableau 
            # # st.write(final_filtered_data)


        if 'sort_ascending' not in st.session_state:
            st.session_state['sort_ascending'] = True

        if st.session_state['sort_ascending']:
            sort_order = st.button('Tri décroissant')
        else:
            sort_order = st.button('Tri croissant')

        if sort_order:
            st.session_state['sort_ascending'] = not st.session_state['sort_ascending']

        if st.session_state['sort_ascending']:
            final_filtered_data.sort_values(by='prix', ascending=True, inplace=True)
        else:
            final_filtered_data.sort_values(by='prix', ascending=False, inplace=True)

        # Display filtered data
        for index, row in final_filtered_data.iterrows():
            expander_label = f"{row['marque']} - <span style='color: red; font-size: 1.5em;'>{row['prix']}€</span> - {row['descriptif']}"
            st.markdown(expander_label, unsafe_allow_html=True)
            with st.expander(" plus d'informations "):
                st.markdown(f"**Prix :** <span style='color: green;'>{row['prix']}€</span>", unsafe_allow_html=True)
                st.markdown(f"**Marque:** <span style='color: green;'>{row['marque']}</span>", unsafe_allow_html=True)
                st.markdown(f"**URL Produit:** <a href='{row['url-produit']}' target='_blank'>{row['url-produit']}</a>", unsafe_allow_html=True)
                st.markdown(f"**Info générale:** <span style='color: green;'>{row['info_generale']}</span>", unsafe_allow_html=True)
                st.markdown(f"**Descriptif:** <span style='color: green;'>{row['descriptif']}</span>", unsafe_allow_html=True)
                st.markdown(f"**Saison:** <span style='color: green;'>{row['Saisonalite']}</span>", unsafe_allow_html=True)
                st.markdown(f"**Type de véhicule:** <span style='color: green;'>{row['type_Véhicule']}</span>", unsafe_allow_html=True)
                st.markdown(f"**Consommation:** <span style='color: green;'>{row['Consommation']}</span>", unsafe_allow_html=True)
                st.markdown(f"**Indice Pluie:** <span style='color: green;'>{row['Indice_Pluie']}</span>", unsafe_allow_html=True)
                st.markdown(f"**Bruit:** <span style='color: green;'>{row['Bruit']}dB</span>", unsafe_allow_html=True)
                st.markdown(f"**Largeur:** <span style='color: green;'>{row['Largeur']}</span>", unsafe_allow_html=True)
                st.markdown(f"**Hauteur:** <span style='color: green;'>{row['Hauteur']}</span>", unsafe_allow_html=True)
                st.markdown(f"**Diametre:** <span style='color: green;'>{row['Diametre']}</span>", unsafe_allow_html=True)
                st.markdown(f"**Charge:** <span style='color: green;'>{row['Charge']}</span>", unsafe_allow_html=True)
                st.markdown(f"**Vitesse:** <span style='color: green;'>{row['Vitesse']}</span>", unsafe_allow_html=True)
                st.markdown(f"**Runflat:** <span style='color: green;'>{row['Runflat']}</span>", unsafe_allow_html=True)
                st.markdown(f"**Note:** <span style='color: green;'>{row['note']}/5</span>", unsafe_allow_html=True)
