from .getpuzzleinput import getpuzzleinput
from sys import argv
from collections import Counter
import re
from functools import reduce

def main():
    if len(argv) > 1:
        inp = '\n'.join(argv[1:])
    else:
        inp = getpuzzleinput(2017, 7)
    pattern = r'^([a-z]+) \(([0-9]+)\) -> (.+)$'
    progdefs = [re.match(pattern, p) for p in inp.split('\n') if re.match(pattern, p)]
    progs = {}
    for pdef in progdefs:
        name = pdef.group(1)
        weight = pdef.group(2)
        children = pdef.group(3).split(', ')
        progs[name] = {
            'name': name,
            'weight': weight,
            'children': children,
        }
    copy = progs.copy()
    for name, obj in copy.items():
        for elem in obj['children']:
            if elem in progs:
                del progs[elem]
    for name, obj in progs.items():
        print(name)

def sumrec(base, progs):
    wts = []
    if len(base['children']) == 0:
        return base['weight']
    for item in base['children']:
        wts.append(sumrec(progs[item], progs) + base['weight'])
    res = reduce((lambda x, y: x + y), wts)
    i = wts[0]
    for item in wts:
        if item != i:
            print(base['name'] + ': {0}'.format(wts))
            break
    return res

def main2():
    if len(argv) > 1:
        inp = '\n'.join(argv[1:])
    else:
        inp = getpuzzleinput(2017, 7)
    pattern = r'^([a-z]+) \(([0-9]+)\) -> (.+)$'
    cpattern = r'^([a-z]+) \(([0-9]+)\)$'
    isplit = inp.split('\n')
    progdefs = [re.match(pattern, p) for p in isplit if re.match(pattern, p)]
    cdefs = [re.match(cpattern, p) for p in isplit if re.match(cpattern, p)]
    progs = {}
    for pdef in cdefs:
        name = pdef.group(1)
        weight = pdef.group(2)
        children = []
        progs[name] = {
            'name': name,
            'weight': int(weight),
            'children': children,
            'parent': None,
            'balanced': True
        }
    for pdef in progdefs:
        name = pdef.group(1)
        weight = pdef.group(2)
        children = pdef.group(3).split(', ')
        progs[name] = {
            'name': name,
            'weight': int(weight),
            'children': children,
            'parent': None,
            'balanced': False
        }
    for name, prog in progs.items():
        for child in prog['children']:
            progs[child]['parent'] = name
    root = None
    for name, prog in progs.items():
        if prog['parent'] is None:
            root = prog
            break
    sumrec(root, progs)