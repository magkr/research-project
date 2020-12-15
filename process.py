import networkx as nx

class Process():
    def __init__(self, g):
        self.g = g
        players = list(set(dict.values(nx.get_node_attributes(self.g,'player'))))
        players.remove(None)
        self.players = players
        
    def player(self, node):
        return self.g.nodes.get(node)['player']

    def none_or_player(self, node, plyer):
        return not self.player(node) or self.player(node) == plyer

    def dependencies(self, n):
        if self.g.nodes.get(n)['name'] == 'End' or self.g.nodes.get(n)['name'] == 'Start':
            return []
        return [pre for pre in self.g.predecessors(n) if self.player(pre) != self.player(n) and self.player(pre) != None] 

    def get_by_name(self, name):
        return next(n for n in self.g if self.g.nodes.get(n)['name'] == name)

    def display_graph(self):
        print("Players:", self.players)
        print("End node:", self.get_by_name('End', self.g))
        print("Dependencies:")
        for n in list(self.g):
            print(n, self.g.nodes.get(n), ":", dependencies(n, self.g))