import sys
import heapq
import copy
input = sys.stdin.readline
# 한 도시에서 출발해 N개의 도시를 모두 거쳐 다시 원래의 도시로 돌아오는 여
#한 번 갔던 도시로는 다시 갈 수 없음.

answer = float('inf') #가장 적은 비용을 들이는 외판원의 순회 여행 경로를 구하자
n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int,input().split())))
q=[]
visited=[False for _ in range(n)]
visited[0] = True
heapq.heappush(q,[0,0,visited])
while q:
    cost,now,visited =heapq.heappop(q)
    if answer < cost : continue
    if all(visited) and graph[now][0] !=0:
        answer = min(answer,cost+graph[now][0])
    for i,next in enumerate(graph[now]):
        if not visited[i] and next != 0:
            tmp = copy.deepcopy(visited)
            tmp[i]= True
            heapq.heappush(q,[cost+next,i,tmp])

print(answer)

