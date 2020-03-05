t = int(input().strip())
for _ in range(t):
    k = int(input().strip())
    g = input()
    ai,m = -1,0
    for i,s in enumerate(g):
        if s=='A':
            if ai >= 0:
                m = max(m,i-ai-1)
            ai = i
    else:
        if ai >= 0:
            m = max(m, k-ai-1)
    print(m)
