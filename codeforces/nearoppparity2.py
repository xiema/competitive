from sys import stdin,stdout

n = int(stdin.readline().strip())
ints = list(map(int, stdin.readline().split()))
counts = {0:{},1:{}}

def getnearest(idx, p_even, seen):
    seen.add(idx)

    #if idx in counts[p_even]:
        #return counts[p_even][idx]

    if ints[idx]%2 == p_even:
        counts[p_even][idx] = 0
        return 0

    a,b = idx+ints[idx],idx-ints[idx]
    if a >= n and b < 0:
        counts[p_even][idx] = -1
        return -1

    if (a >= n or a in seen) and (b < 0 or b in seen):
        if a not in counts[p_even] and b not in counts[p_even]:
            return -1

    ca,cb = -1,-1
    if a < n:
        if a in counts[p_even]:
            ca = counts[p_even][a]
        elif a not in seen:
            ca = getnearest(a, p_even, seen.copy())
    if b >= 0:
        if b in counts[p_even]:
            cb = counts[p_even][b]
        elif b not in seen:
            cb = getnearest(b, p_even, seen.copy())
    #if idx == 84:
        #print(a,ca,cb)

    ans = None
    if ca >= 0 and cb >= 0:
        #counts[p_even][idx] = min(ca,cb) + 1
        ans = min(ca,cb) + 1
        #counts[p_even][idx] = ans
    elif ca >= 0:
        #counts[p_even][idx] = ca + 1
        ans = ca + 1
    elif cb >= 0:
        #counts[p_even][idx] = cb + 1
        ans = cb + 1
    else:
        #return -1
        ans = -1

    #return counts[p_even][idx]
    return ans

out = []
for i in range(n):
    opp = (ints[i]+1)%2
    v = getnearest(i, opp, set())
    #print(i, ints[i], v)
    counts[opp][i] = v
    out.append(v)

stdout.write(' '.join(list(map(str,out))))
