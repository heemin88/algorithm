from collections import deque
def solution(places):
    # 맨해튼 거리가 2 이하로 앉으면 안됨 .
    def calDistance(r1,c1,r2,c2):
        return abs(r1-r2) + abs(c1-c2)
    def bfs(startX,startY,finishX,finishY,place):
        q = deque([])
        q.append([startX,startY,0])
        dx = [1,-1,0,0]
        dy = [0,0,-1,1]
        visited= [[False for _ in range(5)] for _ in range(5)]
        visited[startX][startY] = True
        while q:
            x,y,cnt = q.popleft()
            if cnt>2: continue;
            if (x,y) == (finishX,finishY):
                return True
            for i in range(4):
                nx = x+dx[i]
                ny = y+dy[i]
                if 0<=nx<5 and 0<=ny<5 and place[nx][ny] == "O" and not visited[nx][ny]:
                    visited[nx][ny] = True
                    q.append([nx,ny,cnt+1])
        return False
    answer = [] # 각 대기실 별로 거리두기를 지키고 있으면 1, 한 명이라도 지키지 않고 있으면 0
    # P : 응시자 O : 빈 테이블 X : 파티션
    for place in places:
        p_location = []
        for i in range(5):
            for j in range(5):
                if place[i][j] == 'P':
                    p_location.append([i,j])
        success = True
        for i in range(len(p_location)):
            x,y = p_location[i][0],p_location[i][1]
            for j in range(i+1, len(p_location)):
                nx,ny = p_location[j][0],p_location[j][1]
                if calDistance(x,y,nx,ny) ==1 :
                    success= False
                    break
                elif calDistance(x,y,nx,ny) ==2 :
                    if (x==nx and place[x][y+1] == "O") or (y==ny and place[x+1][y] == "O") or (place[x][ny]=="O") or (place[nx][y]=="O"):
                        success=False 
                        break
                    # if bfs(x,y,nx,ny,place):
                    #     success= False
                    #     break
            if not success : break
                    
        if success : 
            answer.append(1)
        else: answer.append(0)
    return answer