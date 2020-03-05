from sys import stdin, stdout
from bisect import bisect_left, insort

n = int(stdin.readline().strip())
vena,venb = [],[]
for i in range(n):
    sa,ea,sb,eb = map(int,stdin.readline().split())
    vena.append((sa,True,sb,eb))
    vena.append((ea+1,False,sb,eb))
    venb.append((sb,True,sa,ea))
    venb.append((eb+1,False,sa,ea))

vena.sort()
venb.sort()

def check (ven):
    s,e = [],[]
    for v in ven:
        if not v[1]:
            del s[bisect_left(s,v[2])]
            del e[bisect_left(e,v[3])]
        else:
            if (s and s[-1] > v[3]) or (e and e[0] < v[2]):
                return False
            insort(s, v[2])
            insort(e, v[3])
    return True

if check(vena) and check(venb):
    print("YES")
else:
    print("NO")
