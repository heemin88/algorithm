import copy
n, m = map(int, input().split())  # 세로크기 , 가로크기
vmap = []
result =[]
def virus_generation(i, j,temp,visited):
    visited[i][j] = True
    temp[i][j] = 2
    if i > 0 and not visited[i-1][j] and temp[i - 1][j] == 0:  # 상
        virus_generation(i - 1, j,temp,visited)
    if i < n-1 and not visited[i+1][j] and temp[i + 1][j] == 0:  # 하
        virus_generation(i + 1, j,temp,visited)
    if j < m-1 and not visited[i][j+1] and temp[i][j + 1] == 0:  # 오른
        virus_generation(i, j + 1,temp,visited)
    if j > 0 and not visited[i][j-1] and temp[i][j - 1] == 0:  # 왼
        virus_generation(i, j - 1,temp,visited)
def wall (cnt):
    if cnt ==3:
        temp = copy.deepcopy(vmap)
        visited = [[False for _ in range(m)] for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if vmap[i][j] == 2:
                    virus_generation(i,j,temp,visited)
        cnt2 = 0
        for i in range(n):
            cnt2 += temp[i].count(0)
        result.append(cnt2)
        return
    for i in range(n):
        for j in range(m):
            if vmap[i][j] ==0:
                vmap[i][j] = 1
                wall(cnt+1)
                vmap[i][j] = 0

for i in range(n):
    vmap.append(list(map(int, input().split())))
wall(0)
print(max(result))