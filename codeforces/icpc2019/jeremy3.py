from sys import stdin, stdout

class Segment:
    def __init__(self, start, end, length):
        self.start = start
        self.end = end
        self.length = length
        self.seq = [(start, end, length)]
        self.nextseg, self.prevseg = [], []

    def append(self, end, length):
        self.seq.append((self.end, end, length))
        self.end = end
        self.length += length

    def remove(self, p):
        if self.length == 0:
            return p
        if p == self.start:
            k1,k2,v = self.seq.pop(0)
            self.start, self.length = k2, self.length-v
            if self.length == 0 and self.nextseg:
                for seg in self.nextseg:
                    seg.prevseg.remove(self)
                    if seg.prevseg:
                        k2 = seg.end
            return k2
        elif p == self.end:
            k1,k2,v = self.seq.pop(-1)
            self.end, self.length = k1, self.length-v
            if self.length == 0 and self.prevseg:
                for seg in self.prevseg:
                    try:
                        seg.nextseg.remove(self)
                        if seg.nextseg:
                            k1 = seg.start
                    except ValueError:
                        seg.prevseg.remove(self)
                        if seg.prevseg:
                            k1 = seg.end
            return k1

    def findlongest_aux(self, begin):
        a,b,l,sega,segb = None,None,self.length,self,self
        if begin == self.end:
            a,b = self.end,self.start
            for seg in self.prevseg:
                _,_b,_l,_,_segb = seg.findlongest_aux(self.start)
                _l+=self.length
                if _l > l:
                    b,l,segb = _b,_l,_segb
        else:
            a,b = self.start,self.end
            for seg in self.nextseg:
                _,_b,_l,_,_segb = seg.findlongest_aux(self.end)
                _l+=self.length
                if _l > l:
                    b,l,segb = _b,_l,_segb
        return a,b,l,sega,segb

    def findlongest(self, begin, prev=None):
        a,b,l,sega,segb = self.findlongest_aux(begin)
        if b == prev:
            return a,b,l,sega,segb
        return segb.findlongest(b,begin)

    def gettotal(self):
        i,j = 0,len(self.seq)-1
        r = l = self.length
        while i < j:
            l -= self.seq[i][2] + self.seq[i][2]
            r += l
            i += 1
            j -= 1
        return r


T = int(stdin.readline())

for _ in range(T):
    k = int(stdin.readline())
    flags, houses = {}, {}
    root, rootend, rootseglen = None, None, None
    for _ in range(2*k-1):
        a,b,t = stdin.readline().split()
        t = int(t)
        flags[a], flags[b] = 0, 0
        if a not in houses:
            houses[a] = []
            root, rootend, rootseglen = a, b, t
        if b not in houses:
            houses[b] = []
            root, rootend, rootseglen = b, a, t
        houses[a].append((b,t))
        houses[b].append((a,t))

    houselist, flags[root], flags[rootend] = [root, rootend], 1, 1
    rootseg = Segment(root, rootend, rootseglen)
    next, c = [rootseg], 2
    segments = [rootseg]

    print("test")

    while c < 2*k:
        _next = []
        for seg in next:
            if len(houses[seg.end]) == 2:
                for (h1,t1) in filter(lambda x: flags[x[0]] != 1, houses[seg.end]):
                    flags[h1] = 1
                    _next.append(seg)
                    c += 1
                    seg.append(h1,t1)
                    houselist.append(h1)
            else:
                for (h1,t1) in filter(lambda x: flags[x[0]] != 1, houses[seg.end]):
                    flags[h1] = 1
                    newseg = Segment(seg.end, h1, t1)
                    newseg.prevseg.append(seg)
                    for other in seg.nextseg:
                        other.prevseg.append(newseg)
                        newseg.prevseg.append(other)
                    seg.nextseg.append(newseg)
                    _next.append(newseg)
                    c += 1
                    houselist.append(h1)
        next = _next

    print("test")

    tmin, paired = 0, {}
    for h1 in reversed(houselist):
        if h1 not in paired:
            c = 0
            for (h2,t) in filter(lambda h: flags[h[0]] == 2, houses[h1]):
                if h2 not in paired:
                    paired[h2] = False
                    tmin += t
                    c+=1
            if c%2 == 1:
                paired[h1] = False
            flags[h1] = 2

    print("test")

    tmax = 0
    a,b,sega,segb = root, root, rootseg, None
    for _ in range(k):
        a,b,l,sega,segb = sega.findlongest(a)
        if sega == segb:
            tmax+=sega.gettotal()
            break
        tmax+=l
        segb.remove(b)
        a = sega.remove(a)
        if sega.length == 0:
            if sega.nextseg:
                sega = sega.nextseg[0]
                a = sega.start
            elif sega.prevseg:
                sega = sega.prevseg[0]
                a = sega.end
        #print(a,b)


    print(tmin, tmax)

    #print(houses)
