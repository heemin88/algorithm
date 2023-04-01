import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)
n = int(input())
graph = [[] for _ in range(n+1)]
for i in range(n-1):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
result=[0 for _ in range(0,n+1)]

def dfs(start):
    for num in graph[start]:
        if result[num] ==0:
            result[num] = start
            dfs(num)
dfs(1)
for i in range(2,n+1):
    print(result[i])