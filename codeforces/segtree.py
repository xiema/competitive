from sys import stdin, stdout
from bisect import insort
from collections import namedtuple, deque

C = int(stdin.readline().strip())

Segment = namedtuple('Segment', ['left', 'right', 'index'])
#segs = [Segment(*map(int, stdin.readline().split()), i) for i in range(C)]
#segs.sort()
segs = []
for i in range(C):
    insort(segs, Segment(*map(int, stdin.readline().split()), i))

def istree ():
    vertices, edges = 0, 0
    graphs = {}

    cur = set()
    c = 0
    for seg1 in segs:
        _cur = set()
        for seg2 in cur:
            if seg2.right > seg1.left:
                _cur.add(seg2)
                if seg1.right > seg2.right:
                    edges += 1
                    if seg1.index in graphs:
                        if seg2.index in graphs:
                            if graphs[seg1.index][0] == graphs[seg2.index][0]:
                                return "NO"
                            graphs[seg2.index][0] = graphs[seg1.index][0]
                        else:
                            graphs[seg2.index] = graphs[seg1.index]
                            vertices += 1
                    else:
                        if seg2.index in graphs:
                            graphs[seg1.index] = graphs[seg2.index]
                            vertices += 1
                        else:
                            graphs[seg1.index] = graphs[seg2.index] = [c]
                            c += 1
                            vertices += 2
        _cur.add(seg1)
        cur = _cur

    if vertices == 0:
        return "YES"

    if vertices - 1 == edges:
        return "YES"
    else:
        return "NO"

stdout.write(istree())
