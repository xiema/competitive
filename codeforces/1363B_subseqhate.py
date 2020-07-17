from sys import stdin,stdout

t = int(stdin.readline().strip())

for _ in range(t):
    s = stdin.readline().strip()
    r1 = s.count('1')
    l0,l1,r0 = 0,0,len(s)-r1
    ans = len(s)
    for c in s:
        ans = min(ans, l0+r1, l1+r0)
        if c == '1':
            l1,r1 = l1+1,r1-1
        else:
            l0,r0 = l0+1,r0-1

    stdout.write('{}\n'.format(ans))
