import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

def addnodesGeneral(Grafo,numero,dataf):#Se pasa el Grafo, la cantidad de filas de dataframe por cada año, DataFrame filtrado por año
    Grafo.add_node(numero, year = 0, modality = 'NULL', score = 0)#Se crea Nodo origen del grafo general
    Grafo.add_node(numero + 1, year = 2019, modality = 'NULL', score = 0)
    Grafo.add_node(numero + 2, year = 2020, modality = 'NULL', score = 0)
    Grafo.add_node(numero + 3, year = 2021, modality = 'NULL', score = 0)
    Grafo.add_node(numero + 4, year = 2022, modality = 'NULL', score = 0)
    Grafo.add_node(numero + 5, year = 2023, modality = 'NULL', score = 0)
    for i in range(0,numero):
        persona = dataf.iloc[i,0] #Con la funcion iloc(funcion de pandas) y coordenadas se busca los datos de cada persona como se muestra abajo
        puntaje = dataf.iloc[i,1]
        carrera = dataf.iloc[i,2]
        modalidad = dataf.iloc[i,3]
        año = dataf.iloc[i,4]
        Grafo.add_node(i, person = persona, score = puntaje, number = numero, career = carrera, modality = modalidad, year = año) #Se crea el Nodo con los valores i(numero del nodo) con los datos de cada persona
        #Para crear la aristas se crea un condicion para separarlos por años
        if año == 2019:
            Grafo.add_edge(numero + 1,i)
        elif año == 2020:
            Grafo.add_edge(numero + 2,i)
        elif año == 2021:
            Grafo.add_edge(numero + 3,i)
        elif año == 2022:
            Grafo.add_edge(numero + 4,i)
        elif año == 2023:
            Grafo.add_edge(numero + 5,i)
    #Se unen los nodos de los años
    Grafo.add_edge(numero + 1,numero)
    Grafo.add_edge(numero + 2,numero)
    Grafo.add_edge(numero + 3,numero)
    Grafo.add_edge(numero + 4,numero)
    Grafo.add_edge(numero + 5,numero)

def showsavefig(Grafo, NombreG): #Se entrega el grafo y el nombre como se guardara el grafo en extension png      
    pos = nx.layout.fruchterman_reingold_layout(Grafo)
    nx.draw(Grafo, pos = pos, node_size = 10, with_labels = False) #Dibuja el grafo con las caracteristicas del nodo de tamaño 10 y no mostrara sus etiquetas
    plt.axis("equal") #Dibujara al grafo mas ordenado
    plt.savefig(NombreG) #Se guardara el grafo como imagen.png

def showsavefigyear(Grafo, NombreG):
    color_map = nx.get_node_attributes(Grafo, "year")

    for key in color_map:
        if color_map[key] == 2019:
            color_map[key] = 'red'
        elif color_map[key] == 2020:
            color_map[key] = 'blue'
        elif color_map[key] == 2021:
            color_map[key] = 'yellow'
        elif color_map[key] == 2022:
            color_map[key] = 'purple'
        elif color_map[key] == 2023:
            color_map[key] = 'orange'
        else:
            color_map[key] = 'green'

    year_color = [color_map.get(node) for node in Grafo.nodes()]
    pos = nx.layout.fruchterman_reingold_layout(Grafo)
    nx.draw(GrafoGeneral2, pos = pos, node_size = 10, node_color = year_color, with_labels = False)
    plt.axis("equal")
    plt.savefig(NombreG)

def showsavefigmodality(Grafo, NombreG):
    color_map = nx.get_node_attributes(Grafo, "modality")

    for key in color_map:
        if color_map[key] == 'ORDINARIO I':
            color_map[key] = 'red'
        elif color_map[key] == 'CEPRUNSA I':
            color_map[key] = 'blue'
        elif color_map[key] == 'ORDINARIO II':
            color_map[key] = 'yellow'
        elif color_map[key] == 'CEPRUNSA II':
            color_map[key] = 'purple'
        elif color_map[key] == 'EXTRAORDINARIO':
            color_map[key] = 'orange'
        else:
            color_map[key] = 'green'

    modality_map = [color_map.get(node) for node in Grafo.nodes()]
    pos = nx.layout.fruchterman_reingold_layout(Grafo)
    nx.draw(GrafoGeneral2, pos = pos, node_size = 10, node_color = modality_map, with_labels = False)
    plt.axis("equal")
    plt.savefig(NombreG)

def showsavefigscore(Grafo, NombreG, score):
    color_map = nx.get_node_attributes(Grafo, "score")

    for key in color_map:
        if color_map[key] >= score:
            color_map[key] = 'red'
        elif color_map[key] < score:
            color_map[key] = 'yellow'
        elif color_map[key] == 0:
            color_map[key] = 'green'

    score_map = [color_map.get(node) for node in Grafo.nodes()]
    pos = nx.layout.fruchterman_reingold_layout(Grafo)
    nx.draw(GrafoGeneral4, pos = pos, node_size = 10, node_color = score_map, with_labels = False)
    plt.axis("equal")
    plt.savefig(NombreG)

def Opciones(opcion):
    if opcion == 1:
        showsavefig(GrafoGeneral1, "Grafo_Oficial.png")
    elif opcion == 2:
        showsavefigyear(GrafoGeneral2, "Grafo_year.png")
    elif opcion == 3:
        showsavefigmodality(GrafoGeneral3, "Grafo_modality.png")
    elif opcion == 4:
        puntaje = int(input("Ingrese el puntaje a comparar(El nodo sera Rojo si es superior al puntaje, Amarillo si es inferior): "))
        showsavefigscore(GrafoGeneral4, "Grafo_score.png", puntaje)

df = pd.read_csv("https://raw.githubusercontent.com/GiomarMC/UNSA-GRAFOS/main/IngresantesCC_UNSA.csv", index_col=["Nro"])

#Se crea un Grafo general de todos los datos del data frame
Grafo = df
print(Grafo)
GrafoGeneral1 = nx.Graph()
GrafoGeneral2 = nx.Graph()
GrafoGeneral3 = nx.Graph()
GrafoGeneral4 = nx.Graph()

#Se imprime la cantidad de personas
print(len(Grafo.index))

#Se llama a la funcion donde creara el grafo general
addnodesGeneral(GrafoGeneral1, len(Grafo.index), Grafo)
addnodesGeneral(GrafoGeneral2, len(Grafo.index), Grafo)
addnodesGeneral(GrafoGeneral3, len(Grafo.index), Grafo)
addnodesGeneral(GrafoGeneral4, len(Grafo.index), Grafo)

#Se imprime la cantidad de nodos del Grafo General
print(GrafoGeneral1.number_of_nodes())

#Se llama a la funcion que dibujara y guardara el Grafo General como imagen.png por medio de un menu de opciones
opcion = int(input("Eliga una opcion de dibujo de grafo \nopcion 1: Grafo General \nopcion 2: Grafo Coloreado por años \nopcion 3: Grafo Coloreado por modalidad \nopcion 4: Grafo Coloreado por puntaje \nopcion: "))
Opciones(opcion)