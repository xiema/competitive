from sys import stdin,stdout
from collections import deque

n = int(stdin.readline().strip())
ints = list(map(int, stdin.readline().split()))
counts = {0:{},1:{}}

out = []
for i in range(n):
    next, opp = deque([[i]]), (ints[i]+1)%2
    seen, sol, solcount = set(), None,0
    while next:
        c = len(next)
        for _ in range(c):
            seq = next.pop()
            if sol and len(seq) > solcount:
                continue
            idx = seq[-1]
            if ints[idx]%2 == opp:
                counts[opp][idx] = 0
                _c = len(seq)
                if not sol or _c < solcount:
                    sol,solcount = seq,_c
                continue
            if idx in counts[opp]:
                if counts[opp][idx] != -1:
                    _c = len(seq) + counts[opp][idx]
                    if not sol or _c < solcount:
                        sol,solcount = seq,_c
                continue
            if idx in seen:
                continue
            seen.add(idx)
            a,b = idx+ints[idx],idx-ints[idx]
            if a >= n and b < 0:
                continue
            if a < n:
                _s = seq[:]
                _s.append(a)
                next.append(_s)
            if b >= 0:
                _s = seq[:]
                _s.append(b)
                next.append(_s)

    if sol:
        total = counts[opp][sol[-1]]
        for j in reversed(sol):
            counts[opp][j] = total
            total += 1
    else:
        for j in seen:
            counts[opp][j] = -1

    #print(i, ints[i], counts[opp][i])
    out.append(str(counts[opp][i]))




stdout.write(' '.join(list(map(str,out))))
