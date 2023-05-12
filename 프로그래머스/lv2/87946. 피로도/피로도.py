from itertools import permutations
def solution(k, dungeons):# 현재 피로도, 각 던전별 최소필요 피로도, 소모 피로도가 담긴 2차원 배열
    answer = 0 #유저가 탐험할 수 있는 최대 던전 수 
    dungeons = list(permutations(dungeons,len(dungeons)))
    #print(dungeons)
    for i in range(len(dungeons)):
        now_k = k
        cnt = 0
        for j in dungeons[i]:
            if now_k < j[0] : break #최소 피로도 보다 현재 피로도가 더 적을 경우 
            now_k -=j[1]
            cnt +=1
        answer = max(answer,cnt)
    return answer