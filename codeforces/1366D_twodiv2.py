from sys import stdin

lim1,lim2 = int(1e4),int(1e7+10)
A = {}
for n in range(2,lim1):
    if n in A:
        continue
    A[n] = [-1,-1]
    m,i = n+n,2
    while m < lim2:
        if i%n:
            A[m] = [n,i]
        elif A[i][0] == -1:
            A[m] = [-1,-1]
        else:
            if A[i][0]%n==0:
                A[m] = [A[i][0]*n, A[i][1]]
            else:
                A[m] = [A[i][1]*n, A[i][0]]
        m,i = m+n,i+1

print(A)

n = int(stdin.readline().strip())
alist = list(map(int, stdin.readline().split()))
l1,l2 = [],[]
for a in alist:
    l1.append(A[a][0])
    l2.append(A[a][1])

print(' '.join(map(str, l1)))
print(' '.join(map(str, l2)))
