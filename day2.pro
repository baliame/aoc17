minmaxlist([], 0, 0).
minmaxlist([H|T], Min, Max) :-
	minmaxlist(T, PMin, PMax),
	(
		H > PMax, Min is PMin, Max is H, !;
		(H < PMin, !; PMin is 0), Min is H, Max is PMax, !;
		Min is PMin, Max is PMax
	).
