from .getpuzzleinput import getpuzzleinput
from sys import argv
from collections import Counter

def main():
    if len(argv) > 1:
        inp = '\n'.join(argv[1:])
    else:
        inp = getpuzzleinput(2017, 5)
    code = [int(a) for a in inp.split('\n')]
    pc = 0
    steps = 0
    while pc in range(len(code)):
    	off = code[pc]
    	code[pc] += 1
    	pc += off
    	steps += 1
    print(steps)


def main2():
    if len(argv) > 1:
        inp = '\n'.join(argv[1:])
    else:
        inp = getpuzzleinput(2017, 5)
    code = [int(a) for a in inp.split('\n')]
    pc = 0
    steps = 0
    while pc in range(len(code)):
    	off = code[pc]
    	if (code[pc] >= 3):
    		code[pc] -= 1
    	else:
    		code[pc] += 1
    	pc += off
    	steps += 1
    print(steps)