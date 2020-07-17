from sys import stdin,stdout

t = int(stdin.readline().strip())

for _ in range(t):
    n = int(stdin.readline().strip())
    a = list(map(int,stdin.readline().split()))
    e = 0
    for i in range(0,n,2):
        e += a[i]
    M,m,k = e,a[0],1
    e-=a[0]
    for i in range(1,n):
        if i%2==0: #even
            e -= a[i]
            if k > 0 and a[k] < a[k-1]:
                m = m + a[k-1]
                k-=1
            else:
                m = m + a[k]
                k+=1
        else: #odd
            if k > 0 and a[k] < a[k-1]:
                m = m - a[k] + a[i]
                k+=1
            else:
                m = m - a[k-1] + a[i]
                k-=1
        M = max(M, m+e)
    stdout.write('{}\n'.format(M))
