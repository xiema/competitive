from sys import stdin,stdout

m = int(stdin.readline().strip())

for _ in range(m):
    n,T,a,b = map(int, stdin.readline().split())
    diff = list(map(int,stdin.readline().split()))
    mand = list(map(int,stdin.readline().split()))

    easy,hard = [],[]
    for i in range(n):
        if diff[i]:
            hard.append(mand[i])
        else:
            easy.append(mand[i])

    easy.sort()
    hard.sort()

    t,i,j,k = 0,0,0,0
    ans = 0
    while t < T:
        #print(t,i,j)
        _be,_bh = i < len(easy), j<len(hard)
        if _be and _bh:
            #if easy[i] < hard[j]:
            #    k = i
            if t < hard[j]:
                if t < easy[i]:
                    ans = max(ans,i+j)
                    _t = t+b
                    if _t <= T and (j+1 == len(hard) or _t < hard[j+1]) and _t < easy[i]:
                        k=i
                t += a
                i += 1
            else:
                t = t+b-a*(i-k)
                j += 1
                i = k
        elif _be:
            if t < easy[i]:
                ans = max(ans,i+j)
            i += 1
            t += a
        elif _bh:
            if t < hard[j]:
                ans = max(ans,i+j)
            j += 1
            t = t+b-a*(i-k)
            i = k
        else:
            break

    if t <= T and (i==len(easy) or t<easy[i]) and (j==len(hard) or t<hard[j]):
        ans = max(ans,i+j)

    stdout.write("{}\n".format(ans))
