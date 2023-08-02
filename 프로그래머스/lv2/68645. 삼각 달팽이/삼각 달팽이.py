def solution(n): # 높이 
    length =0 # 필요한 모든 배열 길이 
    for i in range(1,n+1):
        length +=i
    answer = [0 for _ in range(length)]
    answer[0] =1
    
    i = 0 # index 
    now_depth = 1 # 현재 depth
    num = 2 # 저장할 숫자
    finish = length 
    while num <= finish:
        while now_depth <n: # 깊이 n까지 내려가기 (아래로 이동)
            answer[i +now_depth] = num
            i = i+now_depth
            now_depth +=1
            num +=1
        
        while i+1 < length and answer[i+1] == 0 : # 값이 0이면서 길이가 해당 높이의 길이까지 (옆으로 이동)
            answer[i+1] = num
            i=i+1
            num +=1
        length -= now_depth # 길이 감소 
        
        while answer[i-now_depth] ==0: # 값이 0이 아닐 때 까지 올라가기 (위로 이동)
            answer[i-now_depth] = num
            i = i-now_depth
            now_depth -=1
            num +=1
        n -=1
    return answer