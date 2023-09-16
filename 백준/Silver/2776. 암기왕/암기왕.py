import sys
import bisect
input = sys.stdin.readline
answer = [] #수첩 1에 값이 있는지 확인
t = int(input())
for _ in range(t):
    n = int(input())
    num = list(map(int, input().split()))
    m = int(input())
    num2 = list(map(int, input().split()))
    num.sort()
    for i in num2:
        tmp = bisect.bisect_left(num, i)
        if tmp <n and num[tmp] == i:
            print(1)
        else:
            print(0)
