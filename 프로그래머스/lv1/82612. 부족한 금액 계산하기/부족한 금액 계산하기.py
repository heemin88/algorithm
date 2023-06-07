def solution(price, money, count): #놀이기구 이용료, 현재 금액, 이용횟수
    answer = 0
    for i in range(1,count+1):
        answer += price*i
    if answer-money <0:
        return 0
    return answer-money