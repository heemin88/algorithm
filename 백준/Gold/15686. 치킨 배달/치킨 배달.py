# 0 은 빈칸, 1은 집 , 2는 치킨집
from itertools import combinations
n,m = map(int,input().split()) #도시 수 ,최대 치킨집의 개수
city=[]
chicken =[]
home = []
for i in range(n):
    city.append(list(map(int,input().split())))
    for j in range(n):
        if city[i][j] == 2:
            chicken.append((i,j))
        elif city[i][j] ==1:
            home.append((i,j))
answer =float('inf')
for combi in combinations(chicken,m):
    total_distance =0
    for r1,c1 in home:
        distance = float('inf')
        for r2,c2 in combi:
            distance = min(distance,abs(r1-r2) + abs(c1-c2))
        total_distance += distance
    answer = min(total_distance,answer)
print(answer)