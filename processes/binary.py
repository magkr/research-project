import networkx as nx
import matplotlib.pyplot as plt
import random

# Expected output for 3=-10, 4=30, 5=15, 6=20, 9=20, 11=5 14=10, 19=-10, 20=-5, 24=30, 25=-20, 26=30
# Supplier:			30 		{15, 16, 18, 22, 24}
# Manufacturer:		30		{0, 1, 3, 6, 7, 8, 9}

def binary(depth):
    g = nx.DiGraph()
    g.add_node(-1,  weight=0,    player=None,            name="Start")
    g.add_node(-2,  weight=0,    player=None,            name="End")

    nodes_per_row = 1
    first_participant = 'A'
    second_participant = 'B'

    y = 1
    while y <= depth:
        for i in range(nodes_per_row):
            g.add_node(first_participant+"-"+str(y)+"-"+str(i), weight=random.randint(-1, 3), player=first_participant, name=first_participant+"-"+str(i)+"-"+str(y))
            g.add_node(second_participant+"-"+str(y)+"-"+str(i), weight=random.randint(-1, 3), player=second_participant, name=second_participant+"-"+str(i)+"-"+str(y))
            if(y % 2 == 0):
                g.add_edge(first_participant+"-"+str(y)+"-"+str(i), second_participant+"-"+str(y)+"-"+str(i))
            else:
                g.add_edge(second_participant+"-"+str(y)+"-"+str(i), first_participant+"-"+str(y)+"-"+str(i))
            if(y != 1): 
                g.add_edge(first_participant+"-"+str(y-1)+"-"+str(int(i/2)), first_participant+"-"+str(y)+"-"+str(i))
                g.add_edge(second_participant+"-"+str(y-1)+"-"+str(int(i/2)), second_participant+"-"+str(y)+"-"+str(i))
        nodes_per_row *= 2
        y += 1
        
    
    g.add_edge(-1, first_participant+"-"+str(1)+"-"+str(0))
    g.add_edge(-1, second_participant+"-"+str(1)+"-"+str(0))

    for i in range(int(nodes_per_row/2)):
        g.add_edge(first_participant+"-"+str(depth)+"-"+str(i), -2)
        g.add_edge(second_participant+"-"+str(depth)+"-"+str(i), -2)

    return g
    