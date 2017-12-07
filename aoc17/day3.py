from sys import argv
from math import sqrt

# Let input be y = x-1
# It. count: 2, 4, 6, 8...
# Half it count: 1, 2, 3, 4...
# Sum of integer series 1->n: f(n) = n(n+1) / 2
# We're looking for n where f(n) > y/2 and f(n-1) < y/2
# 1) f(n) = n(n+1) / 2 > y/2
# 1) 2f(n) = n(n+1) > y
# 2) f(n-1) = n(n-1) / 2 < y/2
# 2) 2f(n-1) = n(n-1) < y
# Combined: n(n-1) <= y < n(n+1)
# Consider eq. 1: n(n-1) <= y
# n(n-1) - y <= 0
# n^2 - n - y <= 0
# The two solutions of the quadratic equation will give the range in which the equation is lesser than or equal to 0 as a(=1) is positive
# Within this range of n, the equation is satisfied.
# n and y can only be an integer
# We only need one equation to calculate n
# 1) n^2 - n - y = 0
# D = 1 - (4 * -y) = 1 + 4y
# n1,2 = (-1 +/- sqrt(1+4y)) / 2
# n1 = (1 - sqrt(1 + 4y)) / 2 -> can't be the solution, is always negative for y>0 integers
# n2 = (1 + sqrt(1 + 4y)) / 2 -> thus this is the one we're uding
# n = int(n2)
# Examples: f(n) values can be 0, 1, 3, 6, 10, 15...
# For y=1, f(n-1) should be 1 and f(n) should be 3. n2 = (1 + sqrt(5))/2 < 2 > 1; n = int(1 < n2 < 2) = 1
# For y=2, f(n-1) should be 1 and f(n) should be 3. n2 = (1 + sqrt(9) / 2) = 2 = n
# For y=3, f(n-1) should be 3 and f(n) should be 6. (n-1 = 2, n = 3) n2 = (1 + sqrt(12) / 2) < 3 > 2, n = int(2 <n2 < 3) = 2
# 5: (1 + sqrt(21)) / 2 ~ (1 + 4)/2 -> 2 = n
# 6: (1 + sqrt(25)) / 2 = (1 + 5)/2 -> 3 = n

# FOR y  : 0  1  2  3  4  5  6  7  8  9
# EXP n  : 1  1  2  2  2  2  3  3  3  3
# EXP n-1: 0  0  1  1  1  1  2  2  2  2
# ACT    : 1  1  2  2  2  2  3  3  3  3

# Each cycle is a movement on the x then y axis. Odd cycles (1,3,5) move us in +x/-y directions, even cycles move us in -x/+y directions.
# Each cycle takes a total movement of 2*cycle ID. First, cycle ID number of steps are taken in the x direction, then the same in the y direction.
# This means that in cycle 1 we move 1 towards +x, 1 towards -y, then in cycle 2 -2 towards +x (or 2 towards -x), and 2 towards +y.
# At the end of each cycle we are on a point on the x=-y line.

# The reason we calculate n is to find the cycle we need to figure out. It's simple: n is the amount of cycles for us to *pass* x.
# n-1 is the amount of cycles that will be fully executed.
# x is the number of the field to reach. y = x-1 above is the number of steps to take from 1 to reach x.

# Odd cycles, we increment the absolute value of x and y by one. Every cycle inverts the sign of x and y.
# x is negative on even cycles. y is negative on odd cycles.
# After cycle 1, we are at +1,-1, after cycle 2, -1,+1, after cycle 3, +2,-2.
# Algorithm for calculating our position after m = n-1 cycles:
# x0 = (m % 2 ?  1: -1) * int(m/2 + 0.5) Values for 1,2,3...:  1 * int(1) =  1, -1 * int(1.5) = -1,  1 * int(2) =  2...
# y0 = (m % 2 ? -1:  1) * int(m/2 + 0.5) Values for 1,2,3...: -1 * int(1) = -1,  1 * int(1.5) =  1, -1 * int(2) = -2...
# x0, y0 is our starting point

# From here we've already taken m(m+1) = n(n-1) steps. We need to take y - n(n-1) = k steps.
# The first n steps in the nth cycle are x-steps. The number of x-steps is min(n, k).
# The second n steps in the nth cycle are y-steps. The number of y-steps is max(0, k-n).
# The direction of x-steps is -1 on even cycles, 1 on odd cycles. y is inverse.
# The final xt, yt coordinates are: xt = x0 + (n % 2 ?  1 : -1) * min(n, k); yt = y0 + (n % 2 ? -1 : 1) * max(0, k-n)

def calc_pos(x, debug=False):
    y = x - 1
    n = int((1 + sqrt(4 * y)) / 2)
    m = max(n - 1, 0)
    k = y - n*(n-1)
    xms = 1 if m % 2 else -1
    yms = -xms
    xns = yms
    yns = xms
    dist = int(m/2 + 0.5)
    x0 = xms * dist
    y0 = yms * dist
    xsteps = xns * min(n, k)
    ysteps = yns * max(0, k-n)
    if debug:
        print('x = {0}; y = {1} -> m = {2}, n = {3}'.format(x,y,m,n))
        print('dist = {0}, x0 = {1}, y0 = {2}'.format(dist, x0, y0))
        print('n(n-1) = {0}, k = {1}, xms = {4}, yms = {5}, xns = {2}, yns = {3}'.format(n*(n-1), k, xns, yns, xms, yms))
    return (x0 + xsteps, y0 + ysteps)

def calc_dbg():
    if len(argv) > 1:
        inp = argv[1]
    else:
        raise RuntimeError('No downloadable input. Provide manually.')
    print(calc_pos(int(inp), debug=True))

def main():
    if len(argv) > 1:
        inp = argv[1]
    else:
        raise RuntimeError('No downloadable input. Provide manually.')
    x, y = calc_pos(int(inp))
    print(abs(x) + abs(y))

def stupid_bullshit(x):
    order = ((1,0),(0,-1),(-1,0),(0,1))
    spiral = {0: {0: 1}}
    c_order = 0
    c_steps = 1
    cx = 0
    cy = 0
    while True:
        sx, sy = order[c_order % 4]
        steps = int(c_steps)
        for i in range(steps):
            cx += sx
            cy += sy
            res = 0
            for dx in range(-1, 2):
                for dy in range(-1, 2):
                    if dx == 0 and dy == 0:
                        continue
                    chkx = cx + dx
                    chky = cy + dy
                    if chkx not in spiral or chky not in spiral[chkx]:
                        continue
                    res += spiral[chkx][chky]
            if cx not in spiral:
                spiral[cx] = {}
            spiral[cx][cy] = res
            if res > x:
                return res
        c_order += 1
        c_steps += 0.5

def main2():
    if len(argv) > 1:
        inp = argv[1]
    else:
        raise RuntimeError('No downloadable input. Provide manually.')
    print(stupid_bullshit(int(inp)))