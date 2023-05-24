def solution(sequence, k): #수열 정수 배열 , 부분수열의 합
    answer = []#부분수열의 시작 인덱스와 마지막 인덱스를 담아 리턴
    left =0
    right =-1
    now = 0
    while True:
        if now <k:
            right +=1
            if right >= len(sequence) : break
            now += sequence [right]
        else:
            now -= sequence[left]
            if left >= len(sequence): break
            left+=1
        if now == k:
            answer.append([left,right]) 
        
    answer.sort(key = lambda x : (x[1]-x[0],x[0]))
    return answer[0]