import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

def addnodesGeneral(Grafo,numero,dataf):#Se pasa el Grafo, la cantidad de filas de dataframe por cada año, DataFrame filtrado por año
    Grafo.add_node("INICIO")#Se crea Nodo origen del grafo general
    for i in range(0,numero):
        persona = dataf.iloc[i,0] #Con la funcion iloc(funcion de pandas) y coordenadas se busca los datos de cada persona como se muestra abajo
        carrera = dataf.iloc[i,2]
        modalidad = dataf.iloc[i,3]
        año = dataf.iloc[i,4]
        Grafo.add_node(i, person = persona, number = numero, career = carrera, modality = modalidad, year = año) #Se crea el Nodo con los valores i(numero del nodo) con los datos de cada persona
        #Para crear la aristas se crea un condicion para separarlos por años
        if año == 2019:
            Grafo.add_edge(2019,i)
        elif año == 2020:
            Grafo.add_edge(2020,i)
        elif año == 2021:
            Grafo.add_edge(2021,i)
        elif año == 2022:
            Grafo.add_edge(2022,i)
        elif año == 2023:
            Grafo.add_edge(2023,i)
    #Se unen los nodos de los años
    Grafo.add_edge(2019,"INICIO")
    Grafo.add_edge(2020,"INICIO")
    Grafo.add_edge(2021,"INICIO")
    Grafo.add_edge(2022,"INICIO")
    Grafo.add_edge(2023,"INICIO")

def showsavefig(Grafo,NombreG): #Se entrega el grafo y el nombre como se guardara el grafo en extension png
    nx.draw(Grafo, node_size = 10,with_labels = False) #Dibuja el grafo con las caracteristicas del nodo de tamaño 10 y no mostrara sus etiquetas
    plt.axis("equal") #Dibujara al grafo mas ordenado
    plt.savefig(NombreG) #Se guardara el grafo como imagen.png

df = pd.read_csv("https://raw.githubusercontent.com/GiomarMC/UNSA-GRAFOS/main/IngresantesCC_UNSA.csv", index_col=["Nro"])

#Se crea un Grafo general de todos los datos del data frame
Grafo = df
print(Grafo)
GrafoGeneral = nx.Graph()

#Se imprime la cantidad de personas
print(len(Grafo.index))

#Se llama a la funcion donde creara el grafo general
addnodesGeneral(GrafoGeneral, len(Grafo.index), Grafo)

#Se llama a la funcion que dibujara y guardara el Grafo General como imagen.png
showsavefig(GrafoGeneral, "Grafo_Oficial.png")

#Se imprime la cantidad de nodos del Grafo General
print(GrafoGeneral.number_of_nodes())
