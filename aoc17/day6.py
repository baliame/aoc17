from .getpuzzleinput import getpuzzleinput
from sys import argv
from collections import Counter

def main():
    if len(argv) > 1:
        inp = '\n'.join(argv[1:])
    else:
        inp = getpuzzleinput(2017, 6)
    stacks = [int(a) for a in inp.split('\t')]
    states = []
    steps = 0
    while stacks not in states:
        states.append(stacks[:])
        maxv = 0
        maxi = -1
        for i in range(len(stacks)):
            if stacks[i] > maxv:
                maxv = stacks[i]
                maxi = i
        stacks[maxi] = 0
        maxi = (maxi + 1) % len(stacks)
        for e in range(maxv):
            stacks[maxi] += 1
            maxi = (maxi + 1) % len(stacks)
        steps += 1
    print(steps)


def main2():
    if len(argv) > 1:
        inp = '\n'.join(argv[1:])
    else:
        inp = getpuzzleinput(2017, 6)
    stacks = [int(a) for a in inp.split('\t')]
    states = []
    steps = 0
    while stacks not in states:
        states.append(stacks[:])
        maxv = 0
        maxi = -1
        for i in range(len(stacks)):
            if stacks[i] > maxv:
                maxv = stacks[i]
                maxi = i
        stacks[maxi] = 0
        maxi = (maxi + 1) % len(stacks)
        for e in range(maxv):
            stacks[maxi] += 1
            maxi = (maxi + 1) % len(stacks)
        steps += 1
    print(steps - states.index(stacks))
