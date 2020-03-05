from sys import stdin,stdout

T = int(stdin.readline().strip())
for t in range(1,T+1):
    N = int(stdin.readline().strip())
    mtx = []
    for _ in range(N):
        mtx.append(list(map(int, stdin.readline().strip())))
    M = int(stdin.readline().strip())
    flip = False
    for _ in range(M):
        line = stdin.readline().split()
        if line[0] == "row":
            a,b = int(line[1])-1,int(line[2])-1
            if not flip:
                mtx[a],mtx[b] = mtx[b],mtx[a]
            else:
                for i in range(N):
                    mtx[i][a],mtx[i][b] = mtx[i][b],mtx[i][a]
        elif line[0] == "col":
            a,b = int(line[1])-1,int(line[2])-1
            if not flip:
                for i in range(N):
                    mtx[i][a],mtx[i][b] = mtx[i][b],mtx[i][a]
            else:
                mtx[a],mtx[b] = mtx[b],mtx[a]
        elif line[0] == "transpose":
            flip = not flip
        elif line[0] == "inc":
            for r in mtx:
                for i in range(N):
                    r[i] = (r[i]+1)%10
        elif line[0] == "dec":
            for r in mtx:
                for i in range(N):
                    r[i] = (r[i]-1)%10

    stdout.write("Case #{}\n".format(t))
    if not flip:
        for i in range(N):
            for j in range(N):
                stdout.write(str(mtx[i][j]))
            stdout.write('\n')
    else:
        for i in range(N):
            for j in range(N):
                stdout.write(str(mtx[j][i]))
            stdout.write('\n')
    stdout.write('\n')
