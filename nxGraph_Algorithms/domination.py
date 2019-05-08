from Functions.bool_functions import *
from Functions.global_properties import *
from itertools import combinations

def minimum_dominating_set(G):
    for k in range (1, n(G)):
        for S in combinations (V(G), k):
            if is_dominating(G, list(S)) == True:
                return list(S)
            
            
def domination_number(G):
    return len(minimum_dominating_set(G))

