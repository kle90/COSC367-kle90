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
 
def atom_checker(atom_body, C):
    for atom in atom_body:
        if atom not in C:
            return False
    return True
      
def forward_deduce(knowledge_base):
    C = set()
    clause_list = list(clauses(knowledge_base))
    i = 0
    while i < len(clause_list):
        if clause_list[i][0] not in C and clause_list[i][1] == []:
            C.add(clause_list[i][0])
            i = 0
        if clause_list[i][0] not in C:
            if len(clause_list[i][1]) > 1:
                if atom_checker(clause_list[i][1], C) == True:
                    C.add(clause_list[i][0])
                    i = 0
                else: 
                    i += 1
            elif clause_list[i][1][0] in C:
                C.add(clause_list[i][0])
                i = 0    
            else:
                i += 1
        else:
            i += 1
            
        
        
    
    return C

kb = """
a :- b, c.
b :- d, e.
b :- g, e.
c :- e.
d.
e.
f :- a,
     g.
"""

print(", ".join(sorted(forward_deduce(kb))))
