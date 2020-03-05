import sys, random

dates = {(0,0,0): True}

def gen(num):
    ret = [str(num)]
    for i in range(num):
        day,month,year = 0,0,0
        while (day,month,year) in dates:
            day,month,year = random.randrange(1,30), random.randrange(1,12), random.randrange(1950,1999)
        dates[(day,month,year)] = True
        ret.append("{:0>#02} {} {} {}".format(i, day, month, year))
    return ret




fn = "E:\\Projects\\Programming\\cpp\\birthdates.in"
lines = gen(100)
with open(fn, 'w') as f:
    f.write('\n'.join(lines))
print('\n'.join(lines))
