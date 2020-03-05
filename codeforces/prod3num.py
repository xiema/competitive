from sys import stdin,stdout

primes = set()
composites = {}

def gen_primes(n):
    for i in range(2,n+1):
        if i not in composites:
            primes.add(i)
            for j in range(i*2,n+1,i):
                composites.setdefault(j, set()).add(i)

t = int(stdin.readline().strip())
ns = [int(stdin.readline().strip()) for _ in range(t)]
gen_primes(max(ns))

lines = []
for n in ns:
    if n in primes:
        lines.append("NO\n")
        continue

    div = list(composites[n])
    if len(div) < 2:
        a = div[0]
        b = a*a
        c = a*b
        if n >= c*c:
            lines.append("YES\n{} {} {}\n".format(a, b, n//c))
    elif len(div) < 3:
        n = (n//div[0])//div[1]
        if n not in div:
            lines.append("YES\n{} {} {}\n".format(div[0],div[1],n))
        else:
            lines.append("NO\n")
    else:
        c = 1
        for i in div[2:]:
            c *= i
        lines.append("YES\n{} {} {}\n".format(div[0],div[1],c))


stdout.writelines(lines)
