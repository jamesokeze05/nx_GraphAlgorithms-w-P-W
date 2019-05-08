

import networkx as nx
from Functions.bool_functions import *

G = nx.read_edgelist('Test/G1.txt')
nx.draw_networkx(G)


print(is_matching(G))