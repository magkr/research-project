import networkx as nx

# Expected output:
# Upper:    0   {0, 1}
# Lower:    0   {2}

def very_simple():
    g = nx.DiGraph()
    g.add_node(-1, name="Start", player=None, weight=0)
    g.add_node(-2, name="End", player=None, weight=0) 
    g.add_node(0, name="A", player="Upper", weight=0)
    g.add_node(1, name="B", player="Upper", weight=0)
    g.add_node(2, name="C", player="Lower", weight=0)
    g.add_edge(-1, 0)
    g.add_edge(-1, 2)
    g.add_edge(0, 1)
    g.add_edge(2, 1)
    g.add_edge(2, -2)
    g.add_edge(1, -2)
    return g