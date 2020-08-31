from sys import stdin

t = int(stdin.readline().strip())

for _ in range(t):
    n,m,a,b = map(int,stdin.readline().split())
    if a>b and n*(a-b)//b!=m-n:
        print("NO")
        continue
    elif b>a and m*(b-a)//a!=n-m:
        print("NO")
        continue
    elif a==b and n!=m:
        print("NO")
        continue


    M = []
    j = 0
    for i in range(n):
        r = ['0' for _ in range(m)]
        for _ in range(a):
            r[j] = '1'
            j = (j+1)%m
        M.append(''.join(r))

    print("YES")
    print('\n'.join(M))
