from sys import stdin,stdout
from math import sqrt,floor

def ispow2(n):
    while n%2==0:
        n/=2
    return n==1

def isprime(n):
    if n%2==0:
        return False
    limit = floor(sqrt(n)) + 1
    for f in range(3,limit,2):
        if n%f==0:
            return False
    return True


t = int(stdin.readline().strip())

for _ in range(t):
    n = int(stdin.readline().strip())
    if n==1:
        stdout.write("FastestFinger\n")
    elif n==2 or n%2: #odd
        stdout.write("Ashishgup\n")
    elif ispow2(n): #power of 2
        stdout.write("FastestFinger\n")
    else:
        n/=2
        if isprime(n): #single 2 in factorization
            stdout.write("FastestFinger\n")
        else:
            stdout.write("Ashishgup\n")
