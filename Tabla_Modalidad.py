import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/GiomarMC/UNSA-GRAFOS/main/IngresantesCC_UNSA.csv')

#barplots
#usando la base de datos representaremos en un grafico de barras el registro de compras por año
fig , ax = plt.subplots(figsize = (10,6))
y =df.groupby('PROCESO').mean().PUNTAJE
print(y)
x = ['CEPRUNSA I','CEPRUNSA II','EXTRAORDINARIO','ORDINARIO I','ORDINARIO II']
print(x)
plt.bar(x,y,
        width = 0.8,
        color = 'blue',
        )
plt.suptitle('Grafico comparativo de modalidad de ingreso',fontsize=30)
plt.ylabel('Puntaje promedio', fontsize=25)
plt.xlabel('Modalidad',fontsize=25)
plt.savefig("Tabla_Modalidad.png")