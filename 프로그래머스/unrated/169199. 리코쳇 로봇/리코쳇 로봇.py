from copy import deepcopy
max = 987654321
answer =  max
def solution(board):
    # R - 로봇 처음 위치, D - 장애물 위치, G- 목표지점
    location_r =[]
    for i,b in enumerate(board):
        board[i]=list(b)
        for j,bb in enumerate(board[i]):
            if bb =='R':
                location_r=[i,j]
    dx=[0,0,-1,1] 
    dy=[-1,1,0,0]
    h = len(board) #세로
    w = len(board[0]) #가로
    visited=[[max for _ in range(w)]for _ in range(h)]
    def search(x,y,cnt): 
        global answer
        #print(x,y,cnt,answer)
        if answer <= cnt: return
        if board[x][y]== 'G':
            answer = min(answer,cnt)
            return
        for i in range(4):
            xx = x+dx[i]
            yy= y+dy[i]
            if 0<=xx<h and 0<=yy<w and board[xx][yy] != 'D':
                nx,ny = xx,yy
                while True: # D를 만나거나 게임판 끝까지 갈때까지 이동 
                    nx += dx[i]
                    ny += dy[i]
                    if not 0<=nx<h or not 0<=ny<w : break
                    if board[nx][ny]=='D' : break
                nx -=dx[i]
                ny -=dy[i]
                if visited[nx][ny] <= cnt+1 : continue # 이전에 방문했는데 길이가 더 짧을때 거친 경우
                visited[nx][ny]= cnt +1
                search(nx,ny,cnt+1) #이동한 시점부터 다시 재귀 
    visited[location_r[0]][location_r[1]]=0
    search(location_r[0],location_r[1],0)
    
    if answer == max: return -1
    else : return answer    
