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

def get_sens(ven):
    ret = {}
    i,ends = 0,[]
    for v in ven:
        ret[v[2]] = set()
        while i < len(ends) and ends[i][1] < v[0]:
            i+=1
        for j in range(i,len(ends)):
            ret[ends[j][2]].add(v[2])
            ret[v[2]].add(ends[j][2])
        ends.append(v)
    return ret

sensa, sensb = get_sens(vena), get_sens(venb)

for i in range(n):
    if sensa[i] != sensb[i]:
        print("NO")
        break
else:
    print("YES")
