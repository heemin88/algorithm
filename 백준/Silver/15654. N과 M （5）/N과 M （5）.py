import sys
from itertools import permutations
n,m = map(int,sys.stdin.readline().split())
num = list(map(int,sys.stdin.readline().split()))
num.sort()
if m ==1:
    for i in num:
        print(i)
else:
    num =list(permutations(num,m))
    for i in num:
        print(*i)

