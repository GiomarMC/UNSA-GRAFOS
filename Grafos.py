import pandas as pd
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

def addnodesandedges(G,n,p,y): #Se pasa el grafo, la cantidad de filas de dataframe por cada año, DataFrame filtrado por año, Nodo origen del grafo
    G.add_node(y)#Nodo en el que se uniran los demas nodos creados del data frame
    for i in range(0,n):
        s = p.iloc[i,0] #con la funcion iloc y coordenadas busco los datos de cada persona como se muestra abajo
        n = p.iloc[i,1]
        c = p.iloc[i,2]
        m = p.iloc[i,3]
        a = p.iloc[i,4]
        G.add_node(i, person = s, number = n, career = c, modality = m, year = a) #añado nodos con un valor i con atributos sacados del dataframe del año
        G.add_edge(y,i) #rtambien de paso le creo una arista entre el nodo creado ahora jutno con el nodo que tiene el y-años
        #print(G.nodes[i]) #se muestra el nodo creado con sus atributos


def showsavefig(P,s): #se el da el grafo y el string del nombre de la imagen
    nx.draw(P,with_labels=True) #dibujo la figura cmostranros los numero
    plt.savefig(s) #la guardo en formanto prederminado como png

df = pd.read_csv("https://raw.githubusercontent.com/GiomarMC/UNSA-GRAFOS/main/IngresantesCC_UNSA.csv", index_col=["Nro"])
Grafo = df
print(Grafo)
GrafoGeneral = nx.Graph()

Graph2019 = df[ df["ANIO"] == 2019] #hago un dataframe del año 2019 y asi con los demas
print(Graph2019 )
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

print(len(Graph2019.index), len(Graph2020.index), len(Graph2021.index), len(Graph2022.index), len(Graph2023.index), len(Grafo.index)) #muestro la cantidad de numeros de cada áño

addnodesandedges(NGraph2019, len(Graph2019.index), Graph2019, 2019) #funcion pa crear el grafo de un solo año asi los demas iguals
addnodesandedges(NGraph2020, len(Graph2020.index), Graph2020, 2020)
addnodesandedges(NGraph2021, len(Graph2021.index), Graph2021, 2021)
addnodesandedges(NGraph2022,len(Graph2022.index),Graph2022,2022)
addnodesandedges(NGraph2023, len(Graph2023.index), Graph2023, 2023)
addnodesandedges(GrafoGeneral, len(Grafo.index), Grafo, 0)

showsavefig(NGraph2019, "Grafo2019.png") #funcion para descargar la imagen del  grafo corresppodientre y cono nobmre y terminarcion de como quiero que sea el archo puede ser
showsavefig(NGraph2020, "Grafo2020.png") # png, jpg, pdf, y otros mas
showsavefig(NGraph2021, "Grafo2021.png")
showsavefig(NGraph2022, "Grafo2022.png")
showsavefig(NGraph2023, "Grafo2023.png")
showsavefig(GrafoGeneral, "Grafo_Oficial.png")

print(NGraph2019.number_of_nodes()) #muestro los nodos de cada grafo para compara que este correspondiento al numero de filas  se tendria q restar -1
print(NGraph2020.number_of_nodes())
print(NGraph2021.number_of_nodes())
print(NGraph2022.number_of_nodes())
print(NGraph2023.number_of_nodes())