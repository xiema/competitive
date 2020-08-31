from sys import stdin

Pr = []
Cm = set()
for i in range(2,450):
    if i in Cm:
        continue
    Pr.append(i)
    for j in range(i,450,i):
        Cm.add(j)

seen = [False for _ in range(200000)]

def check(seq, f):
    ln = len(seq)
    for s in range(f):
        C = seq[s]
        for i in range(s,ln,f):
            if seq[i]!= C:
                break
        else:
            return True

def solve(seq):
    if check(seq, 1):
        return 1

    ln = m = len(seq)
    done = set()
    for pr in Pr:
        if pr > m:
            break
        if ln%pr:
            continue
        for d in range(pr, ln+1, pr):
            if ln%d:
                continue
            if d in done:
                continue
            done.add(d)
            if check(seq, d):
                m = min(m, d)
                break
            elif check(seq, ln//d):
                m = min(m, ln//d)

    return m


T = int(stdin.readline().strip())
ans = []
for _ in range(T):
    n = int(stdin.readline().strip())
    p = list(map(int, stdin.readline().split()))
    c = list(map(int, stdin.readline().split()))
    m = n

    for i in range(n):
        seen[i] = False
    for i in range(n):
        if seen[i]:
            continue
        u,seq = i,[]
        while not seen[u]:
            seen[u] = True
            seq.append(c[u])
            u = p[u]-1
        m = min(m,solve(seq))
        if m == 1:
            break
    ans.append(str(m))

print('\n'.join(ans))
