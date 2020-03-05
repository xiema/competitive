from sys import stdin, stdout
from itertools import chain
from collections import deque

T = int(stdin.readline().strip())

for _ in range(T):
    k = int(stdin.readline().strip())
    iter = chain(stdin.readline().split(), stdin.readline().split())
    nums = list(map(int, filter(lambda x : x != "E", iter)))
    one = nums.index(1)
    nums = nums[one:] + nums[:one]

    print(nums)

    odd = False
    for i,v in enumerate(nums):
        if i%2 == v%2:
            odd = not odd

    print(odd)
