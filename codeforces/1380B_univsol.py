from sys import stdin,stdout

t = int(stdin.readline().strip())

for _ in range(t):
    s = stdin.readline().strip()
    R,S,P = 0,0,0
    for c in s:
        if c == 'R':
            R+=1
        elif c == 'S':
            S+=1
        else:
            P+=1
    m = max(R,S,P)
    if m == R:
        a = 'P'
    elif m == S:
        a = 'R'
    else:
        a = 'S'

    stdout.write(a * len(s) + '\n')
