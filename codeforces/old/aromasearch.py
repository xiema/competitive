xo,yo,ax,ay,bx,by = map(int,input().split())
xs,ys,t = map(int,input().split())

d1 = 0
d2 = d0 = abs(xo-xs)+abs(yo-ys)
c = 0
while d0 > t:
    xo,yo = ax*xo+bx,ay*yo+by
    _d0 = abs(xo-xs)+abs(yo-ys)
    if _d0 > d0:
        break
    d2 = d0 =_d0
x,y = xo,yo
while d1+d2<=t or d0+d1<=t:
    x,y = ax*x+bx,ay*y+by
    d1 = x-xo + y-yo
    d2 = abs(x-xs)+abs(y-ys)
    c += 1

print(c)
