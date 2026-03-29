import pandas as pd
import matplotlib.pyplot as plt

def frequence_reunion_par_mois ():
    """
    affiche un diagramme du nombre de réunions par mois de l'année
    """
    reunion  = pd.read_csv("Reunion.csv")
    reunion["moisReunion"] = pd.to_datetime(reunion["dateReunion"]).dt.month # https://pandas.pydata.org/docs/user_guide/timeseries.html#converting-to-timestamps
    # https://pandas.pydata.org/docs/user_guide/groupby.html#aggregation
    stats_reunion = reunion.groupby('moisReunion', as_index=False).count()
    
    plt.bar(stats_reunion["moisReunion"], stats_reunion["idReunion"],
             color="#6BF178",
             edgecolor='black',
             align="center")
    plt.title("Effectifs de réunions par mois")
    plt.show()


frequence_reunion_par_mois()
