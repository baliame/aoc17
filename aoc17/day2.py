from .getpuzzleinput import getpuzzleinput
from sys import argv

def main():
    if len(argv) > 1:
        inp = argv[1]
    else:
        inp = getpuzzleinput(2017, 2)
    rows = inp.split('\n')
    res = 0
    for row in rows:
        data = row.split('\t')
        minval = 0
        maxval = -1
        for valstr in data:
            val = int(valstr)
            if maxval < minval:
                minval = val
                maxval = val
            else:
                if val > maxval:
                    maxval = val
                elif val < minval:
                    minval = val
        res += maxval - minval
    print(res)

def main2():
    if len(argv) > 1:
        inp = argv[1]
    else:
        inp = getpuzzleinput(2017, 2)
    rows = inp.split('\n')
    res = 0
    for row in rows:
        data = [int(valstr) for valstr in row.split('\t')]
        dlen = len(data)
        for i in range(dlen):
            done = False
            for j in range(i+1, dlen):
                x = data[i]
                y = data[j]
                if x%y == 0:
                    res += int(x / y)
                    done = True
                    break
                elif y%x == 0:
                    res += int(y / x)
                    done = True
                    break
            if done:
                break
    print(res)