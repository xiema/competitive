import sys

k = 10000
k2 = 2*k
r = ["1 2 1\n"]
next, i = [2], 2
while i < k2:
    _next = []
    for h in next:
        i+=1
        r.append("{} {} 1\n".format(h, i))
        if i == k2:
            break
        _next.append(i)
        i+=1
        r.append("{} {} 1\n".format(h, i))
        if i == k2:
            break
        _next.append(i)
    next = _next

with open(sys.path[0] + "\\jeremy3.in", 'w') as file:
    file.write("1\n{}\n".format(k))
    file.writelines(r)
