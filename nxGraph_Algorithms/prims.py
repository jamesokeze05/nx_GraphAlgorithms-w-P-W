import networkx as nx
from Functions.weighted_functions import *


#The objective of prims algorithm is to return a subgraph G/E of G such that G/E contains all vertices of G
#This algorithm is an example of a greedy algorithm which obtain an optimal substructure via the greedy choice property.

#This will contain the edges and vertices of the Minimum Spanning Tree.

def prims(G, starting_vertex):
    T = nx.Graph() #Prims algorithms begin by taking a graph G (the priority queue which contains all edges and vertices) as well as a starting vertex and creates a new graph and assign it to variable T.
    T.add_node(starting_vertex)#It then adds starting vertex to the newly created graph since this will be the starting point for the Minimum Spanning Tree
    while is_spanning(G,T) == False:
    #This while loop compares the vertices in graph g to vertices in graph t to determine wether all vertices in graph g are inside of graph
        T.add_edge(e[0], e[1])
        #This will add the edge labeled e[0], e[1] to the Minimum Spanning Tree
        
    return V(T), E(T), f'Optimal Cost: {total_edge_cost(G,T)}'
    #Finallyending by returning the vertices and edges of the MST
G = nx.read_weighted_edgelist('weightedgraph.txt')
print(prims(G, 'a'))
