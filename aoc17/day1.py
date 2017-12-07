from .getpuzzleinput import getpuzzleinput
from sys import argv

def main():
    if len(argv) > 1:
        inp = argv[1]
    else:
        inp = getpuzzleinput(2017, 1)
    res = 0
    zero = ord('0')
    for i, c in enumerate(inp):
        ni = i + 1
        if i == len(inp) - 1:
            ni = 0
        if c == inp[ni]:
            res += ord(c) - zero
    print(res)

def main2():
    if len(argv) > 1:
        inp = argv[1]
    else:
        inp = getpuzzleinput(2017, 1)
    res = 0
    zero = ord('0')
    length = len(inp)
    step = int(length / 2)
    for i, c in enumerate(inp):
        ni = (i + step) % length
        if c == inp[ni]:
            res += ord(c) - zero
    print(res)

def dbgin():
    inp = getpuzzleinput(2017, 1)
    print(inp)