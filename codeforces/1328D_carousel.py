from sys import stdin,stdout


q = int(stdin.readline().strip())

for _ in range(q):
    n = int(stdin.readline().strip())
    t = list(map(int, stdin.readline().split()))
    cons = -1
    types = set()
    for i in range(n):
        types.add(t[i])
        if t[i] == t[i-1]:
            cons = i

    if len(types) == 1:
        stdout.write('1\n{}\n'.format(' '.join(['1' for _ in range(n)])))
    elif n%2==0:
        stdout.write('2\n{}\n'.format(' '.join([['1','2'][i%2] for i in range(n)])))
    elif cons != -1:
        a = []
        b = False
        c = ['1','2']
        for i in range(n):
            if i != cons:
                b = not b
            a.append(c[b])
        stdout.write('2\n{}\n'.format(' '.join(a)))
    else:
        a = [['1','2'][i%2] for i in range(n)]
        a[-1] = '3'
        stdout.write('3\n{}\n'.format(' '.join(a)))
