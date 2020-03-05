from sys import stdin, stdout

T = int(stdin.readline())
out = []
limit = int(1e9+7)

for _ in range(T):
    n = int(stdin.readline())
    s = list(map(int, stdin.readline()[:-1]))
    total = len(s)
    b = True
    for k in range(n):
        mult = s[k]-1
        if mult == 0: continue
        suf = total-k-1
        add = mult * suf
        _total = total + add
        if b:
            s.extend(mult * s[k+1:])
            if _total >= n:
                b = False
            # if _total > n:
            #     (i,j) = divmod(n-total, suf)
            #     s.extend(i * s[k+1:] + s[k+1:k+1+j])
            #     b = False
            # else:
            #     s.extend(mult * s[k+1:])
        total = _total % limit

    out.append(str(total))

stdout.write('\n'.join(out))
