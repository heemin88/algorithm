# from collections import Counter
def solution(N, stages):# 전체 스테이지 개수, 현재 멈춰있는 스테이지의 번호
    # 실패율 : 스테이지 도달 but 클리어 x / 스테이지에 도착한 플레이어 수
    answer = []
    stages.sort()
    for i in range(N):
        if len(stages) ==0 : 
            answer.append([0,i+1])
            continue
        p = stages.count(i+1)
        fail = p/len(stages)
        stages =stages[p:]
        answer.append([-fail,i+1])
    answer.sort()
    return [x[1] for x in answer]