from sys import stdin, stdout

t = int(stdin.readline().strip())
P = {a:0 for a in [2,3,5,7,11,13,17,19,23,29,31]}

for _ in range(t):
    n = int(stdin.readline().strip())
    alist = list(map(int, stdin.readline().split()))
    for p in P:
        P[p] = 0
    used = 0
    ans = []
    for a in alist:
        for p in P:
            if a%p==0 or p==31:
                if P[p] == 0:
                    used+=1
                    P[p] = used
                ans.append(p)
                break
    ans = ' '.join([str(P[a]) for a in ans])
    stdout.write('{}\n{}\n'.format(used,ans))
