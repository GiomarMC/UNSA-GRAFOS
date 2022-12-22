import pandas as pd

Lista_Puntaje = []
Lista_Anio = []
Lista = []
datos = pd.read_csv("E:\\TIF_discretas\\IngresantesCC_UNSA.csv")
print(datos)
Nodo = datos[['PUNTAJE','ANIO']]
print(Nodo)
Nodo.shape
print(datos.PUNTAJE.unique())
print(datos.ANIO.unique())
New_nodo = list(zip(datos.PUNTAJE.unique(),datos.ANIO.unique()))
print(New_nodo)
j = 0
for i in Nodo.itertuples():
    print("Contenido de la fila:\n{}".format(i), end = "\n\n")