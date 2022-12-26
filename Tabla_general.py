import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/GiomarMC/UNSA-GRAFOS/main/IngresantesCC_UNSA.csv')

df.columns
#grafico de puntaje promedio por cada año
grupo_ingresos_media = df.groupby('ANIO').mean().PUNTAJE
print(grupo_ingresos_media)
x = df.ANIO.unique()
y = grupo_ingresos_media
print(x)
print(y)

fig , ax = plt.subplots(figsize = (10,6))
ax.plot(x,y,
        marker='o')
ax.hlines(y = grupo_ingresos_media.mean(),
          xmin = 2019,
          xmax = 2023,
          color = 'red')
#TITULO EN EL EJE Y
plt.ylabel('Media de puntajes', fontsize=25)
#TITULO EN EL EJE X
plt.xlabel('Años',fontsize=25)
#TITULO PRINCIPAL
plt.suptitle('Grafica de la media de puntajes por año ',fontsize=30)
#LEYENDA
leyenda=['Grafica1','Media']
plt.legend(loc="upper left", labels=leyenda, fontsize=10)
#GRILLA
plt.grid(True, linestyle='-.',linewidth=1, color ='gray')
plt.savefig("Tabla_General.png")