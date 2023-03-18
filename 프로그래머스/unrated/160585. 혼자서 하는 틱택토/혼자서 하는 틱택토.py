def solution(board):
    for i in range(len(board)):
        board[i] = list(board[i])
    ch = False
    o_arr=[]
    x_arr =[]
    for i in range(3):
        for j in range(3):
            if board[i][j] == "O":
                o_arr.append([i,j])
            elif board[i][j] == "X":
                x_arr.append([i,j])
    if len(o_arr)-len(x_arr) >1 or len(o_arr)-len(x_arr) <0 or len(o_arr)>5 or len(x_arr)>4:
        return 0
    o_bool=check(o_arr)
    x_bool = check(x_arr)
    if x_bool and o_bool : # 둘다 승리했을 경우 
        return 0
    elif o_bool: # o 로 인해 게임이 끝났을 경우 
        if len(o_arr)<= len(x_arr): # 게임이 끝나도 계속 진행했을 경우 
            return 0
    elif x_bool:# x로 인해 게임이 끝났을 경우 
        if len(o_arr) != len(x_arr):
            return 0
    return 1
def check(arr):
    for i in range(len(arr)):
        if [i,0] in arr and [i,1] in arr and [i,2]: #세로  
            return True
        if [0,i] in arr and [1,i] in arr and [2,i] : #가로
            return True
    if [0,0] in arr and [1,1] in arr and [2,2] in arr:
        return True
    elif [2,0] in arr and [1,1] in arr and [0,2] in arr:
        return True
    
    return False
    