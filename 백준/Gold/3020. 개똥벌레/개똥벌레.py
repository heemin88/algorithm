import sys
input= sys.stdin.readline
# 개똥벌레가 파괴해야하는 장애물의 최솟값, 그러한 구간이 총 몇 개 있는지 구해보자.
n,h = map(int,input().split()) #가로, 세로 길이 (가로는 무저건 짝수 )
obstacle_top = [0 for _ in range(h+1)]
obstacle_down = [0 for _ in range(h+1)]
for i in range(n):
    if i%2==0:
        obstacle_down[int(input())] +=1
    else:
        obstacle_top[int(input())] +=1
for i in range(h-1,0,-1):
    obstacle_down[i]+= obstacle_down[i+1]
    obstacle_top[i]+= obstacle_top[i+1]
min_cost = n
min_count = 0
for i in range(1,h+1):
    if min_cost > obstacle_down[i]+obstacle_top[h-i+1]:
        min_cost = obstacle_down[i]+obstacle_top[h-i+1]
        min_count =1
    elif min_cost == obstacle_down[i]+obstacle_top[h-i+1]:
        min_count+=1
print(min_cost, min_count)
