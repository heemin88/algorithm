import heapq
import sys

MAX = float('INF')
v, e = map(int, sys.stdin.readline().split())  # 정점의 개수, 간선의 개수
start = int( sys.stdin.readline()) - 1  # 시작 정점의 번호
graph = [[] for _ in range(v)]
for i in range(e):
    a, b, c = map(int,  sys.stdin.readline().split())
    graph[a - 1].append((c, b - 1))
q = []
result = [MAX] * (v)  # 최단 경로 저장
result[start] = 0
heapq.heappush(q, (0, start))
while q:
    cw, cv = heapq.heappop(q)
    if result[cv] < cw:
        continue
    for nw, nv in graph[cv]:
        cost = cw + nw
        if result[nv] > cost:
            result[nv] = cost
            heapq.heappush(q, (cost, nv))
for r in result:
    if r == float('inf'): print('INF')
    else: print(r)
