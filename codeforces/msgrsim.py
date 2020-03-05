from bisect import bisect_left

n,m = map(int, input().split())
alist = list(map(int, input().split()))

posmax = {}
lastpos = {}
seen = []
seenpos = []
c = 0
for idx,a in enumerate(alist):
    if a in lastpos:
        i = bisect_left(seenpos, lastpos[a])
        posmax[a] = max(posmax[a], c-i)
        del seenpos[i]
    else:
        i = bisect_left(seen, a)
        posmax[a] = a+c-i
        seen.insert(i, a)
        c+=1
    seenpos.append(idx)
    lastpos[a] = idx
else:
    ls = sorted([(v,k) for k,v in lastpos.items()], reverse=True)
    c = 1
    for pos,a in ls:
        posmax[a] = max(posmax[a], c)
        c+=1

lines = []
d = 0
for i in range(n,0,-1):
    a,b = i,i
    if i in posmax:
        a,b = 1,posmax[i]
        d+=1
    else:
        b+=d
    lines.append("{} {}".format(a,b))

lines.reverse()
print('\n'.join(lines))
