tran(eins,one). 
tran(zwei,two). 
tran(drei,three). 
tran(vier,four). 
tran(fuenf,five). 
tran(sechs,six). 
tran(sieben,seven). 
tran(acht,eight). 
tran(neun,nine).

listtran([], []).
listtran(G, X) :- G = [H|Y], tran(H, X), listtran(Y, X).
listtran(X, E) :- E = [H|Y], tran(X, H), listtran(Y, X).  

test_answer :-
    listtran([eins, neun, zwei], X),
    writeln(X).