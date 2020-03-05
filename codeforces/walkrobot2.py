from sys import stdin,stdout
t = int(stdin.readline().strip())

for _ in range(t):
    n = int(stdin.readline().strip())
    posX,posY = 0,0
    posD = {(0,0):[0]}
    for i,c in enumerate(stdin.readline().strip()):
        if c == 'L':
            posX -= 1
        elif c == 'R':
            posX += 1
        elif c == 'U':
            posY += 1
        elif c == 'D':
            posY -= 1
        posD.setdefault((posX,posY),[]).append(i+1)

    a,b,c = 0,0,n+1
    for l in posD.values():
        i = 0
        while i+1 < len(l):
            if l[i+1]-l[i] < c:
                a,b = l[i],l[i+1]
                c = b-a
            i+=1

    if a==b:
        stdout.write("-1\n")
    else:
        stdout.write("{} {}\n".format(a+1,b))
