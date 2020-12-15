class State():
    def __init__(self, process):
        self.explored = {}
        for id in list(process.g):
            self.explored[id] = False
        self.player_paths = dict.fromkeys(process.players, [-1])
        self.current_player = self.data(next(process.g.successors(-1)), process)['player'] 

    def get_next_player(self, process):
        for p in process.players:
            if self.player_moves(p, process):
                return p
        print("No players with moves left found")
        return None
    
    def next_player(self, process):
        self.current_player = self.get_next_player(process)

    def check_dependencies(self, n, process):
        return all(self.explored[d] for d in process.dependencies(n))
        
    def player_moves(self, plyer, process):
        current = self.player_paths[plyer][-1]   # get last element in path of player
        return [nxt for nxt in process.g.successors(current) if process.none_or_player(nxt, plyer) and self.check_dependencies(nxt, process)]

    def all_moves(self, process):
        states = {}
        for p in self.players:
            states[p] = self.player_moves(p, process)
        return states
    
    def legal_moves(self, process):
        return self.player_moves(self.current_player, process)

    def make_move(self, n, process):
        if (n in self.player_moves(self.current_player, process)): 
            self.explored[n] = True
            new_path = []
            new_path.extend(self.player_paths[self.current_player]) 
            new_path.append(n)
            self.player_paths[self.current_player] = new_path
        else:
            print("Illegal move for current player")
    
    def is_finished(self, process):
        end = process.get_by_name('End')  
        return all(end in self.player_paths[p] for p in process.players)

    def data(self, n, process):
        return process.g.nodes.get(n)

    def __repr__(self):
        return "Players: " +  "\n" + "Current player: " + str(self.current_player) + "\n" + "Explored: " + str(self.explored) + "\n" + "Paths: " + str(self.player_paths)
