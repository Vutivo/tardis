import streamlit as st
import pandas as pd
import numpy as np
import datetime
import joblib
data = pd.read_csv("cleaned_dataset.csv")

data["Date"] = pd.to_datetime(data["Date"], errors="coerce")



def predict_func(X):
    if isinstance(X, np.ndarray):
        tree_model = joblib.load("model.joblib")
        pred = tree_model.predict(X)
        return pred
    raise ValueError("X doit être un numpy.ndarray")

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

    st.subheader("Évolution du retard moyen à l'arrivée")    
    chart_data = data.groupby("Date")["Retard moyen de tous les trains à l'arrivée"].mean().reset_index()
    chart_data = chart_data.rename(columns={"Retard moyen de tous les trains à l'arrivée": "Retard moyen de tous les trains à l arrivée"})
    
    st.line_chart(chart_data, x="Date", y="Retard moyen de tous les trains à l arrivée")

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
        data["Gare de départ"].dropna().unique(),
        index=None,
        key="interact_gare_depart",
        placeholder="Choisisez votre gare de départ"
    )

    if option:
        filtered_data = data[data["Gare de départ"] == option]

        chart_data = filtered_data.groupby("Date")["Retard moyen de tous les trains au départ"].mean().reset_index()
        st.line_chart(chart_data, x="Date", y="Retard moyen de tous les trains au départ")

        charts_data = filtered_data.groupby("Date")["Retard moyen de tous les trains à l'arrivée"].mean().reset_index()

        # Rename column because he d'ont like "'"
        charts_data = charts_data.rename(columns={"Retard moyen de tous les trains à l'arrivée": "Retard moyen de tous les trains à l arrivée"})
        st.line_chart(charts_data,x="Date",y="Retard moyen de tous les trains à l arrivée")
                    

    else:
        st.warning("Pas de données pour cette gare.")

def plot_predict_delay():

    st.subheader("Prediction du retard d'un train")
    depart = st.selectbox(
        "Choisissez une gare de départ",
        data["Gare de départ"].dropna().unique(),
        index=None,
        key="predict_gare_depart",
        placeholder="Choisisez votre gare de départ"
    )
    arrive = st.selectbox(
        "Choisissez une gare d'arrivée",
        data["Gare d'arrivée"].dropna().unique(),
        index=None,
        key="predict_gare_arrivee",
        placeholder="Choisisez votre gare d'arrivée"
    )
    date = st.date_input(
        "Choisisez une date", 
        datetime.date(2027, 7, 6)
        )

    if depart and arrive:
        if st.button("Predict delay"):

            try:
                filtered_data = pd.DataFrame([{
                    "month": date.month,
                    "year": date.year,
                    "Gare de départ": depart,
                    "Gare d'arrivée": arrive,
                    "Nombre de circulations prévues": 230
                }])

                for col in filtered_data.select_dtypes(include='object').columns:
                    filtered_data[col] = filtered_data[col].astype("category").cat.codes

                X = filtered_data.values

                prediction = predict_func(X)

                st.success(f"Prédiction du retard moyen : {prediction[0]:.2f} min")
                st.warning("Les informations données ne sont pas fiables à 100%")

            except Exception as e:
                st.error(f"Erreur lors de la prédiction : {e}")
    else: 
        st.warning("Impossible de récupérer des données pour cette prediction")
plot_columns()
plot_temporal_evolution()
plot_delay_causes()
plot_Interact_Gare()
plot_predict_delay()

