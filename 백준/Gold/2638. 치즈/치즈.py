import sys
sys.setrecursionlimit(10**4)
input = sys.stdin.readline
n,m = map(int,input().split()) #모눈종이 크기
#치즈가 모두 녹아 없어지는데 걸리는 시간
answer = 0
cheese =[]
dx =[-1,1,0,0]
dy = [0,0,-1,1]
c_cnt=0
for i in range(n):
    cheese.append(list(map(int,input().split())))
    for j in cheese[i]:
        if j == 1:
            c_cnt+=1
visited = [[False for _ in range(m)] for _ in range(n)]
def in_space(x,y): #외부 공기 표시
    cheese[x][y] = -1
    visited[x][y]=True
    for i in range(4):
        xx = x+dx[i]
        yy = y+dy[i]
        if 0<=xx < n and 0<=yy<m and cheese[xx][yy]==0 and not visited[xx][yy]:
            in_space(xx,yy)
def check(x,y): #상하좌우 중 두곳이 0인지 확인하는 함
    cnt = 0
    for i in range(4):
        if cnt >= 2: return True
        xx = x+dx[i]
        yy = y+dy[i]
        if cheese[xx][yy] == -1 :
            cnt +=1
    if cnt >= 2: return True
    return False
in_space(0,0) # 외부 공기 -1처리
while c_cnt >0:
    count =0
    tmp =[]
    for i in range(1,n-1):
        for j in range(1,m-1):
            if cheese[i][j] == 1:
                if check(i,j):
                    tmp.append([i,j])
                    c_cnt -=1
    for x,y in tmp:
        in_space(x,y)
    #print(cheese)
    answer +=1

print(answer)