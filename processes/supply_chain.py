import networkx as nx

# Expected output for 4=30
# Supplier:			40 		{1, 2, 7, 9, 12}
# Manufacturer:		30		{0, 3, 4, 10, 11, 13, 14}

# Expected output for 4=0
# Supplier:			30 		{1, 6, 15, 9, 12}
# Manufacturer:		0		{0, 16, 10, 11, 13, 14}


def supply_chain(aligned):
    g = nx.DiGraph()
    g.add_node(-1,  weight=0,    player=None,            name="Start")
    g.add_node(-2,  weight=0,    player=None,            name="End")

    g.add_node(0,   weight=0,    player="Manufacturer",  name="Make order")
    g.add_node(3,   weight=0,    player="Manufacturer",  name="Receive on time")
    g.add_node(2,   weight=-25,  player="Manufacturer",  name="Loss from delay")
    g.add_node(4,   weight=-45,  player="Manufacturer",  name="Pay")
    g.add_node(5,   weight=50,   player="Manufacturer",  name="Sell")

    g.add_node(6,   weight=0,      player="Supplier",      name="Accept order")
    g.add_node(9,   weight=0,      player="Supplier",      name="Send on time")
    g.add_node(7,   weight=-30,    player="Supplier",      name="Produce")
    g.add_node(8,   weight=-10,    player="Supplier",      name="Increase capacity")
    g.add_node(10,  weight=-8,     player="Supplier",      name="Send delayed")
    g.add_node(11,  weight=45,     player="Supplier",      name="Receive payment")

    if aligned:
        g.add_node(1,   weight=16,   player="Manufacturer",  name="Receive delayed")
        g.add_node(10,  weight=-16,    player="Supplier",      name="Send delayed")
    else:
        g.add_node(1,   weight=8,   player="Manufacturer",  name="Receive delayed")
        g.add_node(10,  weight=-8,    player="Supplier",      name="Send delayed")

    g.add_edge(-1, 0)
    g.add_edge(0, 1)
    g.add_edge(1, 2)
    g.add_edge(2, 4)
    g.add_edge(0, 3)
    g.add_edge(3, 4)
    g.add_edge(4, 5)
    g.add_edge(5, -2)

    g.add_edge(-1, 6)
    g.add_edge(6, 7)
    g.add_edge(7, 8)
    g.add_edge(8, 9)
    g.add_edge(9, 11)
    g.add_edge(7, 10)
    g.add_edge(10, 11)
    g.add_edge(11, -2)

    g.add_edge(0, 6)
    g.add_edge(9, 3)
    g.add_edge(10, 1)
    g.add_edge(4, 11)

    return g