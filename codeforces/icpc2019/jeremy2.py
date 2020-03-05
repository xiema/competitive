from sys import stdin, stdout

class Path:
    def __init__ (self, a, parent = None):
        self.a = a
        self.b = a
        self.t = 0
        self.parent = parent
        self.tseq = []
        self.children = []
        if parent:
            parent.children.append(self)

    def append (self, h, t):
        self.b = h
        self.t += t
        self.tseq.append(t)

    def __repr__ (self, level=0):
        return level*'\t' + "{} {}\n".format(self.a, self.b) + '\n'.join([c.__repr__(level+1) for c in self.children])

class House:
    def __init__ (self, index):
        self.index = index
        self.neighbors = []
        self.flag = 0
        self.paired = False

    def addneighbor (self, h, t):
        self.neighbors.append((h, t))
        h.neighbors.append((self, t))

    def __repr__ (self):
        return str(self.index)

T = int(stdin.readline())

for _ in range(T):
    k = int(stdin.readline())
    houses = {}
    for _ in range(2*k-1):
        a,b,t = map(int, stdin.readline().split())
        if a not in houses:
            houses[a] = House(a)
        if b not in houses:
            houses[b] = House(b)
        houses[a].addneighbor(houses[b], t)

    root, houselist = None, []
    for h1 in houses.values():
        if len(h1.neighbors) == 1:
            h1.flag = 1
            root = Path(h1)
            (h2,t2) = h1.neighbors[0]
            root.append(h2, t2)
            h2.flag = 1
            houselist.append(h1)
            houselist.append(h2)
            break
    next, c = [root], 2

    while c < 2*k:
        _next = []
        for p in next:
            nc, _neighbors = 0, []
            for h in filter(lambda h: h[0].flag != 1, p.b.neighbors):
                h[0].flag = 1
                houselist.append(h[0])
                _neighbors.append(h)
                nc += 1
            if nc == 1:
                p.append(*_neighbors[0])
                _next.append(p)
            elif nc > 1:
                for h in _neighbors:
                    _p = Path(p.b, p)
                    _p.append(*h)
                    _next.append(_p)
            c += nc
        next = _next

    houselist.reverse()
    #print(houselist)
    tmin = 0
    for h1 in houselist:
        if not h1.paired:
            c = 0
            for (h2,t2) in filter(lambda h: h[0].flag == 2, h1.neighbors):
                if not h2.paired:
                    h2.paired = True
                    tmin += t2
                    c+=1
            if c%2 == 1:
                h1.paired = True
        h1.flag = 2
    print(tmin)
