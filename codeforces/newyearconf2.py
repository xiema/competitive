from sys import stdin, stdout
from collections import deque

n = int(stdin.readline().strip())
vena,venb = [],[]
for i in range(n):
    sa,ea,sb,eb = map(int,stdin.readline().split())
    vena.append((sa,ea,i))
    venb.append((sb,eb,i))

vena.sort()
venb.sort()

sensa = {}
ends = deque()
for v in vena:
    sens = set()
    while ends and ends[0][1] < v[0]:
        ends.popleft()
    for e in ends:
        sensa[e[2]].add(v[2])
        sens.add(e[2])
    sensa[v[2]] = sens
    ends.append(v)

def check ():
    ends.clear()
    sensb = {}
    for v in venb:
        sens = set()
        while ends and ends[0][1] < v[0]:
            e = ends.popleft()
            if sensb[e[2]] != sensa[e[2]]:
                return False
        for e in ends:
            if v[2] not in sensa[e[2]]:
                return False
            else:
                sensb[e[2]].add(v[2])
                sens.add(e[2])
        sensb[v[2]] = sens
        ends.append(v)
    return True


if check():
    print("YES")
else:
    print("NO")
