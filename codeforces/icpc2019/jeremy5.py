from sys import stdin, stdout
from collections import deque

out = []
T = int(stdin.readline())

for _ in range(T):
    k = int(stdin.readline())
    k2 = 2*k
    houses, sizes, paired = {}, {}, {}
    root = None
    for _ in range(k2-1):
        a,b,t = stdin.readline().split()
        t = int(t)
        if a not in houses:
            root = a
            houses[a] = [(b,t)]
            sizes[a] = 1
            paired[a] = False
        else:
            houses[a].append((b,t))
        if b not in houses:
            root = b
            houses[b] = [(a,t)]
            sizes[b] = 1
            paired[b] = False
        else:
            houses[b].append((a,t))

    houselist, q = deque(), deque([root])
    c = 1
    while c < k2:
        h1 = q.popleft()
        for (h2,t) in houses[h1]:
            if h2 != h1:
                houselist.appendleft((h2, h1, t))
                q.append(h2)
                c += 1

    tmax, tmin = 0, 0
    for (h2, h1, t) in houselist:
        tmax += min(sizes[h2], k2-sizes[h2]) * t
        sizes[h1] += sizes[h2]
        if not paired[h2]:
            paired[h1] = not paired[h1]
            tmin += t

    out.append("{} {}\n".format(tmin, tmax))

stdout.writelines(out)
