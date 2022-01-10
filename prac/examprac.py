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
    kb_clause = list(clauses(kb))
    c = set()
    fin = False
    count = 0
    while not fin:
        for head, tail in kb_clause:         
            if tail == [] and head not in c:
                c.add(head)
                count = 0
              
            elif head not in c:    
                if set(tail).issubset(c):
                    c.add(head)
                    count = 0                    
            count += 1            
        
        if count == len(kb_clause):
            fin = True
    
    return c
                
        

def main():
    kb = """
    a.
    z.
    """
    print(", ".join(sorted(forward_deduce(kb))))
    

if __name__ == "__main__":
    main()