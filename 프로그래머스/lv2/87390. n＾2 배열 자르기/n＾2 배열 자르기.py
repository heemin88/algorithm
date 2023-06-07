def solution(n, left, right):
    answer = []
    cnt =0
    
    for num in range(left,right+1):
        div = num//n +1
        mod = num%n
        if div == mod:
            answer.append(div+1)
        elif div < mod:
            answer.append(mod+1)
        else:
            answer.append(div)
    return answer