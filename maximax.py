from time import time
import copy
import sys
from state import State
from process import Process
from processes.very_simple import very_simple
from processes.simple_red_blue import simple_red_blue
from processes.simple_application import simple_application
from processes.supply_chain import supply_chain
from processes.adv_supply_chain import adv_supply_chain
from processes.binary import binary
from processes.food_delivery import food_delivery
from processes.jeans_retailer import jeans_retailer

states = 0
process = None

def utility(state):
    sums = {}
    for p in process.players:
        sum = 0
        for n in state.player_paths[p]:
            sum += state.data(n, process)['weight']
        sums[p] = sum
    return sums

def maximax(s): 
    global states 
    if s.is_finished(process): 
        return utility(s), s.player_paths 
    
    moves = s.player_moves(s.current_player, process)
    
    if not moves: # moves is empty so change player
        s.next_player(process)
        return maximax(s)

    v = -sys.maxsize
    best_values = {}
    best_paths = {}

    for m in moves:
        states += 1
        new_s = copy.deepcopy(s)
        new_s.make_move(m, process)

        values, paths = maximax(new_s)
        
        if(values[s.current_player] > v):
            v = values[s.current_player]
            best_values = values
            best_paths = paths

    return best_values, best_paths

def set_process(pr):
    global process
    process = pr

def test():
    global states
    depth = 1
    while depth <= 20:
        g = binary(depth)
        set_process(Process(g))
        sta = State(process)
        print()
        print("----------- Test with depth", depth, "------------")
        start = time()
        values, paths = maximax(sta)
        end = time()
        print("nodes:", 2**depth)
        print("states:", states)
        print("time elapsed:", end - start)

        states = 0
        depth += 1

def main(arg):
    if(arg == "test"):
        test()
        return
    global process
    g = {
        'very_simple': very_simple(),
        'simple_red_blue' : simple_red_blue(),
        'simple_application' : simple_application(),
        # binary test
        'binary': binary(10),
        # examples
        'adv_supply_chain' : adv_supply_chain(),
        'food_delivery_aligned' : food_delivery(True),
        'food_delivery_misaligned' :  food_delivery(False),
        'supply_chain_aligned' : supply_chain(True),
        'supply_chain_misaligned' : supply_chain(False),
        'jeans_retailer': jeans_retailer()
    }.get(arg)

    process = Process(g)
    sta = State(process)

    start = time()
    utilities, paths = maximax(sta)
    end = time()
    
    print(utilities, paths, "\n")
    print("states:", states)
    print("time elapsed:", end - start)

if __name__ == "__main__":
    arg = "adv_supply_chain"
    if sys.argv[1:]:
        arg = sys.argv[1:][0]

    print("\nRUNNING MAXIMAXI ON:", arg)
    main(arg)
