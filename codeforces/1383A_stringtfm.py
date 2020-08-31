from sys import stdin,stdout

t = int(stdin.readline().strip())

o = {}
for c in "abcdefghijklmnopqrst":
    o[c] = ord(c)-ord('a')

for _ in range(t):
    n = int(stdin.readline().strip())
    A = stdin.readline().strip()
    B = stdin.readline().strip()

    def solve():
        l = []
        for i in range(n):
            a,b = o[A[i]],o[B[i]]
            if b < a:
                return -1
            elif b > a:
                l.append((b-a,a,b))
        l.sort()

        R = [i for i in range(20)]
        C = 0
        for d,a,b in l:
            s = a
            i = a
            while R[i] != i and R[i] < b:
                s = i = R[i]
            if R[i] == b:
                continue
            e = i
            while i < b:
                if R[i] == i or R[i] > b:
                    e = i
                i+=1
            if e == i:
                R[i] = b
            else:
                if R[e] == e:
                    R[s],R[e] = e,b
                else:
                    R[s],R[e],R[b] = e,b,R[e]
            C+=1
        return C

    stdout.write('{}\n'.format(solve()))
