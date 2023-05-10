import heapq
def solution(maps):
    # 각 칸은 통로 또는 벽
    # 레버를 당겨야만 문으로 나갈 수 있음.
    answer = -1
    start =[]
    end =[]
    lever =[]
    h,w = len(maps),len(maps[0])
    visited=[[False for _ in range(w)]for _ in range(h)]
    graph = [[1 for _ in range(w)]for _ in range(h)]
    for i ,st in enumerate(maps): # 출발지, 레버, 탈출지 위치 찾고, X인 부분 그래프에서 0으로 초기화
        for j, s in enumerate(st):
            if s == 'S':
                start=[i,j]
            elif s == 'E':
                end = [i,j]
            elif s == 'L':
                lever = [i,j]
            elif s == 'X':
                graph[i][j] = 0
    dx=[-1,1,0,0]
    dy =[0,0,-1,1]
    q = []
    heapq.heappush(q,[0,start[0],start[1]]) # 거리, x, y => 거리가 짧은 순대로 꺼내지도록
    result =0
    visited[start[0]][start[1]]=True
    
    while q: # 출발지점 -> 레버까지 최단거리
        cnt,x,y = heapq.heappop(q)
        if x==lever[0] and y == lever[1]: #레버에 도착했다면 
            result = cnt
            break
        for i in range(4):
            xx = x+dx[i]
            yy = y+dy[i]
            if 0<=xx<h and 0<=yy<w and not visited[xx][yy] and graph[xx][yy]:
                visited[xx][yy]=True
                q.append([cnt+1,xx,yy])
    if result == 0 : #lever까지 갈 수 없는 경우 -> 탈출 불가
        return answer
    q = []
    heapq.heappush(q,[result,lever[0],lever[1]])
    visited=[[False for _ in range(w)]for _ in range(h)]
    visited[lever[0]][lever[1]]=True
    while q: # 레버에서 출구까지 최단 거리
        cnt,x,y = heapq.heappop(q)
        if x==end[0] and y == end[1]:
            answer = cnt
            break
        for i in range(4):
            xx = x+dx[i]
            yy = y+dy[i]
            if 0<=xx<h and 0<=yy<w and not visited[xx][yy] and graph[xx][yy]:
                visited[xx][yy]=True
                q.append([cnt+1,xx,yy])
    return answer