from sys import stdin,stdout
from math import sqrt
from collections import Counter

primes,primes_list = set([2]),None
composites = set()

def gen_primes(n):
    for i in range(3,n+1,2):
        if i not in composites:
            primes.add(i)
            for j in range(i*2,n+1,i):
                composites.add(j)

def get_fact(n):
    fact = []
    if n not in primes:
        for p in primes_list:
            if n%p==0:
                c = 0
                while n%p==0:
                    n//=p
                    c+=1
                fact.append((p,c))
                if n==1:
                    break
                elif len(fact) > 1:
                    fact.append((n,1))
                    break
        else:
            fact.append((n,1))
    return fact


t = int(stdin.readline().strip())
ns = [int(stdin.readline().strip()) for _ in range(t)]
gen_primes(int(sqrt(max(ns)))+1)
primes_list = list(primes)
primes_list.sort()
#print(primes_list)

for n in ns:
    fact = get_fact(n)
    #print(n,fact)
    div = []
    if len(fact) == 3 or (len(fact) == 2 and fact[0][1]+fact[1][1]-2 > 1):
        a,b = fact[0][0],fact[1][0]
        div = [a,b,(n//a)//b]
    elif len(fact) == 1 and fact[0][1] >= 6:
        a = fact[0][0]
        b = a*a
        div = [a,b,(n//a)//b]

    if div:
        stdout.write("YES\n{} {} {}\n".format(*div))
    else:
        stdout.write("NO\n")
