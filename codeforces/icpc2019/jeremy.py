from sys import stdin, stdout, setrecursionlimit

setrecursionlimit(10**6)

class Path:
    def __init__ (self, a = None, b = None, t = 0, seq = None, tseq = None, rseq = None, rtseq = None):
        self.a = a
        self.b = b
        self.t = t
        self.seq = seq or [a,b]
        self.tseq = tseq or [t]
        self.rseq = rseq or [b,a]
        self.rtseq = rtseq or [t]

    def append (self, b, t):
        self.t += t
        self.b = b
        self.seq.append(b)
        self.tseq.append(t)
        self.rseq.insert(0,b)
        self.rtseq.insert(0,t)

    def remove (self, h):
        if self.t > 0:
            if self.a == h:
                self.t -= self.tseq[0]
                del self.seq[0]
                del self.rseq[-1]
                del self.tseq[0]
                del self.rtseq[-1]
                if len(self.seq) > 0:
                    self.a = self.seq[0]
            elif self.b == h:
                self.t -= self.rtseq[0]
                del self.rseq[0]
                del self.seq[-1]
                del self.rtseq[0]
                del self.tseq[-1]
                if len(self.seq) > 0:
                    self.b = self.rseq[0]

    def __lt__ (self, other):
        if self.t == other.t:
            c1,c2 = len(self.seq),len(other.seq)
            if c1 == c2:
                return self.tseq[0]+self.tseq[-1] < other.tseq[0]+other.tseq[-1]
            return c1 < c2
        return self.t < other.t

class House:
    def __init__ (self, index):
        self.index = index
        self.children = {}
        self.childcount = 0
        self.times = []
        self.parent = None
        self.parenttime = 0
        self.paired = False
        self.paths = []

    def add(self, child, time):
        self.children[child.index] = child
        child.parent = self
        child.parenttime = time
        self.childcount += 1

    def remove(self, child):
        if child.index in self.children:
            del self.children[child.index]
            self.childcount -= 1

    def update(self):
        self.times = []
        for child in self.children.values():
            l,p = child.longest()
            self.times.append((l + child.parenttime, p))

    def longest(self):
        if len(self.children) == 0:
            return 0, self
        l,p = 0,self
        for (_l, _p) in self.times:
            if _l > l:
                l, p = _l, _p
        return self.times[0][0], self.times[0][1]

    def findlongest(self):
        c = len(self.children)

        if c == 0:
            return 0, self, self

        if c == 1:
            for idx, child in self.children.items():
                add, a,b = child.findlongest()
                return add+self.times[idx], self, b

        add, a, b = 0, None, None
        for idx, child in self.children.items():
            _add, _a, _b = child.findlongest()
            _add += self.times[idx]
            if _add > add:
                add,a,b = _add,_a,_b

        return add, self, b

    def getlongestpaths(self):
        seq = []
        for idx, child in self.children.items():
            add,a,b = child.findlongest()
            seq.append((add+self.times[idx],a,b))
        seq.sort(reverse=True)
        return seq

    def getminimum(self):
        if len(self.children) == 0:
            return 0, True
        min = 0
        c = 0
        for child in self.children.values():
            _min, extra = child[0].getminimum()
            min += _min
            if extra:
                min += child[1]
                c+=1
        if c%2 == 0:
            return min, True
        else:
            return min, False

    def childcount(self):
        return len(self.children)

    def __lt__(self, other):
        return self.index < other.index

    def __repr__(self):
        return str(self.index)

def connect (path1, path2):
    return Path(path1.a, path2.a, path1.t+path2.t, path1.seq+path2.rseq, path1.tseq+path2.rtseq, path2.seq+path1.rseq, path2.tseq+path1.rtseq)

T = int(stdin.readline())

for _ in range(T):
    k = int(stdin.readline())
    houses = {}
    cur = None
    for _ in range(2*k-1):
        a,b,t = map(int, stdin.readline().split())
        if a not in houses:
            houses[a] = House(a)
            if b in houses:
                houses[b].add(houses[a], t)
            else:
                houses[b] = House(b)
                houses[a].add(houses[b], t)
        else:
            if b in houses:
                houses[a].add(houses[b], t)
            else:
                houses[b] = House(b)
                houses[a].add(houses[b], t)
        if not cur:
            cur = houses[a]

    houselist = [cur]
    next = [cur]
    c = 1
    while c < 2*k:
        _next = []
        for h in next:
            _c = h.childcount
            if _c > 0:
                _next.extend(h.children.values())
                c += _c
        houselist.extend(_next)
        next = _next
    houselist.reverse()

    tmin, paths = 0, []
    for h1 in houselist:
        if not h1.paired:
            c = 0
            for h2 in h1.children.values():
                if not h2.paired:
                    h2.paired = True
                    tmin += h2.parenttime
                    c+=1
            if c%2 == 1:
                h1.paired = True
        if h1.childcount > 0:
            for h2 in h1.children.values():
                if h2.childcount == 0:
                    h1.paths.append(Path(h2, h1, h2.parenttime))
                else:
                    for p in h2.paths:
                        p.append(h1, h2.parenttime)
                    h1.paths.extend(h2.paths)
            if h1.childcount > 1:
                c = len(h1.paths)
                for i in range(c-1):
                    for j in range(i,c):
                        p = connect(h1.paths[i], h1.paths[j])
                        paths.append(p)

    if cur.childcount == 1:
        paths.extend(cur.paths)

    paths.sort(reverse=True)
    tmax = 0
    while True:
        c = len(paths)
        if c == 0:
            break;
        elif c == 1:
            while paths[0].t > 0:
                t,a,b = paths[0].t, paths[0].a, paths[0].b
                tmax+=t
                paths[0].remove(a)
                paths[0].remove(b)
            break
        else:
            t,a,b = paths[0].t, paths[0].a, paths[0].b
            tmax+=t
            _paths = []
            for p in paths:
                p.remove(a)
                p.remove(b)
                if p.t > 0:
                    _paths.append(p)
            paths = _paths
            paths.sort(reverse=True)

    stdout.write("{} {}\n".format(tmin, tmax))
