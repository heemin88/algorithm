import sys
from itertools import combinations

def dfs(round):
    global cnt
    if round ==15 : #모든 경기가 다 끝나면
        cnt = 1
        for r in res:
            if sum(r) !=0:
                cnt = 0
                break
        return
    team1,team2 = games[round]
    for x,y in [(2,0),(1,1),(0,2)]:
        if res[team1][x] !=0 and res[team2][y] !=0:
            res[team1][x]-=1
            res[team2][y]-=1
            dfs(round+1)
            res[team1][x] += 1
            res[team2][y] += 1


input = sys.stdin.readline
games = list(combinations(range(6),2))
answer =[]
for _ in range(4):
    tmp = list(map(int, input().split()))
    res = [tmp[i:i+3] for i in range(0,16,3)]
    cnt = 0
    dfs(0)
    answer.append(cnt)
print(*answer)