n = int(input())
home =[]
result =0
visited=[[False for _ in range(n)]for _ in range(n)]
def move(left_x,left_y,right_x,right_y):
    global result
    #print(left_x,left_y,right_x,right_y)
    if right_x== n-1 and right_y == n-1:
        result += 1
        return
    #가로일 때
    if left_x == right_x:
        #가로로 이동
        if right_y +1<n and home[right_x][right_y+1] != 1:
            move(right_x,right_y,right_x,right_y+1)
            # 대각선으로 이동
            if right_x+1 <n and home[right_x+1][right_y] !=1 and home[right_x+1][right_y+1] !=1:
                move(right_x,right_y,right_x+1,right_y+1)
    # 세로일 때
    elif left_y == right_y:
        #세로로 이동
        if right_x+1 <n and home[right_x+1][right_y] != 1:
            move(right_x,right_y,right_x+1,right_y)
            #대각선으로 이동
            if right_y+1 <n and home[right_x][right_y+1] !=1 and home[right_x+1][right_y+1] !=1:
                move(right_x,right_y,right_x+1,right_y+1)
    #대각선일 때
    else:
        #가로로 이동
        if right_y +1<n and home[right_x][right_y+1] != 1:
            move(right_x,right_y,right_x,right_y+1)
            # 대각선으로 이동
            if right_x+1 <n and home[right_x+1][right_y] !=1 and home[right_x+1][right_y+1] !=1:
                move(right_x,right_y,right_x+1,right_y+1)
        #세로로 이동
        if right_x+1 <n and home[right_x+1][right_y] != 1:
            move(right_x,right_y,right_x+1,right_y)
for i in range(n): # 0,0 -> n,n
    home.append(list(map(int,input().split())))
if home[n-1][n-1] ==1 : print(result)
else:
    move(0,0,0,1)
    print(result)