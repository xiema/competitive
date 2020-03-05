from sys import stdin,stdout
from collections import deque

n = int(stdin.readline().strip())
ints = list(map(int, stdin.readline().split()))
stk = deque([(i,(v+1)%2) for i,v in enumerate(ints)])
even,odd = {}, {}
counts = {0 : {}, 1 : {}}
while stk:
    idx, p_even = stk.popleft()
    print(idx, ints[idx], p_even)

    a,b = idx+ints[idx],idx-ints[idx]
    ca,cb = None,None
    if a < n:
        if ints[a]%2 == p_even:
            ca = 1
        elif a in counts[p_even]:
            ca = counts[p_even][a]
    else:
        ca = -1
    if b >= 0:
        if ints[b]%2 == p_even:
            cb = 1
        elif b in counts[p_even]:
            cb = counts[p_even][b]
    else:
        cb = -1

    if not ca or not cb:
        stk.append((idx, p_even))
        continue

    ans = -1
    if ca > 0 and cb > 0:
        ans = min(ca,cb) + 1
    elif ca > 0:
        ans = ca + 1
    elif cb > 0:
        ans = cb + 1

    counts[p_even][idx] = ans

out = []
for i in range(n):
    out.append(str(counts[(ints[i]+1)%2][i]))

stdout.write(' '.join(list(map(str,out))))
