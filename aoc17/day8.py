from .getpuzzleinput import getpuzzleinput
from sys import argv
from collections import Counter
import re
from functools import reduce


hve = 0

def regval(target, reg):
    if target not in reg:
        reg[target] = 0
    return reg[target]


def exec(obj, reg):
    global hve
    if 'cond' in obj:
        if not exec(obj['cond'], reg):
            return
    target = regval(obj['target'], reg)
    if 'comp' in obj:
        if obj['comp'] == '!=':
            return target != obj['value']
        elif obj['comp'] == '>':
            return target > obj['value']
        elif obj['comp'] == '<':
            return target < obj['value']
        elif obj['comp'] == '>=':
            return target >= obj['value']
        elif obj['comp'] == '<=':
            return target <= obj['value']
        elif obj['comp'] == '==':
            return target == obj['value']
        return False
    elif 'op' in obj:
        if obj['op'] == 'dec':
            reg[obj['target']] = target - obj['value']
        elif obj['op'] == 'inc':
            reg[obj['target']] = target + obj['value']
        if target > hve:
            hve = target


def main():
    if len(argv) > 1:
        inp = '\n'.join(argv[1:])
    else:
        inp = getpuzzleinput(2017, 8)
    pattern = r'^([a-z]+) (dec|inc) (-?[0-9]+) if ([a-z]+) ([!><=]+) (-?[0-9]+)'
    instr_raw = [re.match(pattern, l) for l in inp.split('\n')]
    instr = [ {'target': r.group(1), 'op': r.group(2), 'value': int(r.group(3)), 'cond': { 'target': r.group(4), 'comp': r.group(5), 'value': int(r.group(6)) }} for r in instr_raw]
    reg = {}
    for i in instr:
        exec(i, reg)
    m = None
    for k, v in reg.items():
        if m is None:
            m = v
        elif m < v:
            m = v
    print(m)

def main2():
    global hve
    if len(argv) > 1:
        inp = '\n'.join(argv[1:])
    else:
        inp = getpuzzleinput(2017, 8)
    pattern = r'^([a-z]+) (dec|inc) (-?[0-9]+) if ([a-z]+) ([!><=]+) (-?[0-9]+)'
    instr_raw = [re.match(pattern, l) for l in inp.split('\n')]
    instr = [ {'target': r.group(1), 'op': r.group(2), 'value': int(r.group(3)), 'cond': { 'target': r.group(4), 'comp': r.group(5), 'value': int(r.group(6)) }} for r in instr_raw]
    reg = {}
    for i in instr:
        exec(i, reg)
    print(hve)