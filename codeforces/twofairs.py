from sys import stdin, stdout
from collections import deque

T = int(stdin.readline().strip())
out = []

for _ in range(T):
    n,m,a,b = stdin.readline().split()
    n,m = int(n),int(m)
    roads = {}
    for _ in range(m):
        x,y = stdin.readline().split()
        roads.setdefault(x,[]).append(y)
        roads.setdefault(y,[]).append(x)

    visited, next = set([a]), deque([(a, [])])
    counta, ignore = 0, 0

    def trace (v1):
        if v1 == a:
            return True, 0
        elif v1 == b:
            return False, 0
        visited.add(v1)
        flg, c = True, 1
        for v2 in filter(lambda x : x not in visited, roads[v1]):
            _flg,_c = trace(v2)
            flg, c = flg and _flg, c + _c
        return flg, c

    for v1 in roads[a]:
        if v1 not in visited:
            flg, c = trace(v1)
            if flg:
                counta += c
            else:
                ignore += c

    out.append("{}\n".format(counta * (n-2-counta-ignore)))

stdout.writelines(out)
