import networkx as nx
from Functions.global_properties import V, E
from Functions.bool_functions import is_spanning
from Functions.weighted_functions import *

def cost(G, e):
    return G[e[0]][e[1]]['weight']
    #This line returns the cost for a given edge


def incident_edges(G, T):
    incident_e = []
    #This line of code creates an empty list to store neighbor edges in
    for e in E(G):
    # this is for edges in priority Q(all the edges)
    #Thus if at least one of the verteces is in the Minimum Spanning Tree 
        if e[0] in V(T) or e[1] in V(T):
        #and at least one of the vertices is in Priority Q
            if e[0] not in V(T) or e[1] not in V(T):
            #While also crossing an edge and is appended to the incident_edge
                incident_e.append(e)
    return incident_e
    # Such will return back the adjacent edges of given vertex


def minimium_incident_edge(G, T):
    incident_e = incident_edges(G, T) 
    #The minimium incident edge gets the neigbor edges of current vertex
    min_e = incident_e[0]
    # by first calling and setting min_e to the first edge of the incident_edge
    for e in incident_e:
    #Then it checks for the number of incident edges in incident_e
        if cost(G, e) < cost(G, min_e):
        #and if the cost of the edge is in range 
            min_e = e
    return min_e
    #returns adjacent edge with the minimum weight


def total_edge_cost(G, T):
#This function is used to return all the edges in a Minimum Spanning Tree
#this function is also used inside the prisim's algorithym
    return sum([cost(G, e) for e in E(T)])
    #returns line returns the total weight of all the edges in a Minimum Spanning Tree