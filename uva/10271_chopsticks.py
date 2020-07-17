from sys import stdin,stdout

T = int(stdin.readline().strip())

for _ in range(T):
    K,N = map(int, stdin.readline().split())
    L = list(map(int, stdin.readline().split()))
    K+=8

    B = {}
    for i in range(N-1):
        b = L[i]-L[i+1]
        b *= b
        B[i] = b

    m1,m2 = {},{}
    s,e = N-3,(K-1)*2
    m1[s] = B[s]
    for i in range(s-1,e-1,-1):
        m1[i] = min(B[i], m1[i+1])

    for r in range(2,K+1):
        m1,m2 = m2,m1
        s,e = N-r*3,2*(K-r)
        m1[s] = m2[s+2] + B[s]
        for i in range(s-1,e-1,-1):
            m1[i] = min(m1[i+1], B[i]+m2[i+2])

    stdout.write('{}\n'.format(m1[0]))
