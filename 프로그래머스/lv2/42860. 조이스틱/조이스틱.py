def solution(name):
    answer = 0 # 이름에 대해 조이스틱 조작 횟수의 최솟값 
    #65 ~ 90
    # 위 : 다음 알파벳 , 아래 : 이전 알파벳
    # 왼 : 커서를 왼쪽으로 이동 , 오 : 커서를 오른쪽으로 이동
    
    # 맨 처음에 A로만 이루어져 있음.
    cursor = 0 
    a = ord('A') # 65
    length = len(name)
    # 각 자리에서 다른 자리까지 가는 최소 거리 
    remove_a = name.split('A')
    for i,n in enumerate(name):
        tmp= ord(n)-a
        if tmp <14:
            answer += tmp
        else:
            answer += 26-tmp
    if len(remove_a) ==0:
        answer += len(name)-1
    else:
        
    return answer