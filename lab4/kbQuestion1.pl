hungry(X).
edible(Y).
likes(X, Y).
eats(X, Y) :- likes(X, Y).

likes(bob, chocolate).
hungry(alice).

test_answer :- eats(bob, chocolate),
               writeln('Bob eats chocolate.').