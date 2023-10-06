import sys
input = sys.stdin.readline
# N개의 공을 K개의 바구니에 나눠 담을 때, 각 바구니에는 1개 이상의 공이 있어야하고,
# 바구니에 담긴 공의 개수가 모두 달라야 함.
# 가장 많이 담긴 바구니와 가장 적게 담긴 바구니의 공의 개수 차이가 최소가 되도록 함.
n,k = map(int,input().split()) #공의 개수, 팀의 수
#가장 많이 담긴 바구니의 공의 개수 차이를 출력
at_least = sum([x for x in range(1,k+1)])
if n< at_least :
    print(-1)
elif (n - at_least) % k == 0:
    print(k-1)
else: print(k)
