from .getpuzzleinput import getpuzzleinput
from sys import argv
from collections import Counter

def main():
    if len(argv) > 1:
        inp = argv[1]
    else:
        inp = getpuzzleinput(2017, 4)
    rows = inp.split('\n')
    res = 0
    for row in rows:
        words = row.split(' ')
        mc = Counter(words).most_common(1)[0]
        if (mc[1]) == 1:
            res += 1
    print(res)

def main2():
    if len(argv) > 1:
        inp = argv[1]
    else:
        inp = getpuzzleinput(2017, 4)
    rows = inp.split('\n')
    res = 0
    for row in rows:
        bad = False
        words = [Counter(a) for a in row.split(' ')]
        for i in range(len(words)):
            for j in range(i+1, len(words)):
                if words[i] == words[j]:
                    bad = True
                    break
            if bad:
                break
        if not bad:
            res += 1
    print(res)