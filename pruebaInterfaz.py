
import matplotlib
matplotlib.use('TkAgg')
import random as rnd
import networkx as nx
import pandas as pd
import numpy as np
import itertools 
import folium
import webbrowser
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from tkinter import *
from tkinter import ttk
from geopy import distance
path=[]
optimal_path=[]
min_cost=50000
def Leer():
        df=pd.read_excel(open('C:/Users/ALEXANDER/Desktop/Complejidad/BD_2.xlsx',
                      'rb'),sheet_name='Hoja1',converters={'n°':int},index_col=[0])
        return df
def fact(long):
    if long==1:
        return long
    return long *fact(long-1)

def arcos_activos(camino):
    lista_arcos=[]
    for i in range(len(camino)):
        if i==len(camino)-1:
            break
        else:
            lista_arcos.append((camino[i],camino[i+1]))
    return lista_arcos

def distancia(p1, p2): 
    return np.round(distance.distance(p1,p2).km)


def find_nearest_neighbours(p, points, k):  #algorithm to find the nearest neighbours 
    distances = [0]*(len(points)-1)
    
    
    for i in range(len(distances)): 
        distances[i]= distancia(p, points[i]) 
    
    
    ind = np.argsort(distances)      #returns index, according to sorted values in array 
    
    return ind[:k] 

def next_permutation(L):
    '''
    Permute the list L in-place to generate the next lexicographic permutation.
    Return True if such a permutation exists, else return False.
    '''
     
    n = len(L)
 
    #------------------------------------------------------------
 
    # Step 1: find rightmost position i such that L[i] < L[i+1]
    i = n - 2
    while i >= 0 and L[i] >= L[i+1]:
        i -= 1
     
    if i == -1:
        return False
 
    #------------------------------------------------------------
 
    # Step 2: find rightmost position j to the right of i such that L[j] > L[i]
    j = i + 1
    while j < n and L[j] > L[i]:
        j += 1
    j -= 1
     
    #------------------------------------------------------------
 
    # Step 3: swap L[i] and L[j]
    L[i], L[j] = L[j], L[i]
     
    #------------------------------------------------------------
 
    # Step 4: reverse everything to the right of i
    left = i + 1
    right = n - 1
 
    while left < right:
        L[left], L[right] = L[right], L[left]
        left += 1
        right -= 1
             
    return True

class mclass:
    
    pathB=[]
    optimal_pathB=[]
    min_costB=50000
    
    def __init__(self,  window):
        self.window = window
        self.window.title("TSP")
        self.cantidad=StringVar()
        self.nodo=StringVar()
        self.optimal_path=[]
        self.optimal_path_w=0
        self.arcos=[]
        #Elementos de la interfaz
        #caja de texo
        self.box = Entry(window,textvariable=self.cantidad).place(x=120,y=0)#Numero de centros poblados
        self.box1 = Entry(window,textvariable=self.nodo).place(x=120,y=60)
        #buttons
        self.button = Button (window, text="Graficar ", command=self.Graficar).place(x=150,y=90)
        self.button1  = Button (window, text="Calcular ", command=self.Calcular).place(x=50,y=90)
        self.button2  = Button (window, text="Mapa ", command=self.mapa).place(x=100,y=300)
        #labels
        self.label=Label(window,text="Numero de ciudades").place(x=0,y=0)
        self.label1=Label(window,text="Algoritmo").place(x=0,y=30)
        self.label2=Label(window,text="Nodo").place(x=0,y=60)
        #Text para mostrar solucion
        
        
        
        self.txt=Text(window,width=35,height=10)
        self.txt.pack(side=LEFT)
        self.txt.insert(END, "Just a text Widget\nin two lines\n")
        #ComboBox
        self.combo=ttk.Combobox(window)
        self.combo.place(x=120,y=30)
        self.combo['values']=('BruteForce','Backtracking')
        #Variables a utilizar
        self.DB=Leer()
        self.Ln=[]
        self.Lp=[]
        self.g=[]
        
        
        self.pathB=[]
        self.optimal_pathB=[]
        self.min_costB=50000
        
        
        #Canvas para dibujar grafo
        self.canvas = Canvas(self.window,
            bg='black',bd=10,relief='ridge',width=400, height=400).place(x=300,y=0)
    
    def GenerarGrafo(self,n,pos,df):
        grafo=np.zeros((n,n))
        lista_nombres=[]
        lista_pos=[]
        for i in range(n):
            for j in range(n):
                if i==j:
                    grafo[i][j]=0
                else:
                    grafo[i][j]=np.round(distance.distance(eval(df.iloc[i+pos[i]][3]),eval(df.iloc[j+pos[i]][3])).km)
                    grafo[j][i]=np.round(distance.distance(eval(df.iloc[i+pos[i]][3]),eval(df.iloc[j+pos[i]][3])).km)
            lista_nombres.append(df.iloc[i+pos[i]][0])
            lista_pos.append(eval(df.iloc[i+pos[i]][3]))
        return grafo,lista_nombres, lista_pos
    
    def Calcular(self):
        n=int(self.cantidad.get())
        nd=int(self.nodo.get())
        v = [False for i in range(n)]
        v[nd] = True
        self.min_costB=50000
        op=self.combo.get()
        self.g,self.Ln,self.Lp=self.GenerarGrafo(n,self.knn(n),self.DB)
        """self.tsp(self.g, v, nd, n,self.pathB)
        self.optimal_path,self.optimal_path_w=self.BruteForce(self.g,nd)
        
        self.txt.delete('1.0', END)
        self.txt.insert(END,"Camino FB: "+ str(self.optimal_path))
        self.txt.insert(END, "\n"+"Peso: "+str(self.optimal_path_w))
        self.txt.insert(END, "\n"+"Centros Poblados: "+str(self.Ln))
        self.txt.insert(END,"Camino BT: "+ str(self.optimal_pathB))
        self.txt.insert(END, "\n"+"Peso: "+str(self.min_costB))
        
        self.txt.insert(END, "\n"+"Centros Poblados: "+str(self.Ln))"""
        if op=="BruteForce":
            self.optimal_path,self.optimal_path_w=self.BruteForce(self.g,nd)
            self.arcos=arcos_activos(self.optimal_path)
     
            self.txt.delete('1.0', END)
            self.txt.insert(END,"Camino FB: "+ str(self.optimal_path))
            self.txt.insert(END, "\n"+"Peso: "+str(self.optimal_path_w))
            self.txt.insert(END, "\n"+"Centros Poblados: "+str(self.Ln))
          #Backtraking
        elif op=='Backtracking':
            self.tsp(self.g, v, nd, n,self.pathB)
            self.optimal_pathB=self.optimal_pathB+[nd]
            self.arcos=arcos_activos(self.optimal_pathB)
            
            self.txt.delete('1.0', END)
            self.txt.insert(END,"Camino BT: "+ str(self.optimal_pathB))
            self.txt.insert(END, "\n"+"Peso: "+str(self.min_costB))
            self.txt.insert(END, "\n"+"Centros Poblados: "+str(self.Ln))
    
    def Graficar (self):
        self.canvas = Canvas(self.window,
        bg='black',bd=10,relief='ridge',width=400, height=400).place(x=300,y=0)
        fig = Figure(figsize=(6,6))
        a = fig.add_subplot(111)


        # the networkx part
        G=nx.Graph()
        G.add_nodes_from(list(set(self.optimal_path)))
        for x in self.arcos:
            G.add_edge(x[0],x[1],weight=self.g[x[0]][x[1]])
      
        
        
        pos=nx.circular_layout(G)
        edge_labels = nx.get_edge_attributes(G,'weight')
        
        nx.draw_networkx(G,pos=pos,ax=a)
        nx.draw_networkx_edge_labels(G,pos,edge_labels=edge_labels,ax=a)
        


        # a tk.DrawingArea
        

        self.canvas=FigureCanvasTkAgg(fig, master=self.canvas)
        self.canvas.get_tk_widget().place(x=300,y=0)
        self.canvas.draw()
    def BruteForce(self,G,  s):
        
     
        """store all vertex apart from source vertex """
        n=len(G)
        vertex=[]; 
        vertexV=[]
        a=1
        for i in range(n):
            if i !=s:
                vertex.append(i)
                vertexV.append(i)
    
   
        """ store minimum weight Hamiltonian Cycle. """
        min_path = 9999999
    
        lista_caminos=[]
        permutaciones=list(itertools.permutations(vertexV,n-1))
        while next_permutation(vertex):
   
  
            """store current Path weight(cost) """
            current_pathweight = 0; 
          
            """ compute current path weight""" 
            k = s; 
            for i in range(len(vertex)):
                current_pathweight += G[k][vertex[i]]; 
            
                k = vertex[i];
        
        
            current_pathweight += G[k][s]
        
        
        
            """ update minimum""" 
            min_path = min(min_path, current_pathweight);
        
            lista_caminos.append([list(permutaciones[a]),current_pathweight])
        
            if a==fact(len(vertexV)):
                break
            a+=1
        
        for i in range(len(lista_caminos)):
            if lista_caminos[i][1]==min_path:
                sol= lista_caminos[i]
        recorrido=[s]+sol[0]+[s]
        peso=sol[1]
        return recorrido,peso
    
    def mapa(self):
        mapa=folium.Map(location=[self.Lp[0][0],self.Lp[0][1]])
        for i,j in self.arcos:
            linea=folium.PolyLine(locations=[[self.Lp[i][0],self.Lp[i][1]],
                                     [self.Lp[j][0],self.Lp[j][1]]],weight=5)
            mapa.add_child(linea)
            fg=folium.FeatureGroup(name="CentroPoblado")
            for n in range(len(self.Ln)):
                fg.add_child(folium.Marker(location=self.Lp[n],
                                  popup=folium.Popup(self.Ln[n]),
                                  icon=folium.Icon(color='blue',
                                                  icon_color='white',
                                                  icon='info_sing')
                                  ))
                mapa.add_child(fg)
        
        mapa.save('index.html')
        
        new = 2 # open in a new tab, if possible

        # open a public URL, in this case, the webbrowser docs
        url = "index.html"
        webbrowser.open(url,new=new)
    
    def knn(self,n):
        i=rnd.randint(1,140000)
        points=[]
        index=[]
        for i in range(i,i+2500):
            points.append(eval(self.DB.iloc[i][3]))
            index.append(i)
        p=points[0]
        ind=find_nearest_neighbours(p, points,n)
        puntos=[]
        for x in ind:
            puntos.append(index[x])
    
        return puntos
    def tsp(self,graph, v, currPos, n,path):
        
        
        # Si se llega al último nodo y tiene
        # un enlace al nodo inicial, es decir,
        # la fuente y luego mantener el mínimo
        # valor fuera del costo total de
        # recorrido y “ans”
        # Finalmente volver a verificar
        # más valores posibles
        
        if len(path)+1==n:
            nd=int(self.nodo.get())
            path=[nd]+path
            
            temp_cost=0
            k=path[0]
            for x in range(len(path)):
                temp_cost += graph[k][path[x]]; 
                k = path[x];
            temp_cost+= graph[k][0]
            
            
            if temp_cost<self.min_costB:
                self.optimal_pathB=path
                self.min_costB=temp_cost
            
            elif temp_cost==self.min_costB:
                self.optimal_pathB=[]
                for t in path:
                    self.optimal_pathB.append(t)
            
            return  

        # PASO DE BACKTRACKING
        # Loop para atravesar la lista de adyacencia.
        # de nodo currPos y aumentando la cuenta
        # por 1 y costo por gráfico [currPos] [i] valor
        for i in range(n):
        
            if (v[i] == False and graph[currPos][i]):

                # Mark as visited
                v[i] = True
            
                path.append(i)
            
                self.tsp(graph, v, i, n, path)
            
            #Marcar el nodo como no visitado
                v[i] = False
                path.pop()
    
    
#Inicializador de la APP   
window= Tk()
window.geometry('750x400')
start= mclass (window)
window.mainloop()
