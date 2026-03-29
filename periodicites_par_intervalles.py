import pandas as pd 
import matplotlib.pyplot as plt

def periodicites_par_intervalles():
    """
    Affiche un diagramme des périodicités par intervalles
    selon si ces periodicités sont comprises entre 1 jour et 1 mois, 
    1 mois et 3 mois, 3 mois et 6 mois, 6 mois et 1 ans ou bien 1 an et 2 ans.
    On ne prend en compte que les machines dont la periodicité d'entretien est 
    inférieure ou égale à 2 ans (730 jours).
    pre:
    post:
    """
    types_entretien = pd.read_csv("typeEntretien.csv")
    plt.hist(types_entretien["periodicite"],
             range=[1,730], # Entretiens effectués de tout les jours à tout les 2 ans
             bins=[1,30,90,180,365,730], # en groupant par fréquences différentes
             color="orange",
             edgecolor='black',
             align="left")
    plt.title("Effectifs des périodicités d'entretien des types d'entretiens par intervalles de durée")
    plt.show()

periodicites_par_intervalles()
