from sys import stdin,stdout

t = int(stdin.readline().strip())

for _ in range(t):
    n = int(stdin.readline().strip())
    A,c,r,z = [],1,0,False

    if n==2:
        stdout.write('1\n0\n')
        continue

    while n:
        if n==2:
            A.append(str(r))
            break
        if z and n%2 or not z and n%2==0:
            z = True
            r+=c
        if n==2:

        elif n==3:
            A.append(str(c))
        else:
            A.append(str(r))
            break
        n//=2
        c*=2
    stdout.write('{}\n'.format(len(A)))
    stdout.write(' '.join(A) + '\n')
