result=float('inf')
def solution(numbers):
    global result
    # 같은 자리 1/상하좌우 2/ 대각선 3
    numbers= list(map(int,list(numbers)))
    answer = 0
    board = [[1,2,3],[4,5,6],[7,8,9],[-1,0,-1]]
    cur_left = [1,0] # x,y
    cur_right = [1,2]
    dx= [1,-1,0,0]
    dy = [0,0,-1,1]
    def move(x,y,cnt,n):
        global result
        if board[x][y]==n: 
            result = min (result,cnt)
            return 
        for i in range(4):
            xx = x+dx[i]
            yy = y+dy[i]
            if 0<=xx<4 and 0<=yy<3 and not visited[xx][yy]:
                visited[xx][yy]= True
                move(xx,yy,cnt+2,n)
                visited[xx][yy]= False
    for i in range(len(numbers)):
        for j in range(3):
            for k in range(3):
                if board[j][k] == numbers[i]:
                    numbers[i] = [j,k]
    for x,y in numbers:
        visited=[[False for _ in range(3)]for _ in range(4)]
        if board[x][y] == board[cur_left[0]][cur_left[1]] or board[x][y] == board[cur_right[0]][cur_right[1]]: #같은 자리
            answer +=1
            continue
        #둘중 더 가까운 곳 계산하기 (상하좌우) -> 대각선
        d1 = abs(x-cur_left[0]) + abs(y-cur_left[1])
        d2 = abs(x-cur_right[0]) + abs(y-cur_right[1])
        result=float('inf')
        if d1 < d2:
            move(cur_left[0],cur_left[1],0,board[x][y])
            answer += result
            print(answer,'left')
            cur_left = [x,y]
        else:
            move(cur_right[0],cur_right[1],0,board[x][y])
            answer += result
            print(answer,'right')
            cur_right = [x,y]
        
    return answer