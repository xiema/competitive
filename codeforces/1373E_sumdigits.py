from sys import stdin,stdout

A = {k : {} for k in range(0,10)}
for n in range(1,151):
    A[0][n] = n

for k in range(1,10):
    for n in range(1,151):
        if n < k:
            A[k][n] = -1
        elif n == k:
            A[k][n] = 0
        else:
            m = n-k-1
            if m > 0 and A[k][m] != -1:
                d,a = 1,A[k][m]
                while a%10 == 9:
                    d*=10
                    a//=10
                A[k][n] = A[k][m] + d
            else:
                A[k][n] = -1


t = int(stdin.readline().strip())

for _ in range(t):
    n,k = map(int, stdin.readline().split())
    stdout.write('{}\n'.format(A[k][n]))
