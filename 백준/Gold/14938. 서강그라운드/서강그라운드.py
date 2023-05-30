n,m,r = map(int,input().split()) #지역의 개수, 수색범위, 길의 개수
t = list(map(int,input().split())) #각 구역에 있는 아이템 수
graph =[[]for _ in range(n+1)]
for i in range(r):
    a,b,l = map(int,input().split())
    graph[a].append([b,l]) #상대 번호, 거까지 길이
    graph[b].append([a,l])

answer = 0
check = [False for _ in range(n+1)]
visited=[100 for _ in range(n+1)]
def find_item(n,cnt,item):
    for s,l in graph[n]: #s: 상대편 번호 l : 거기까지의 길이
        if cnt+l <=m and visited[s]>cnt+l :
            visited[s] = cnt + l
            if check[s] == False: #방문 안했을 때만 item더해줌.
                check[s] = True
                item = find_item(s, cnt + l, item + t[s - 1])
            else:
                item = find_item(s,cnt+l,item)
    return item
for i in range(1,n+1): #마을 1번부터 n번까지 돌면서 아이템 개수 구하기
    item = t[i-1]
    visited[i] = 1
    check[i] = True
    answer = max(find_item(i, 0, item),answer)
    visited = [100 for _ in range(n + 1)]
    check = [False for _ in range(n + 1)]
print(answer)
