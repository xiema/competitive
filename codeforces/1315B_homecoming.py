from sys import stdin,stdout
t = int(stdin.readline().strip())
for _ in range(t):
    a,b,p = map(int, stdin.readline().split())
    s = stdin.readline().strip()
    c = a+b
    k = 2*(p//c)
    if s[-1] == 'A':
        if p%c >= a:
            k+=1
    else:
        if p%c >= b:
            k+=1

    i = len(s)-1
    if k:
        while i > 0:
            if s[i-1]!=s[i]:
                k-=1
                if k < 0:
                    break
            i-=1
    stdout.write("{}\n".format(i+1))
