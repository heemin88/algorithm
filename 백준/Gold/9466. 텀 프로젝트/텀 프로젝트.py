import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
t = int(input())
def dfs(k):
    global cycle
    if visited[k]:
        return team #이미 방문했던 곳 -> 실패
    if select[k]==k+1: return team # 선택된애랑 나랑 같다면 -> 실패
    visited[k]=True
    team.append(k)
    check.add(k)
    if select[k]-1 in check:# 사이클이 만들어진 경우
        team.append(select[k]-1)
        cycle = select[k]-1
        return team
    dfs(select[k]-1)
    return team
for i in range(t):
    n = int(input()) #학생수
    select=[]
    select = list(map(int,input().split()))
    result = n
    visited = [False for _ in range(n)]
    for j in range(n):
        if visited[j] : continue
        team = []
        check = set([])
        cycle = 0
        if select[j]==j+1: #자기 자신을 선택하는 경우
            result -=1
            continue
        team = dfs(j)
        if len(team) !=0 and team[0]==team[len(team)-1]:#성공했다면
            result -= len(team)-1
        else: #실패했다면
            if cycle : #사이클이 존재하지만 실패
                visited[team[len(team)-1]]=False
                for k in range(len(team)-2,-1,-1):
                    if team[k] == cycle : break
                    visited[team[k]]= False
            # else:
            #     for k in team :
            #         visited[k]=False
    print(result)