"""Lab 6 Questions 5 and 6"""

# Question 5

from csp import Relation

relations = [
    Relation(header=['a', 'b', 'c'],
             tuples={(2, 1, 0),
                    (2, 0, 1),
                    (2, 0, 0),
                    (1, 0, 0)}),
    
    Relation(header=['c', 'd'],
             tuples={(2, 1),
                    (2, 0),
                    (1, 0)})
]

print(sorted(sorted(relations)[0].tuples))

# Question 6 

from csp import Relation

relations = [
    Relation(header=['a', 'b'],
        tuples={(1, -1),
               (0, 0),
               (1, 1)}),
    
    Relation(header=['c', 'd'],
        tuples={(1, -1),
               (0, -1),
               (1, 0)}),
    
    Relation(header=['a', 'b', 'c'],
        tuples={(1, 1, -1),
                (-1, -1, -1)})    
      ] 

relations_after_elimination = [
    Relation(header=['c', 'd'],
        tuples={(1, -1),
               (0, -1),
               (1, 0)}),
    
    Relation(header=['b', 'c'],
        tuples={(1, -1)})    
    ### COMPLETE ###
    ] 

print(len(relations))
print(all(type(r) is Relation for r in relations))

print(sorted(sorted(relations)[1].tuples))
