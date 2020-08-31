from sys import stdin,stdout

T = int(stdin.readline().strip())
for _ in range(T):
    N = int(stdin.readline().strip())
    e = list(map(int, stdin.readline().split()))
    e.sort()
    C,c=0,0
    for i in range(N):
        c+=1
        if c==e[i]:
            c=0
            C+=1
    stdout.write('{}\n'.format(C))
