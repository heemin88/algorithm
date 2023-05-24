from collections import Counter
def solution(k, m, score): # 사과의 최대 점수 ,한 상자에 담을 사과 갯수
    answer = 0 #최대 이익
    apple_cnt = len(score) #사과 갯수
    dict_score = dict(Counter(score))
    current_apple =0
    while apple_cnt >= m:
        current_apple +=dict_score.get(k,0)
        if current_apple >= m:
            while current_apple >=m:
                answer += k*m
                current_apple -=m
                apple_cnt -= m
        k-=1
        
        
        
        
    return answer