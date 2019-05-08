from itertools import combinations 
from Functions.bool_functions import *
from Functions.global_properties import *
from math import floor 
import networkx as nx

def maximum_matching(G):
    for k in range(floor(n(G)/2), 1, -1):
        for M in combinations(E(G),k):
            if is_matching(G,list(M)) == True:
                return list(M)

def matching_number(G):
    return len(maximum_matching(G))
        
G = nx.erdos_renyi_graph(20,.1)
nx.draw_networkx(G)
print(matching_number(G))