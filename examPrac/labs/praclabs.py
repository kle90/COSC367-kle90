from search import *
from collections import deque
import copy


class DFSFrontier(Frontier):
    def __init__(self):
        self.container = []
        
    def add(self, path):
        """Adds a new path to the frontier. A path is a sequence (tuple) of
        Arc objects. You should override this method."""
        self.container.append(path)

        
    def __iter__(self):
        """We don't need a separate iterator object. Just return self. You
        don't need to change this method."""
        return self

    def __next__(self):
        """Selects, removes, and returns a path on the frontier if there is
        any.Recall that a path is a sequence (tuple) of Arc
        objects. Override this method to achieve a desired search
        strategy. If there nothing to return this should raise a
        StopIteration exception."""
        
        if len(self.container) > 0:
            return self.container.pop()
        else:
            raise StopIteration
        
class BFSFrontier(Frontier):
    def __init__(self):
        self.container = deque()
    
    def add(self, path):
        """Adds a new path to the frontier. A path is a sequence (tuple) of
        Arc objects. You should override this method."""
        print("+{}".format(path))
        self.container.append(path)

        
    def __iter__(self):
        """We don't need a separate iterator object. Just return self. You
        don't need to change this method."""
        return self

    def __next__(self):
        """Selects, removes, and returns a path on the frontier if there is
        any.Recall that a path is a sequence (tuple) of Arc
        objects. Override this method to achieve a desired search
        strategy. If there nothing to return this should raise a
        StopIteration exception."""
        
        if len(self.container) > 0:
            x = self.container.popleft()
            print("-{}".format(x))            
            return x
        else:
            raise StopIteration    
        
class FunkyNumericGraph(Graph):
    def __init__(self, input_node):
        self.starting_node = input_node
        
    
    def is_goal(self, node):
        """Returns true if the given node is a goal state, false otherwise."""
        if node % 10 == 0:
            return True

    def starting_nodes(self):
        """Returns a sequence of starting nodes. Often there is only one
        starting node but even then the function returns a sequence
        with one element. It can be implemented as an iterator if
        needed."""
        return [self.starting_node]
        

    def outgoing_arcs(self, tail_node):
        """Given a node it returns a sequence of arcs (Arc objects)
        which correspond to the actions that can be taken in that
        state (node)."""
        
        arc1 = Arc(tail_node, tail_node-1, action="1down", cost=1)
        arc2 = Arc(tail_node, tail_node + 2, action="2up", cost=1)
        return [arc1, arc2] 
        
    def estimated_cost_to_goal(self, node):
        """Return the estimated cost to a goal node from the given
        state. This function is usually implemented when there is a
        single goal state. The function is used as a heuristic in
        search. The implementation should make sure that the heuristic
        meets the required criteria for heuristics."""

        raise NotImplementedError    

BLANK = ' '

class SlidingPuzzleGraph(Graph):
    """Objects of this type represent (n squared minus one)-puzzles.
    """

    def __init__(self, starting_state):
        self.starting_state = starting_state

    def outgoing_arcs(self, state):
        """Given a puzzle state (node) returns a list of arcs. Each arc
        represents a possible action (move) and the resulting state."""
        
        n = len(state) # the size of the puzzle
        i, j = next((i, j) for i in range(n) for j in range(n)
                    if state[i][j] == BLANK) # find the blank tile
        arcs = []
        if i > 0:
            action = "Move {} down".format(state[i-1][j]) # or blank goes up
            new_state = copy.deepcopy(state) 
            new_state[i][j], new_state[i-1][j] = new_state[i-1][j], BLANK
            arcs.append(Arc(state, new_state, action, 1))
        if i < n - 1:
            action = "Move {} up".format(state[i+1][j]) # or blank goes down
            new_state = copy.deepcopy(state) 
            new_state[i][j], new_state[i+1][j] = new_state[i+1][j], BLANK
            arcs.append(Arc(state, new_state, action, 1))
        if j > 0:
            action = "Move {} right".format(state[i][j-1]) # or blank goes left
            new_state = copy.deepcopy(state) 
            new_state[i][j], new_state[i][j-1] = new_state[i][j-1], BLANK
            arcs.append(Arc(state, new_state, action, 1))
        if j < n - 1:
            pass
            # COMPLETE (repeat the same pattern with some modifications)
        return arcs

    def starting_nodes(self):
        return [self.starting_state]
    
    def is_goal(self, state):
        """Returns true if the given state is the goal state, False
        otherwise. There is only one goal state in this problem."""
        
        n = len(state)
        # COMPLETE
        
def max_value(tree):
    if type(tree) == int:
        return tree
    new_list = []
    for node in tree:
        new_list.append(min_value(node))
    
    return max(new_list)
    
def min_value(tree):
    if type(tree) == int:
        return tree
    new_list = []
    for node in tree:
        new_list.append(max_value(node))
    
    return min(new_list)

def max_action_value(game_tree):
    pass

def min_action_value(game_tree):
    pass

import itertools, copy 
from csp import *

import itertools, copy 
from csp import *

def arc_consistent(csp):
    csp = copy.deepcopy(csp)
    to_do = {(x, c) for c in csp.constraints for x in scope(c)} # COMPLETE
    while to_do:
        x, c = to_do.pop()
        ys = scope(c) - {x}
        new_domain = set()
        for xval in csp.var_domains[x]: # COMPLETE
            assignment = {x: xval}
            for yvals in itertools.product(*[csp.var_domains[y] for y in ys]):
                assignment.update({y: yval for y, yval in zip(ys, yvals)})
                if satisfies(assignment, c): # COMPLETE
                    new_domain.add(xval) # COMPLETE
                    break
        if csp.var_domains[x] != new_domain:
            for cprime in set(csp.constraints) - {c}:
                if x in scope(cprime):
                    for z in scope(cprime): # COMPLETE
                       if x != z:
                           to_do.add((z, cprime))
            csp.var_domains[x] = new_domain     #COMPLETE
    return csp

def select(population, error, max_error, r):
    roulette_list = []
    total = 0
    for individual in population:
        total += (max_error - error(individual))
        roulette_list.append(total)

    for tup in enumerate(roulette_list):
        if total * r < tup[1]:
            return population[tup[0]]

def main():
    graph = ExplicitGraph(
                nodes={'A', 'B', 'C', 'D'},
                edge_list=[('B', 'A'), ('C', 'D'), ('A','D'), ('C','A')],
                starting_nodes=['C'],
                goal_nodes={'B'},
                )

    solutions = generic_search(graph, BFSFrontier())
    solution = next(solutions, None)
    print_actions(solution)
    
if __name__ == "__main__":
    main()