import re

def clauses(knowledge_base):
    """Takes the string of a knowledge base; returns an iterator for pairs
    of (head, body) for propositional definite clauses in the
    knowledge base. Atoms are returned as strings. The head is an atom
    and the body is a (possibly empty) list of atoms.

    -- Kourosh Neshatian - 2 Aug 2021

    """
    ATOM   = r"[a-z][a-zA-Z\d_]*"
    HEAD   = rf"\s*(?P<HEAD>{ATOM})\s*"
    BODY   = rf"\s*(?P<BODY>{ATOM}\s*(,\s*{ATOM}\s*)*)\s*"
    CLAUSE = rf"{HEAD}(:-{BODY})?\."
    KB     = rf"^({CLAUSE})*\s*$"

    assert re.match(KB, knowledge_base)

    for mo in re.finditer(CLAUSE, knowledge_base):
        yield mo.group('HEAD'), re.findall(ATOM, mo.group('BODY') or "")
    
def forward_deduce(kb):
    C = set()
    kb_list = list(clauses(kb))
    done = True
    i = 0
    while i < len(kb_list):
        head, b = kb_list[i]
        if b == [] and head not in C:
            C.add(head)
            i = 0
        elif set(b).issubset(C) and head not in C:
            C.add(head)
            i = 0
        else:
            i += 1
    return C
        
        
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
        return heapq.heappop(self.container)[1]
        
        #raise StopIteration   # raise this when the container is exhuasted
    

graph = ExplicitGraph(
    nodes = {'S', 'A', 'B', 'G'},
    edge_list=[('S','A',3), ('S','B',1), ('B','A',1), ('A','B',1), ('A','G',5)],
    starting_nodes = ['S'],
    goal_nodes = {'G'})

solution = next(generic_search(graph, PriorityFrontier()))
print_actions(solution)
