import networkx as nx

# Expected outcome
# Fond:          0      {0, 1} 
# University'   -10     {3, 4}

def simple_application():
    g = nx.DiGraph()
    g.add_node(-1, name="Start", player=None, weight=0)
    g.add_node(-2, name="End", player=None, weight=0) 

    g.add_node(0, name="Receive application", player="Fond", weight=0)
    g.add_node(1, name="Decline", player="Fond", weight=0)
    g.add_node(2, name="Accept and pay", player="Fond", weight=-80)
    g.add_node(3, name="Send application", player="University", weight=-10)
    g.add_node(4, name="Receive notification", player="University", weight=0)
    g.add_node(5, name="Receive payment", player="University", weight=80)
    g.add_edge(-1, 0)
    g.add_edge(-1, 3)
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 4)
    g.add_edge(2, 5)
    g.add_edge(3, 4)
    g.add_edge(3, 5)
    g.add_edge(3, 0)
    g.add_edge(1, -2)
    g.add_edge(2, -2)
    g.add_edge(4, -2)
    g.add_edge(5, -2)
    return g