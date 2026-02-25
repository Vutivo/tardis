import streamlit as st
import pandas as pd

data = pd.read_csv("cleaned_dataset.csv")


def plot_columns():

    avg_delay = data["Retard moyen de tous les trains à l'arrivée"].mean()
    
    total_trains = data["Nombre de circulations prévues"].sum()

    punctuality_rate = (data["fiabilite de la ligne"].mean()) *100

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(label="Retard Moyen Global", value=f"{avg_delay:.2f} min")

    with col2:
        st.metric(label="Total de circulations depuis 2018", value=f"{total_trains:,}")

    with col3:
        st.metric(label="Taux de Ponctualité", value=f"{punctuality_rate:.1f}%")


    

plot_columns()

def plot_temporal_evolution():

    st.subheader("Évolution du retard moyen au départ")    
    chart_data = data.groupby("Date")["Retard moyen de tous les trains au départ"].mean().reset_index()
    st.line_chart(chart_data, x="Date", y="Retard moyen de tous les trains au départ")

plot_temporal_evolution()



# --- SECTION 2: DISTRIBUTION DES RETARDS (Delay Patterns) ---
# TODO: Créer un graphique (Pie chart ou Bar chart horizontal) 
# TODO: Utiliser les colonnes 'Prct retard pour cause...' (externes, infrastructure, matériel, etc.)
# TODO: Ce graphique doit montrer la répartition moyenne des causes de retard au niveau national

# --- SECTION 3: ANALYSE INTERACTIVE PAR GARE (Interactive Element) ---
# TODO: Créer un sélecteur (st.selectbox) pour choisir une 'Gare de départ'
# TODO: Filtrer le dataframe en fonction de la gare choisie
# TODO: Afficher un graphique à barres montrant les gares d'arrivée les plus touchées par les retards depuis cette ville


# --- SECTION 5: INTERFACE DE PRÉDICTION (Prediction Interface) ---
# TODO: Créer des champs de saisie pour l'utilisateur (Gare départ, Gare arrivée, mois du voyage)
# TODO: Ajouter un bouton "Prédire mon retard"
# TODO: Afficher le résultat de la prédiction du modèle de manière claire et lisible