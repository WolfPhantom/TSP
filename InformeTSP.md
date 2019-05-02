# Problema de vendedor ambulante
## 1.	Introducción
El  problema del vendedor viajero o también conocido como TSP (por siglas en ingles). Consiste en encontrar, en un grupo finito de ciudades y sus respectivos costos de viajes entre ciudad y ciudad, el camino más económico de recorrer todas las ciudades. Dicho recorrido tiene ciertas condiciones, se debe iniciar el recorrido en una ciudad, pasar por todas las ciudades, solamente una vez, y terminar en la ciudad en la que se comenzó. Esto debe ser logrado teniendo en consideración que el resultado debe ser el recorrido que tenga el menor costo.

A lo largo de la historia, se han diversas soluciones a este problema. Por ejemplo: 

> Karl Menger (Shortest Hamiltonian Path, 1930), J.B. Robinson 	(Hamiltonian game, 1949), G. Dantzig, R. Fulkerson, y S. Johnson 	(Solution of a large-scale traveling-salesman problem, 1954), M. Held 	and R.M. Karp (Introducción de heurísticas basadas en programación 	dinámica, 1962), entre otros. (Espinoza, 2006)

La principal motivación para el desarrollo del proyecto, consiste en las diferentes aplicaciones del TSP. Algunas de ellas son estudio en la secuencia de genes, diseño de chips, enrutamiento de vehículos, entre otras.

## 2.	Objetivo

El presente trabajo tiene como objetivo principal encontrar una solución parcial al problema de TSP usando una *dataset* del Ministerio de Educación del Perú. La cual contiene la posición geográfica (latitud y longitud) de cada centro poblado del Perú.

## 3.	Marco Teórico

El algoritmo de búsqueda por fuerza bruta, conocido también como búsqueda exhaustiva. Es una técnica de programación, la cual consiste en encontrar todos los candidatos a solución y verificar, uno por uno, si satisfacen al problema.

El *backtracking* es una técnica de programación para hacer una búsqueda a través de todas las alternativas en un espacio de búsqueda. Para esto, los algoritmos que emplean *backtracking* construyen posibles soluciones candidatas. Por ejemplo, dada una solución candidata “s” se verifica si es solución, si no lo es se construyen todas las posibles extensiones de “s” y se invoca recursivamente al algoritmo con todas ellas.

## 4.	Soluciones
Fuerza Bruta(Solucion Ingenua)
1) Considere la ciudad 1 como el punto inicial y final. 
2) Generar todos (n-1)! Permutaciones de las ciudades. 
3) Calcule el costo de cada permutación y realice un seguimiento de la    permutación del costo mínimo. 
4) Devolver la permutación con costo mínimo.

```Python
def BruteForce(self,G,  s):
        
        """almacenar todos los vértices aparte del vértice fuente """
        n = len(G)
        vertex = []; 
        vertexV = []
        a = 1
        for i in range(n):
            if i != s:
                vertex.append(i)
                vertexV.append(i)
    
   
        """ almacenar el peso mínimo del ciclo hamiltoniano."""
        min_path = 9999999
    
        lista_caminos = []
        permutaciones = list(itertools.permutations(vertexV, n-1))
        while next_permutation(vertex):
   
  
            current_pathweight = 0; 
          
            
            k = s; 
            for i in range(len(vertex)):
                current_pathweight += G[k][vertex[i]]; 
            
                k = vertex[i];
        
        
            current_pathweight += G[k][s]
        

            min_path = min(min_path, current_pathweight);
        
            lista_caminos.append([list(permutaciones[a]), current_pathweight])
        
            if a == fact(len(vertexV)):
                break
            a += 1
        
        for i in range(len(lista_caminos)):
            if lista_caminos[i][1] == min_path:
                sol = lista_caminos[i]
        recorrido = [s] + sol[0] + [s]
        peso = sol[1]
        return recorrido, peso

```


BackTracking

En este caso, primero creamos todos los ciclos hamiltonianos utilizando conceptos de retroceso profundo. Entonces entre
En estos ciclos hamiltonianos, el problema del vendedor ambulante corresponde a los ciclos de costo mínimo.
 
Algoritmo:

•	Primero, hemos creado la estructura de datos del gráfico utilizando la matriz de adyacencia para almacenar cada vértices.

•	Generado el peso aleatorio o la matriz de conexiones.

•	Luego extraemos todos los ciclos hamiltonianos usando la función tsp () en nuestroprograma. Esta función funciona como:

•	Primero, enviamos el vértice inicial como argumento en función.

•	Ahora, el siguiente fragmento de código se procesa solo en vértices no visitados. También tenemos Estructura de datos de ruta mantenida para almacenar la ruta hamiltoniana. Visitas de ruta cada vértice exactamente una vez.

•	Compruebe si agregar vértice a la ruta lleva a la solución o no es

•	Contribuyendo entonces considérelo en el camino hamiltoniano.

•	De lo contrario Retrocede hasta que te recuperes.

•	También hemos implementado el código para obtener una ruta óptima dentro de la propia función.
Verificamos la ruta, si es la ruta, calculamos el costo de los ciclos y
Compáralo con el ciclo global hasta ahora. Y si queda satisfecho entonces almacenamos el camino óptimo en la estructura de datos para imprimirlo después del final del programa.
```Python
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

```
## 5.	Complejidad

La complejidad del algoritmo de la búsqueda por la fuerza bruta  en el tiempo es O (N!). Por lo que nunca debes usar en listas largas. 

## 6. Conclusiones
Luego de hacer las pruebas debidas, hemos comprobado que se ha podido implementar una solución para TSP en los nodos de tamaño corto, debido a que en el peor de los casos es posible factorial de n

## Referencias

Espinoza, D. (2006). El Problema del Vendedor Viajero (TSP) y Programación Entera (IP) [diapositivas de PowerPoint]. Recuperado de: http://www.dii.uchile.cl/~daespino/PApers/TSP_and_IP_chile_050820.pdf 

Baier, J. (s.f.). Backtracking [diapositivas de PowerPoint]. Recuperado de: http://jabaier.sitios.ing.uc.cl/iic2552/backtracking.pdf 
