n2lr(N, L) :-
	O is (N mod 10),
	(
		N >= 10, R is N // 10, n2lr(R, S), L = [O|S], !;
		L = [O]
	).

n2l(N, L) :-
	n2lr(N, RL),
	reverse(RL, L).

sumof([X, X|L], A, B) :- sumof([X|L], A, C), B is C + X, !.
sumof([_, Y|L], A, B) :- sumof([Y|L], A, B).
sumof([A], A, A) :- !.
sumof([_], _, 0).

day1(N, B) :-
	n2l(N, L),
	L = [A|_],
	sumof(L, A, B).

countlist([_|L], N) :- countlist(L, M), N is M + 1.
countlist([], 0).

splitlist(L, L1, L2) :-
	countlist(L, N),
	splitlist(L, L1, L2, N // 2).

splitlist(L, _, L, 0) :- !.
splitlist([X|L], [X], L, 1) :- !.
splitlist([X|L], [X|L1], L2, N) :- M is N - 1, splitlist(L, L1, L2, M), !.

sumofb([X|L1], [X|L2], B) :- sumofb(L1, L2, C), B is C + (2 * X), !.
sumofb([_|L1], [_|L2], B) :- sumofb(L1, L2, B).
sumofb([], [], 0).

day1b(N, B) :-
	n2l(N, L),
	splitlist(L, L1, L2),
	sumofb(L1, L2, B).