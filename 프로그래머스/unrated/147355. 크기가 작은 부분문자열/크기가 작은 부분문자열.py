def solution(t, p):
    answer = 0
    length = len(list(p))
    p = int(p)
    for i in range(len(t)-length+1):
        if p >= int(t[i:i+length]):
            answer +=1
    return answer