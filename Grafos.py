import pandas as pd
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

def addnodesandedges(Grafo,numero,dataf,año): #Se pasa el Grafo, la cantidad de filas de dataframe por cada año, DataFrame filtrado por año, Nodo origen del grafo(año)
    Grafo.add_node(año)#Nodo en el que se uniran los demas nodos creados del data frame
    for i in range(0,numero): #Con la funcion iloc(funcion de pandas) y coordenadas se busca los datos de cada persona como se muestra abajo
        persona = dataf.iloc[i,0]
        numero = dataf.iloc[i,1]
        carrera = dataf.iloc[i,2]
        modalidad = dataf.iloc[i,3]
        año = dataf.iloc[i,4]
        Grafo.add_node(i, person = persona, number = numero, career = carrera, modality = modalidad, year = año) #Se crea el Nodo con los valores i(numero del nodo) con los datos de cada persona
        Grafo.add_edge(año,i) #Se crea la arista que une al Nodo que contiene los datos de la persona con el Nodo del año
        #Para mostrar el contenido del nodo se utiliza (print(G.nodes[nombre del nodo])

def showsavefig(Grafo,NombreG): #Se entrega el grafo y el nombre como se guardara el grafo en extension png
    nx.draw(Grafo, node_size = 30,with_labels = False) #Dibuja el grafo con las caracteristicas del nodo de tamaño 10 y no mostrara sus etiquetas
    plt.axis("equal") #Dibujara al grafo mas ordenado
    plt.savefig(NombreG) #Se guardara el grafo como imagen.png

df = pd.read_csv("https://raw.githubusercontent.com/GiomarMC/UNSA-GRAFOS/main/IngresantesCC_UNSA.csv", index_col=["Nro"])

#Se filtra el Data Frame separandolo por años de ingreso y se crea un grafo para esos datos
Graph2019 = df[ df["ANIO"] == 2019]
print(Graph2019)
NGraph2019 = nx.Graph()

Graph2020 = df[ df["ANIO"] == 2020]
print(Graph2020)
NGraph2020 = nx.Graph()

Graph2021 = df[ df["ANIO"] == 2021]
print(Graph2021)
NGraph2021  = nx.Graph()

Graph2022 = df[ df["ANIO"] == 2022]
print(Graph2022)
NGraph2022 = nx.Graph()

Graph2023 = df[ df["ANIO"] == 2023]
print(Graph2023)
NGraph2023 = nx.Graph()

#Se imprime la cantidad de personas por año
print(len(Graph2019.index), len(Graph2020.index), len(Graph2021.index), len(Graph2022.index), len(Graph2023.index))

#Se llama a la funcion que crea los nodos y las aristas
addnodesandedges(NGraph2019, len(Graph2019.index), Graph2019, 2019)
addnodesandedges(NGraph2020, len(Graph2020.index), Graph2020, 2020)
addnodesandedges(NGraph2021, len(Graph2021.index), Graph2021, 2021)
addnodesandedges(NGraph2022, len(Graph2022.index), Graph2022, 2022)
addnodesandedges(NGraph2023, len(Graph2023.index), Graph2023, 2023)

#Se llama a la funcion que dibuja y guarda al grafo como imagen.png
showsavefig(NGraph2019, "Grafo2019.png")
showsavefig(NGraph2020, "Grafo2020.png")
showsavefig(NGraph2021, "Grafo2021.png")
showsavefig(NGraph2022, "Grafo2022.png")
showsavefig(NGraph2023, "Grafo2023.png")

#Imprime el numero de nodos que cada grafo
print(NGraph2019.number_of_nodes())
print(NGraph2020.number_of_nodes())
print(NGraph2021.number_of_nodes())
print(NGraph2022.number_of_nodes())
print(NGraph2023.number_of_nodes())