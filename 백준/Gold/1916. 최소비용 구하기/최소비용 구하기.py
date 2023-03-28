import heapq

MAX = int(1e9)
n = int(input()) #도시의 개수
m = int(input()) # 버스의 개수
graph = [[]for _ in range(n)]
for i in range(m) :
    a,b,c = map(int,input().split())
    graph[a-1].append((b-1,c))
start ,end = map(int, input().split())
start -=1
end -=1

queue = []
heapq.heappush(queue,(0,start))
node = [MAX]*n #출발지에서 가는 최솟값들을 저장
node[start]=0
while queue:
    cdistance, cnode = heapq.heappop(queue)
    if cdistance > node[cnode]: # 이미 처리 되어있는 경우
        continue
    for nx, nd in graph[cnode]:
        dis = node[cnode] + nd
        if dis < node[nx]:
            node[nx] = dis
            heapq.heappush(queue,(dis,nx))
print(node[end])