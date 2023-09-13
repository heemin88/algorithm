import sys
import heapq
import copy
input = sys.stdin.readline
answer = 0  # 상어가 먹을 수 있는 물고기 번호의 합의 최댓값


# 한 칸에는 물고기 한 마리
# 물고기 이동 - 번호가 작은 물고기부터.
# 이동할 수 있는 칸 : 빈칸 / 다른 물고기가 있는 칸
# 물고기는 방향이 이동할 수 있는 칸을 향할 때 까지 45도 회전. 이동 할 수 있는 칸 X -> 이동 X

# ↑, ↖, ←, ↙, ↓, ↘, →, ↗
def move(x, y, direct):
    next_x, next_y = -1, -1
    if direct == 1 and x - 1 >= 0 :
        next_x, next_y = x - 1, y
    elif direct == 2 and x - 1 >= 0 and y - 1 >= 0 :
        next_x, next_y = x - 1, y - 1
    elif direct == 3 and y - 1 >= 0:
        next_x, next_y = x, y - 1
    elif direct == 4 and x + 1 < 4 and y - 1 >= 0 :
        next_x, next_y = x + 1, y - 1
    elif direct == 5 and x + 1 < 4 :
        next_x, next_y = x + 1, y
    elif direct == 6 and x + 1 < 4 and y + 1 < 4 :
        next_x, next_y = x + 1, y + 1
    elif direct == 7 and y + 1 < 4:
        next_x, next_y = x, y + 1
    elif (direct == 8 or direct==0) and y + 1 < 4 and x - 1 >= 0:
        next_x, next_y = x - 1, y + 1
    return next_x, next_y

def switch(x, y, nx, ny,number,x_y,empty):
    fish = x_y[x][y]
    nfish = x_y[nx][ny]
    number[fish][0], number[fish][1] = nx,ny
    number[nfish][0], number[nfish][1] = x,y
    x_y[x][y], x_y[nx][ny] = nfish, fish
    empty[x][y],empty[nx][ny] = empty[nx][ny] , empty[x][y]
    return number,x_y

number = [[] for _ in range(17)]  # 각 번호별 [x,y,direct]

shark_loc = []
shark_dir = 0
x_y = []  # 물고기 테이블
for i in range(4):
    tmp = list(map(int, input().split()))
    x_y.append([tmp[x] for x in range(0, 8, 2)])
    for j in range(8):
        if j % 2 == 0:
            number[tmp[j]] = [i, j // 2]
        else:
            number[tmp[j - 1]].append(tmp[j])


empty=[[False for _ in range(4)]for _ in range(4)]
# 상어 들어옴
shark_loc = [0, 0]  # 현재상어 위치
shark_dir = number[x_y[0][0]][2]  # 현재 상어 방향
answer += x_y[0][0]
empty[0][0] = True

q= []
heapq.heappush(q,[answer,shark_loc,shark_dir,number,x_y,empty])

while q: #상어가 갈 수 있는 모든 경우의 수를 보기 위해.
    count,loc,shark_dir,number,x_y,empty =  heapq.heappop(q)
    answer = max(answer,count)
    # 물고기 이동
    for i in range(1, 17):  # 1번 물고기 부터
        x, y, direct = number[i]
        if empty[x][y] : continue  # 잡아먹힌 물고기 처리
        for k in range(8):
            nx, ny = move(x, y, (direct + k)%8 )
            if (nx,ny) == (loc[0],loc[1]) : continue #상어있는 곳이면
            if (nx, ny) != (-1, -1):  # 물고기 이동 성공
                if direct+k ==8 : number[i][2] = direct+k
                else: number[i][2] = (direct+k)%8
                number,x_y=switch(x, y, nx, ny,number,x_y,empty)
                break
    #상어 이동
    s_x,s_y = loc[0],loc[1]
    while True:
        nx,ny = move(s_x,s_y,shark_dir)
        if (nx, ny) != (-1, -1) :  # 상어 이동 성공
            if not empty[nx][ny] : #빈칸이 아닌지 확인
                tmp_e= copy.deepcopy(empty)
                tmp_e[nx][ny] = True
                heapq.heappush(q,[count+x_y[nx][ny],[nx,ny],number[x_y[nx][ny]][2],copy.deepcopy(number),copy.deepcopy(x_y),tmp_e])
            s_x ,s_y = nx,ny

        else: #실패
            break
print(answer)