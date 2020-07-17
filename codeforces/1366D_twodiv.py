from sys import stdin

limit = int(1e4)
P,C = set(),set()
for i in range(2,limit):
    if i in C:
        continue
    P.add(i)
    n = i
    while n < limit:
        C.add(n)
        n +=i

n = int(stdin.readline().strip())
alist = list(map(int, stdin.readline().split()))
l1,l2 = [],[]
M = {}
for a in alist:
    if a in M:
        l1.append(M[a][0])
        l2.append(M[a][1])
        continue

    if a in P:
        M[a] = [-1,-1]
        l1.append(-1)
        l2.append(-1)
        continue

    A = False
    for p in P:
        if p > a:
            break
        if a%p:
            continue
        d1,d2 = 1,a
        while d2%p == 0:
            if d2 in M:
                if M[d2][0] == -1:
                    d1,d2 = a,1
                elif M[d2][0]%p==0:
                    d1,d2 = d1*M[d2][0],M[d2][1]
                else:
                    d1,d2 = d1*M[d2][1],M[d2][0]
                break
            d2//=p
            d1*=p
        if d2 != 1:
            l1.append(d1)
            l2.append(d2)
            M[a] = [d1,d2]
            A = True
            break
    if not A:
        l1.append(-1)
        l2.append(-1)
        M[a] = [-1,-1]


print(' '.join(map(str, l1)))
print(' '.join(map(str, l2)))
