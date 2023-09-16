import sys
from itertools import combinations
input = sys.stdin.readline
n,m = map(int,input().split())
num = list(map(int,input().split()))
num.sort()
num = list(set(combinations(num,m)))
num.sort()
for i in num:
    print(*i)