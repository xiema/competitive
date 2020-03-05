from sys import stdin, stdout
from collections import deque

class Segment():
    __slots__ = ['seq', 'length', 'start', 'end']
    def __init__(self, start, end, length):
        self.start = start
        self.end = end
        self.length = length
        self.seq = deque([(start, end, length)])

    def add (self, id, length):
        self.seq.append((self.end, id, length))
        self.end = id
        self.length += length

    def remove (self, id):
        if self.start == id:
            (a,b,t) = self.seq.popleft()
            self.start = b
            self.length -= t
            return self.start
        elif self.end == id:
            (a,b,t) = self.seq.pop()
            self.end = a
            self.length -= t
            return self.end
        return id

    def opposite (self, id):
        if self.start == id:
            return self.end
        elif self.end == id:
            return self.start

    def __repr__ (self):
        return "{}<{}>{}".format(self.start, self.length, self.end)

def findlongest_aux (tree, start, exclude = None):
    end, length = start, 0
    for seg in tree[start]:
        segend = seg.opposite(start)
        if segend != exclude:
            _end, _length = findlongest_aux(tree, segend, start)
            _length += seg.length
            if _length > length:
                end, length = _end, _length
    return end, length

def findlongest (tree, start, prev = None):
    end, length = findlongest_aux(tree, start)
    if end == prev:
        return start, end, length
    return findlongest(tree, end, start)

def remove (tree, p):
    seg = tree.pop(p)
    if seg:
        seg = seg[0]
        start = seg.remove(p)
        if seg.length > 0:
            tree.setdefault(start, []).append(seg)
        else:
            tree[start].remove(seg)
        return start


T = int(stdin.readline())

for _ in range(T):
    k = int(stdin.readline())
    houses = {}
    root, rootend, rootlen = None, None, None
    for _ in range(2*k-1):
        a,b,t = stdin.readline().split()
        t = int(t)
        houses.setdefault(a,[]).append((b,t))
        houses.setdefault(b,[]).append((a,t))

    for h1,neighbors in houses.items():
        if len(neighbors) == 1:
            root = h1
            (rootend,rootlen) = neighbors[0]
            break

    visited = set([root,rootend])
    rootseg = Segment(root,rootend,rootlen)
    ends, next = set([root]), [(rootend, rootlen, root, rootseg)]
    tree = {root : []}
    houselist = [(rootend, root, rootlen)]
    while next:
        _next = []
        for (h1,t1,v,seg) in next:
            h2list = list(filter(lambda x: x[0] not in visited, houses[h1]))
            nc = len(h2list)
            if nc == 0:
                ends.add(h1)
                tree[h1] = [seg]
                tree[v].append(seg)
                continue
            elif nc == 1:
                (h2,t2) = h2list[0]
                visited.add(h2)
                seg.add(h2,t2)
                _next.append((h2,t2,v,seg))
                houselist.append((h2, h1, t2))
            else:
                tree[h1] = [seg]
                tree[v].append(seg)
                for (h2,t2) in h2list:
                    visited.add(h2)
                    seg = Segment(h1, h2, t2)
                    _next.append((h2,t2,h1,seg))
                    houselist.append((h2, h1, t2))
        next = _next

    houselist.reverse()

    tmin = 0
    dist = []
    paired = {}
    for (h1,h2,t) in houselist:
        if not paired.get(h1, False):
            paired[h2] = not paired.setdefault(h2, False)
            tmin += t

    tmax = 0
    start, end = root, root
    for _ in range(k):
        print(tmax)
        start, end, t = findlongest(tree, start)
        tmax += t
        start = remove(tree, start)
        end = remove(tree, end)

    print(tmin, tmax)

    #print(houses)
