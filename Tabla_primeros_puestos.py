import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/GiomarMC/UNSA-GRAFOS/main/IngresantesCC_UNSA.csv')

puntaje = [68.367657,62.498102,71.990000,57.980000,73.990000,63.930000,54.085307,62.382800,69.922522,75.396188,57.864303]
proceso = ['ORDINARIO II 2019','ORDINARIO I 2020','ORDINARIO II 2020','CEPRUNSA I 2021','ORDINARIO I 2021','ORDINARIO II 2021','CEPRUNSA II 2022','EXTRAORDINARIO 2022','ORDINARIO II 2022','CEPRUNSA I 2023','ORDINARIO I 2023']
fig , ax = plt.subplots(figsize = (22,6))
ax.plot(proceso,puntaje,
        marker='o')
#TITULO EN EL EJE Y
plt.ylabel('Puntaje Alcanzado', fontsize=25)
#TITULO EN EL EJE X
plt.xlabel('Proceso',fontsize=25)
#TITULO PRINCIPAL
plt.suptitle('Grafica comparativa de primeros puestos por proceso ',fontsize=30)
#LEYENDA
leyenda=['Linea de cambio']
plt.legend(loc="upper left", labels=leyenda, fontsize=10)
#GRILLA
plt.grid(True, linestyle='-.',linewidth=1, color ='gray')
plt.savefig("Tabla_Primeros_Puestos.png")