import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

Reunion = pd.read_csv("reunion.csv")

#calcul du nombres de lieu
nb_lieu = Reunion["idLieu"].value_counts()
print("Le nombre de reunion", nb_lieu)
#compte le nombre de reunion en fonction du lieu
reunion_par_lieu = Reunion.groupby("idLieu")["idReunion"].count()

lieu_populaire = reunion_par_lieu.idxmax()
lieu_moins_populaire = reunion_par_lieu.idxmin()
print("Le lieu le plus populaire est celui avec l'idLieu :", lieu_populaire)
print("Le lieu le moins populaire est celui avec l'idLieu : ", lieu_moins_populaire)

#classement des lieu en fonction du nombre de reunion
classement = reunion_par_lieu.sort_values()

#graphique en bar 
classement.plot(kind="bar")
plt.title("La popularité des lieux de réunion")
plt.xlabel("Lieu")
plt.ylabel("Nombre de réunion")
plt.show()