import pandas as pd
import matplotlib.pyplot as plt

def repartition_dignite():

	Tenrac = pd.read_csv("Tenrac.csv")
	Tenrac['nomDignite'] = Tenrac['nomDignite'].fillna('Sans Dignité') #juste pour remplacer les NULL par "Sans Dignité"

	groupby = Tenrac.groupby(['nomTitre', 'nomDignite']).size().unstack(fill_value=0) #groupby pour regrouper par titre et par dignite , le .size pour savoir combien de Tenracs ont chaque combinaisons et le .unstack pour 																			transformer le groupby en grille (en prenant les lignes de nomDignite pour les changer en colonnes) ce qui rendra la figure + lisible , le 																			fill_value sert à éviter les NaN

	groupby.plot(kind='bar', stacked=False, figsize=(12, 6), width=0.8)

	plt.title('Dignités par catégorie de Titre')
	plt.xlabel('Titres des Tenracs')
	plt.ylabel('Nombre de membres')
	plt.legend(title='Dignités disponibles')
	plt.xticks(rotation=0) #pour éviter que les titres soient à 90 degrés

	plt.tight_layout()
	plt.show()
repartition_dignite()
