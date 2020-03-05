from math import ceil
T = int(input().strip())
for _ in range(T):
    n,g,b = map(int,input().split())
    ans = None
    if g >= b:
        ans = (n//(g+b))*(g+b) + n%(g+b)
    else:
        need = ceil(n/2)
        ans = (need//g)*g + need%g + (ceil(need/g)-1) * b
        ans = max(n, ans)
    print(ans)
