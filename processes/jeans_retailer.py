import networkx as nx
import matplotlib.pyplot as plt

# Expected output for 3=-10, 4=30, 5=15, 6=20, 9=20, 11=5 14=10, 19=-10, 20=-5, 24=30, 25=-20, 26=30
# Supplier:			30 		{15, 16, 18, 22, 24}
# Manufacturer:		30		{0, 1, 3, 6, 7, 8, 9}


def jeans_retailer():
    g = nx.DiGraph()
    g.add_node(-1,  weight=0,   player=None,            name="Start")
    g.add_node(-2,  weight=0,   player=None,            name="End")

    g.add_node(0,   weight=0,   player="Retailer",  name="Order jeans")
    g.add_node(1,   weight=0,   player="Retailer",  name="Receive high quality jeans") 
    g.add_node(2,   weight=0,   player="Retailer",  name="Receive delay notification") 
    g.add_node(3,   weight=-4,  player="Retailer",  name="Accept") 
    g.add_node(4,   weight=-2,  player="Retailer",  name="Decline")

    g.add_node(5,   weight=0,   player="Jeans supplier",    name="Receive order")
    g.add_node(6,   weight=-2,   player="Jeans supplier",    name="Send higher qualiy jeans")
    g.add_node(7,   weight=0,   player="Jeans supplier",    name="Notify about delay")
    g.add_node(8,   weight=-4,  player="Jeans supplier",    name="Receive decline")
    g.add_node(9,   weight=4,   player="Jeans supplier",    name="Receive acceptance")
    
    g.add_edge(-1, 0)
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(2, 3)
    g.add_edge(2, 4)
    g.add_edge(1, -2)
    g.add_edge(3, -2)
    g.add_edge(4, -2)
   
    g.add_edge(-1, 5)
    g.add_edge(5, 6)
    g.add_edge(5, 7)
    g.add_edge(7, 8)
    g.add_edge(7, 9)
    g.add_edge(6, -2)
    g.add_edge(8, -2)
    g.add_edge(9, -2)

    g.add_edge(0, 5)
    g.add_edge(6, 1)
    g.add_edge(7, 2)
    g.add_edge(3, 9)
    g.add_edge(4, 8)

    return g