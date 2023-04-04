n,m = map(int,input().split()) #가수 수 , PD수
graph =[[] for _ in range(n+1)]
visited=[False for _ in range(n+1)]
finished=[False for _ in range(n+1)]
for i in range(m):
    tmp =list(map(int, input().split()))
    for j in range(1,tmp[0]):
        graph[tmp[j]].append(tmp[j+1])
order=[]
cycle = False
def dfs(k):
    global cycle
    visited[k] = True
    for num in graph[k]:
        if not visited[num]:
            dfs(num)
        elif not finished[num]:
            print(0)
            exit()
    order.append(k)
    finished[k]=True

for i in range(1,n+1):
    if not visited[i]:
        dfs(i)

order.reverse()
for i in order:
    print(i)
