from sys import stdin,stdout

t = int(stdin.readline().strip())
for _ in range(t):
    n = int(stdin.readline().strip())
    M = [stdin.readline().strip() for _ in range(n)]
    ans = True
    for i in range(n-1,-1,-1):
        for j in range(n-1,-1,-1):
            if M[i][j] == '1':
                if i<n-1 and M[i+1][j]=='0' and j<n-1 and M[i][j+1]=='0':
                    ans = False
                    break
        if not ans:
            break
    if ans:
        stdout.write("YES\n")
    else:
        stdout.write("NO\n")
