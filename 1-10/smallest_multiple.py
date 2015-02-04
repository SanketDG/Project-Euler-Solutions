from fractions import gcd
from functools import reduce


def lcm(a, b):
    return a * b // gcd(a, b)

for _ in xrange(int(raw_input())):
    n = int(raw_input())
    print reduce(lcm, range(1, n + 1))
