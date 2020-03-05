from sys import stdin, stdout

t = int(stdin.readline().strip())

for _ in range(t):
    n, m = map(int, stdin.readline().split())
    presents = list(map(int, stdin.readline().split()))
    orders = list(map(int, stdin.readline().split()))

    ip, io, pstart = 0, 0, 0
    found = set()
    oset = set(orders)
    time = 0
    unstkcount = 0
    o = orders[io]
    while io < len(orders):
        ip = presents.index(o,pstart)
        isect = oset.intersection(presents[pstart:ip])
        unstkcount += ip-pstart
        time += 2*unstkcount+1
        pstart = ip+1
        found.update(isect)
        io+=1
        while io < len(orders):
            o = orders[io]
            if o in found:
                time += 1
                unstkcount -= 1
            else:
                break
            io+=1

    stdout.write("{}\n".format(time))
