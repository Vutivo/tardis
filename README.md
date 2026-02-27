# Tardis Project

This repository contains a cleaned dataset,graphs,a model and a dashboard featuring data about the SNCF train services, especially about train delays. It showcases diffrents graph to better understand correlations and train a model being able to predict future delays.


## Contents

You will find severals files :
- project_dataset.csv : Original dataset from SNCF. It contains dirty values making it essential to clean before using it.
- cleaned_dataset.csv : Cleaned dataset. Several cloumns were removed aswell as multiple rows to ease its use.
- tardis_dashboard.py : python script running a streamlit dashboard. It features key metrics, a delay graph with a station selector and finally a delay prediction feature.
- tardis_eda.ipynb : Jupyter notebook cleaning the dataset and showcasing different graphs to better understand the dataset and analyze it.
- tardis_model.ipynb : Jupyter notebook training the model to predict future delays.
- model.zip : Compressed joblib trained model.
- requirements.txt : All depedencies that has to be installed for files to work.

## How to use

1. Clone the repository.
2. Create a virutal environnement. ```  python -m venv venv ```
3. Install depedencies. ``` pip install -r requirements.txt ```
4. Run the streamlit dashboard. ``` streamlit run tardis_dashboard.py ```


## Credits

This project was made by [Zephyr6352](https://github.com/Zephyr6352),[Kenan-LCF](https://github.com/Kenan-LCF) and [Chompy0](https://github.com/Chompy0).
