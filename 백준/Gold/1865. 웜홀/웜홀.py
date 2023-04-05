from collections import deque
t = int(input())
def bf(): #벨만포드
    D = [100000000] *(n+1)
    D[1] = 0
    for i in range(n):
        for g in graph:
            start,goal, time = g
            if D[goal]>D[start] + time:
                D[goal] = D[start]+time
                if i == n-1:
                    return 'YES'
    return 'NO'

for i in range(t):
    n,m,w=map(int,input().split()) # 지점의 수, 도로의 개수, 웜홀의 개수
    graph = [] #도로의 시간저장 / 방향없음 .
    for j in range(m):
        s,e,t = map(int,input().split())
        graph.append([s,e,t])
        graph.append([e, s, t])
    for j in range(w):
        s, e, t = map(int, input().split())
        graph.append([s,e,-t])
    print(bf())