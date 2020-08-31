from sys import stdin

def solve(M,n,m):
    for i in range(n):
        for j in range(m):
            if M[i][j]==0:
                continue
            c,r = 0,0
            if i>0:
                c+=(M[i-1][j]>0)
                r+=1
            if i<n-1:
                c+=(M[i+1][j]>0)
                r+=1
            if j>0:
                c+=(M[i][j-1]>0)
                r+=1
            if j<m-1:
                c+=(M[i][j+1]>0)
                r+=1
            if M[i][j] > r:
                return False
            if c<M[i][j] and i>0 and M[i-1][j]==0:
                M[i-1][j]=1
                c+=1
            if c<M[i][j] and i<n-1 and M[i+1][j]==0:
                M[i+1][j]=1
                c+=1
            if c<M[i][j] and j>0 and M[i][j-1]==0:
                M[i][j-1]=1
                c+=1
            if c<M[i][j] and j<m-1 and M[i][j+1]==0:
                M[i][j+1]=1
                c+=1
    for i in range(n):
        for j in range(m):
            if M[i][j]==0:
                continue
            c = 0
            if i>0:
                c+=(M[i-1][j]>0)
            if i<n-1:
                c+=(M[i+1][j]>0)
            if j>0:
                c+=(M[i][j-1]>0)
            if j<m-1:
                c+=(M[i][j+1]>0)
            M[i][j] = c
    return True

t = int(stdin.readline().strip())
for _ in range(t):
    n,m = map(int, stdin.readline().split())
    M = [list(map(int, stdin.readline().split())) for _ in range(n)]
    if solve(M,n,m):
        print("YES")
        for i in range(n):
            print(' '.join([str(M[i][j]) for j in range(m)]))
    else:
        print("NO")
