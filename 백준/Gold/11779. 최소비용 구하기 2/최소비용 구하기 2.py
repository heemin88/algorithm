import heapq
import sys
MAX = float('inf')
n = int(sys.stdin.readline())#도시의 개수
m = int(sys.stdin.readline()) # 버스의 개수
graph = [[]for _ in range(n)]
path =[0]*n
for i in range(m):
    a,b,c = map(int,sys.stdin.readline().split())
    graph[a-1].append((c,b-1))
start , end = map(int,sys.stdin.readline().split())
start -=1 ; end -=1
q = []
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
            path[nv] = cv
            result[nv]= cost
            heapq.heappush(q,(cost,nv))
print(result[end])
p = []
p.append(end+1)
i = end
cnt =1
while i !=start:
    p.append(path[i]+1)
    i = path[i]
    cnt += 1
p.reverse()
print(cnt)
print(*p)
