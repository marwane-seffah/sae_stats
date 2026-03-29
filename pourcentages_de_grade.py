import matplotlib.pyplot as plt
import pandas as pd 
import numpy as np


#lecture du fichier csv
Grade = pd.read_csv("Grades.csv")

nb_Grade = Grade["NomGrade"].value_counts()

#calcul des porcentages par nom de Grades
pourcentage = nb_Grade / nb_Grade.sum() * 100

#Diagramme circulairre
plt.pie(pourcentage, labels=pourcentage, 
        colors=['blue', 'yellow', 'red', 'pink', 'green', 'grey', 'purple'],
        autopct= lambda z: str(round(z, 2)) + '%',
        pctdistance=0.7,
        labeldistance=1.2,
        normalize=False)
plt.title("Répartition des grades en pourcentages")
plt.show 
