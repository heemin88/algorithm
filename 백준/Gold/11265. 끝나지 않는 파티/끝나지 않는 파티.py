import sys
input = sys.stdin.readline
#한 파티장 -> 다른 파티장까지 시간 내에 도착할 수 없는지 알아보자 .
#플로이드 와샬 : 모든 정점에서 모든 정점으로 가는 최단 거리를 알고 싶을 때
n,m = map(int,input().split()) #파티장의 크기, 서비스를 요청한 손님의 수
graph = []
answer = []
for _ in range(n):
    graph.append(list(map(int,input().split())))
for i in range(n): #거쳐가는 정점
    for j in range(n): # 출발 정점
        for k in range(n): #도착 정점
            if graph[j][i]+graph[i][k]< graph[j][k]:
                graph[j][k] = graph[j][i]+graph[i][k] 
for _ in range(m):
    a,b,time = map(int,input().split())
    if graph[a-1][b-1] <= time:
        answer.append("Enjoy other party")
    else:
        answer.append("Stay here")
print(*answer,sep="\n")