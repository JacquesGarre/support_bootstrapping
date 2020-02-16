# encoding: utf-8
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
from scipy.stats import ttest_ind

# Clear terminal
def clear(): 
    if os.name == 'nt': 
        os.system('cls') 
    else: 
        os.system('clear') 

# Read csv
dir_path = os.path.dirname(os.path.realpath(__file__))
csv = os.path.join(dir_path, "temps_visites.csv")
data = pd.read_csv(csv, encoding="utf-8") 

# Show data from csv J1
J1 = data['J1'].dropna().astype('int')
mean_J1 = J1.mean()
median_J1 = J1.median()
clear()
print(J1)

J1 = J1.value_counts().sort_index().to_frame()

# Show plot J1
J1.plot()
plt.xlabel('Temps passé sur jakazon.com (secs)', fontsize=15)
plt.ylabel('Nombre de visites', fontsize=15)
plt.xticks(np.arange(15, 120, 15))
plt.yticks(np.arange(0, 7, 1))
plt.title('Jour 1')
plt.axvline(mean_J1, color='r', linestyle='--')
plt.axvline(median_J1, color='g', linestyle='--')
plt.grid()
plt.show()


# Show data from csv J2
J2 = data['J2'].dropna().astype('int')
mean_J2 = J2.mean()
median_J2 = J2.median()
clear()
print(J2)
J2 = J2.value_counts().sort_index().to_frame()

# Show plot J2
J2.plot()
plt.xlabel('Temps passé sur jakazon.com (secs)', fontsize=15)
plt.ylabel('Nombre de visites', fontsize=15)
plt.xticks(np.arange(15, 120, 15))
plt.yticks(np.arange(0, 7, 1))
plt.title('Jour 2')
plt.axvline(mean_J2, color='r', linestyle='--')
plt.axvline(median_J2, color='g', linestyle='--')
plt.grid()
plt.show()


# Compare both days using t-test / Student
clear()
print("Le test t de Student permet de comparer les moyennes de deux series (différentes) de mesures faites sur les mêmes unités statistiques")
print("Conditions d’application du test de Student : Normalité et égalité des variances\n")

print("Une erreur fréquente est d’utiliser des tests statistiques qui supposent une distribution normale sur des données qui ne suivent pas la loi normale.")

print("La distribution normale ou de Gauss est une curve qui représente une distribution de probabilités")
print("la distribution normale est une distribution de probabilité continue.")

plt.figure() 
plt.plot(J1)
plt.plot(J2)
plt.xlabel('Temps passé sur jakazon.com (secs)', fontsize=15)
plt.ylabel('Nombre de visites', fontsize=15)
plt.xticks(np.arange(15, 120, 15))
plt.yticks(np.arange(0, 7, 1))
plt.title('Jour 1 et 2')
plt.grid()
plt.show()

print("Le théorème central limite\n")
print("Selon le théorème central limite, les moyennes des échantillons indépendants provenant d'une même population se distribuent selon une distribution normale")



