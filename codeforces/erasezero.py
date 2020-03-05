t = int(input().strip())
out = []
for _ in range(t):
    cnt,total,b=0,0,False
    for c in input().strip():
        if b:
            if c=='0':
                cnt += 1
            elif c =='1':
                total += cnt
                cnt = 0
        else:
            if c=='1':
                b = True
    out.append(str(total))
print('\n'.join(out))
