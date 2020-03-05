t = int(input().strip())

def f(n):
    if n < 10:
        return n
    ret = f(n//10)
    t = ret%10+n%10
    return (ret+t//10)*10 + t//10+t%10


for _ in range(t):
    s = int(input().strip())
    print(f(s))
