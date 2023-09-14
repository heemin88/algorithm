import sys
input = sys.stdin.readline
n = int(input())
map = list(input())
# E : (1, x+1)
# W : (1, x-1)
visited=[False for _ in range(n)]
answer = 0
def dfs(x):
    visited[x] = True
    if map[x] == 'E' and not visited[x+1]:
        dfs(x+1)
        return x+1
    elif map[x] == 'W' and not visited[x-1]:
        dfs(x-1)
        return x-1
    return -1
for i in range(n):
    if visited[i] : continue
    if dfs(i) != -1:
        answer +=1
print(answer)