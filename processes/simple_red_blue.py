import networkx as nx

# Expected output for: 2=100, 4=1, 5=100, 7=50
# Blue:     50      {0, 7, 3}
# Red:      100     {5}

# Expected output for: 2=100, 4=1, 5=0, 7=50        Changed 5=0
# Blue:     100     {0, 1, 2, 3}
# Red:      1       {4}

# Expected output for: 2=100, 4=0, 5=0, 7=50        Red doesn't care, but chooses best path for Blue
# Blue:     100     {0, 1, 2, 3}
# Red:      0       {4}

# Expected output for: 4=20                         Blue doesn't care, but chooses best path for Red (I have also tried changing the index of E and F)
# Blue:     0           {0, 1, 2, 3}
# Red:      20          {4}

def simple_red_blue():
    g = nx.DiGraph()
    g.add_node(-1, name="Start", player=None, weight=0)
    g.add_node(-2, name="End", player=None, weight=0) 

    g.add_node(0, name="A", player="Blue", weight=0)
    g.add_node(1, name="B", player="Blue", weight=0)
    g.add_node(2, name="C", player="Blue", weight=0)
    g.add_node(3, name="D", player="Blue", weight=0)
    g.add_node(4, name="E", player="Red", weight=20)
    g.add_node(5, name="F", player="Red", weight=0)
    g.add_node(6, name="G", player="Blue", weight=0)
    g.add_node(7, name="H", player="Blue", weight=0)
    g.add_edge(-1, 0)
    g.add_edge(-1, 4)
    g.add_edge(-1, 5)
    g.add_edge(0, 1)
    g.add_edge(0, 7)
    g.add_edge(1, 2)
    g.add_edge(1, 4)
    g.add_edge(1, 6)
    g.add_edge(7, 3)
    g.add_edge(2, 3)
    g.add_edge(6, 3)
    g.add_edge(4, 2)
    g.add_edge(5, 6)
    g.add_edge(3, -2)
    g.add_edge(4, -2)
    g.add_edge(5, -2)
    return g