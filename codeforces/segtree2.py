from sys import stdin, stdout

C = int(stdin.readline().strip())
total = 0
segs = {}
for _ in range(C):
    l, r = map(int,stdin.readline().split())
    segs[l], segs[r] = r, l

total = 0
i = 1
C2 = 2 * C
for _ in range(C):
    print(total)
    j = segs[i]
    if j > i:
        j -= 1
        if segs[j] > j:
            total += j-i
        else:
            total += segs[j]-i
    else:
        j += 1
        if segs[j] < j:
            total += i-j
        else:
            total += i-segs[j]

    i = j

print(total)
