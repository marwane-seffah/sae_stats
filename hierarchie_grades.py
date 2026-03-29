import pandas as pd
import matplotlib.pyplot as plt

def hierarchie_grades():
    """
    Affiche le diagramme correspondant à la répartition des grades parmis 
    les tenracs par ordre hierarchique.
    pre:
    post:
    """
    tenrac = pd.read_csv("Tenrac.csv")
    stats_grade = tenrac.groupby('nomGrade').count() # pour obtenir des effectifs
    
    GRADES = ['Affilié', 'Sympathisant', 'Adhérent', 'Chevalier', 'Grand Chevalier', 'Commandeur', "Grand'Croix"]
    
    stats_grade = stats_grade.reindex(GRADES) # https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.reindex.html
    
    stats_grade["codePersonnel"].plot.pie( # ce sera les codes personnels qu'on compte puisqu'il nous permettent de différencier les gens
           autopct = lambda z: str(round(z, 2)) + '%', 
           colors= ["#A63D40", "#C87B59", "#E9B872", "#BDB166", "#90A959", "#7A9F82", "#6494AA"],
           normalize=True)
    plt.ylabel('')
    plt.title('Fréquences des grades parmis les tenracs')
    plt.show()
hierarchie_grades()
