from sys import stdin

n,k = map(int,stdin.readline().split())
ba,bb,bc = [],[],[]
for _ in range(n):
    t,a,b = map(int, stdin.readline().split())
    if a and b:
        bc.append(t)
    elif a:
        ba.append(t)
    elif b:
        bb.append(t)

ba.sort()
bb.sort()
bc.sort()

a,b,c = 0,0,0
T = 0
while k:
    if c<len(bc) and a<len(ba) and b<len(bb):
        if bc[c] < ba[a]+bb[b]:
            T += bc[c]
            c += 1
            k -= 1
        else:
            T += ba[a] + bb[b]
            a += 1
            b += 1
            k -= 1
    elif c<len(bc):
        T += bc[c]
        c += 1
        k -= 1
    elif a<len(ba) and b<len(bb):
        T += ba[a] + bb[b]
        a += 1
        b += 1
        k -= 1
    else:
        T = -1
        break

print(T)
