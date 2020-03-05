from sys import stdin,stdout

r,c = map(int, stdin.readline().split())

if r == 1 and c == 1:
    stdout.write("0\n")
else:
    base, mult = None,None
    if c < r:
        base = [x for x in range(1,c+1)]
        mult = [x for x in range(c+1,r+c+1)]
    else:
        base = [x for x in range(r+1,r+c+1)]
        mult = [x for x in range(1,r+1)]

    for m in mult:
        for b in base:
            stdout.write('{} '.format(m*b))
        stdout.write('\n')
