from sys import stdin,stdout
T = int(stdin.readline().strip())

def readint(n):
    i,w = 0,''
    while i < n:
        c = stdin.read(1)
        if c.isspace() or c == '':
            if w:
                yield int(w)
                w = ''
                i+=1
        else:
            w += c

for t in range(1,T+1):
    N = int(stdin.readline().strip())
    pq = [i for i in readint(2*N)]
    d = [pq[i]-pq[i+N] for i in range(N)]
    f = 0
    i,j = 0,0
    while i < N:
        f+=d[j%N]
        if f < 0:
            i,j = j+1,j+1
            f=0
        else:
            j+=1
            if j%N==i:
                break
    if i>=N:
        stdout.write("Case {}: Not possible\n".format(t))
    else:
        stdout.write("Case {}: Possible from station {}\n".format(t,i+1))
