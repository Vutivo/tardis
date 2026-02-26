import streamlit as st
import pandas as pd

data = pd.read_csv("cleaned_dataset.csv")

data["Date"] = pd.to_datetime(data["Date"], errors="coerce")



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

def plot_temporal_evolution():

    st.subheader("Évolution du retard moyen au départ")    
    chart_data = data.groupby("Date")["Retard moyen de tous les trains au départ"].mean().reset_index()
    st.line_chart(chart_data, x="Date", y="Retard moyen de tous les trains au départ")

def plot_delay_causes():
    st.subheader("Répartition des causes de retard")

    delay_causes = [col for col in data.columns if "Prct retard pour cause" in col]

    if delay_causes:
        avg_delays = data[delay_causes].mean().sort_values(ascending=False)
        st.bar_chart(avg_delays)
    else:
        st.warning("Aucune colonne de cause de retard trouvée.")

def plot_Interact_Gare():

    st.subheader("Analyse interactive par gare")


    option = st.selectbox(
        "Choisissez une gare de départ",
        data["Gare de départ"],
        index=None,
        placeholder="Choisisez votre gare de départ"
    )

    if option:
        filtered_data = data[data["Gare de départ"] == option]
        chart_data = filtered_data.groupby("Date")["Retard moyen de tous les trains au départ"].mean().reset_index()
        st.line_chart(chart_data, x="Date", y="Retard moyen de tous les trains au départ")


    else:
        st.warning("Pas de données pour cette gare.")

def plot_predict_delay():
    ...


# --- SECTION 5: INTERFACE DE PRÉDICTION (Prediction Interface) ---
# TODO: Créer des champs de saisie pour l'utilisateur (Gare départ, Gare arrivée, mois du voyage)
# TODO: Ajouter un bouton "Prédire mon retard"
# TODO: Afficher le résultat de la prédiction du modèle de manière claire et lisible