def solution(n, k, cmd):  # 행 개수, 처음 행 위치, 수행한 명령어
    table = []  #내 아래 인덱스, 내 위 인덱스
    for i in range(n):
        if i ==0 : table.append([i+1,None])
        elif i==n-1 : table.append([None,i-1])
        else: table.append([i + 1, i - 1])
    delete = []  # 삭제된 행 인덱스
    loc = k  # 선택된 행 인덱스
    answer = ["O" for _ in range(n)]
    for c in cmd:
        if c == "C":  # 삭제
            answer[loc]= "X"
            d,u = table[loc]
            delete.append([loc,d,u]) #인덱스,아래행,윗행
            if u == None: # 맨 윗 행이 삭제된다면
                table[d][1] = None # 내 밑행의 위행은 아무것도 없는 것.
                loc = table[loc][0]
            elif d==None:  # 마지막 행일 경우
                table[u][0] = None  
                loc = table[loc][1] # 내 윗행
            else:
                table[d][1] = u
                table[u][0] = d
                loc = table[loc][0] # 내 아랫행
        elif c == "Z":  # 삭제 취소
            tmp,d,u = delete.pop()  # 가장 최근에 삭제한
            answer[tmp] = "O"
            if u==None:
                table[d][1] = tmp
            elif d == None:
                table[u][0] = tmp
            else:
                table[u][0] = tmp
                table[d][1] = tmp

        else:
            a, b = c.split()
            if a == "D":
                for i in range(int(b)):
                    loc = table[loc][0]
            elif a == "U":
                for i in range(int(b)):
                    loc = table[loc][1]
    
    
    return ''.join(answer)