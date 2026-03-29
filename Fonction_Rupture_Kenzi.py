import pandas as pd
import matplotlib.pyplot as plt

def rupture_stocks():
    """
    Affiche un diagramme des ingrédients les plus utilisés et indique le seuil
    de rupture potentielle
    """
    estcompose = pd.read_csv("estCompose.csv")
    stats_stock = estcompose['nomComposant'].value_counts()

    top_ingredients = stats_stock.head(10) #pour avoir les 10 plus utilisés

    plt.figure(figsize=(12, 6))
    plt.bar(top_ingredients.index, top_ingredients.values,color='blue') #on crée l'axe X (les noms des ingrédients) et l'axe 	Y (le nombre de fois où l'ingrédient apparaît)

    seuil = top_ingredients.values.mean() #définit le seuil (la moyenne des ingrédients les plus utilisés)
    plt.axhline(y=seuil, color='black', label='Seuil qui annonce une potentielle rupture') #pour faire une ligne horizontale qui marque le seuil

    plt.title('Analyse Prédictive : Ingrédients les plus utilisés (qui sont en risque de rupture)')
    plt.xlabel('Nom des ingrédients')
    plt.ylabel('Nombre de plats qui utilise cet ingrédient')
    plt.legend()
    plt.tightlayout()

    plt.show()

rupture_stocks()