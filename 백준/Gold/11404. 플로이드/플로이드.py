n = int(input()) #도시의 개수
m = int(input()) # path갯수
MAX = float('inf')
path =[[MAX for _ in range(n)]for _ in range(n)] # path들
for i in range(m):
    a,b,c = map(int,input().split())
    path[a-1][b-1] = min(c,path[a-1][b-1])
for k in range(n): #바로오느냐 vs 어딘가에 거쳐서 오는가
    for i in range(n):
        for j in range(n):
            if i == j : path[i][j] = 0
            path[i][j] = min(path[i][j],path[i][k]+path[k][j])
#출력
for row in path:
    for i in range(n):
        if row[i] ==MAX :
            row[i]= 0
        print(row[i],end=" ")
    print()