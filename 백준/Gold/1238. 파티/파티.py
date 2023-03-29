import heapq
import sys
MAX = float('inf')
n,m,x = map(int,sys.stdin.readline().split())# 학생수 , 마을 갯수, 목적지
graph = [[]for _ in range(n)]
for i in range(m):
    a,b,c = map(int,sys.stdin.readline().split())
    graph[a-1].append((c,b-1))
x -=1
final = [0]*n
for i in range(n) :
    q = []
    start = i
    result =[MAX] * n
    heapq.heappush(q,(0,start))
    result[start] = 0
    while q:
        cw,cv = heapq.heappop(q)
        if cw > result[cv]:
            continue
        for nw,nv in graph[cv]:
            cost = cw+nw
            if cost < result[nv]:
                result[nv]= cost
                heapq.heappush(q,(cost,nv))
    if i == x:
        for j in range(n):
            final[j] += result[j]
    else:
        final[i] += result[x]
print(max(final))