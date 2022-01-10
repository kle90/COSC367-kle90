from search import *
import statistics
import heapq

class PriorityFrontier(Frontier):
    

    def __init__(self):
        # The constructor does not take any arguments.
        self.container = []
        heapq.heapify(self.container)        
        # Complete the rest
        

    def add(self, path):
        cost = 0
        for arc in path:
            cost == arc.cost
        heapq.heappush(self.container, (cost, path))
        
        #raise NotImplementedError # FIX THIS: Replace it with proper code

    def __iter__(self):
        """The object returns itself because it is implementing a __next__
        method and does not need any additional information for iteration."""
        return self
        
    def __next__(self):
        # Complete
        if len(self.container) > 0:
            return heapq.heappop(self.container)[1]
        else:
            raise StopIteration   # raise this when the container is exhuasted
    

graph = ExplicitGraph(
    nodes = {'S', 'A', 'B', 'G'},
    edge_list=[('S','A',3), ('S','B',1), ('B','A',1), ('A','B',1), ('A','G',5)],
    starting_nodes = ['S'],
    goal_nodes = {'G'})

solution = next(generic_search(graph, PriorityFrontier()))
print_actions(solution)