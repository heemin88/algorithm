def solution(sequence, k):
    answer = []
    right = len(sequence)-1
    left =right
    result =sequence[right]
    length =1000001
    while left>=0:
        if result > k: # 값이 더 커졌을 때, 다시 초기화 
            result -=sequence[right]
            right -=1
        if result == k:# 값이 같을 때, 저장된 길이보다 짧으면 값 넣기
            if length >= right-left:
                result -= sequence[right]
                answer.append([left,right])
                length = right-left
                right -=1
                
        left -=1
        result += sequence[left]
    num_min = length
    final =[10000,10000]
    
    answer.sort()
    for num,num2 in answer:
        if num2-num == length:
            return [num,num2]
    