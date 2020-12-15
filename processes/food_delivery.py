import networkx as nx

# Expected output for 3=-10, 4=30, 5=15, 6=20, 9=20, 11=5 14=10, 19=-10, 20=-5, 24=30, 25=-20, 26=30
# Supplier:			30 		{15, 16, 18, 22, 24}
# Manufacturer:		30		{0, 1, 3, 6, 7, 8, 9}


def food_delivery(aligned):
    g = nx.DiGraph()
    g.add_node(-1,  weight=0,    player=None,            name="Start")
    g.add_node(-2,  weight=0,    player=None,            name="End")

    g.add_node(0,   weight=0,    player="Deliverer",  name="Receive order")
    g.add_node(1,   weight=0,    player="Deliverer",  name="Accept order") 
    g.add_node(4,   weight=0,    player="Deliverer",  name="Reject order") 
    
    g.add_node(5,  weight=0,   player="Restaurant",    name="Order food delivery")
    g.add_node(6,   weight=0,   player="Restaurant",    name="Receive acceptance")
    g.add_node(9,   weight=0,   player="Restaurant",    name="Receive rejection")
    g.add_node(10,   weight=0,   player="Restaurant",    name="Decline order")
    
    if aligned:
        g.add_node(2,   weight=-5,   player="Deliverer",  name="Make delivery") 
        g.add_node(3,   weight=10,   player="Deliverer",  name="Recive payment") 
    
        g.add_node(7,   weight=-10, player="Restaurant",    name="Pay for delivery")
        g.add_node(8,   weight=50,  player="Restaurant",    name="Receive payment for food")
    else:
        g.add_node(2,   weight=-10,   player="Deliverer",  name="Make delivery") 
        g.add_node(3,   weight=8,   player="Deliverer",  name="Recive payment") 
    
        g.add_node(7,   weight=-8, player="Restaurant",    name="Pay for delivery")
        g.add_node(8,   weight=50,  player="Restaurant",    name="Receive payment for food")

    g.add_edge(-1, 0)
    g.add_edge(0, 1)
    g.add_edge(0, 4)
    g.add_edge(1, 2)
    g.add_edge(2, 3)
    g.add_edge(3, -2)
    g.add_edge(4, -2)

    g.add_edge(-1, 5)
    g.add_edge(5, 9)
    g.add_edge(9, 10)
    g.add_edge(5, 6)
    g.add_edge(6, 7)
    g.add_edge(7, 8)
    g.add_edge(10, -2)
    g.add_edge(8, -2)

    g.add_edge(5, 0)
    g.add_edge(1, 6)
    g.add_edge(4, 9)
    g.add_edge(7, 3)

    return g