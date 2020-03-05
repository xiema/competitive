from sys import stdin, stdout

t = int(stdin.readline().strip())
for _ in range(t):
    p = stdin.readline().strip()
    h = stdin.readline().strip()
    lp, lh = len(p), len(h)
    if lh < lp:
        stdout.write("NO\n")
        continue

    letters = {}
    scan = {}
    for c in p:
        letters[c] = letters.setdefault(c,0) + 1

    ans = False
    i,j = 0,0
    scan = {}
    while j < lh:
        c = h[j]
        if c not in letters:
            scan.clear()
            j+=1
            i=j
            if lh-i < lp:
                ans = False
                break
            continue

        scan[c] = scan.setdefault(c,0) + 1
        if scan[c] > letters[c]:
            while h[i] != c:
                scan[h[i]]-=1
                i+=1
            i+=1
            scan[c] -= 1
            if lh-i < lp:
                ans = False
                break
            j+=1
            continue

        if scan[c] == letters[c] and j-i+1 == lp:
            ans = True
            break

        j+=1

    if ans:
        stdout.write("YES\n")
    else:
        stdout.write("NO\n")
