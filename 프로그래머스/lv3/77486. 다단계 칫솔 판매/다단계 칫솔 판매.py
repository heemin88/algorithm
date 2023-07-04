def solution(enroll, referral, seller, amount): #판매원의 이름 # 각 판매원을 다단계 조직에 참여시킨 다른 판매원의 이름 , 판매량 집계 데이터의 판매원 이름, 판매량 집계 데이터의 판매 수량
    answer = [] #각 판매원이 득한 이익금을 나열 (정수형)
    graph={}
    money ={}
    for i in range(len(referral)):
        graph[enroll[i]]=referral[i] #날 추천한 사람은 무조건 한명임.
        money[enroll[i]] = 0

    for i in range(len(amount)):
        amt = amount[i]*100 # 칫솔값 계산
        sell = seller[i] #판 애 이름.
        while sell !='-':
            if amt<1: break
            tmp = int(amt*0.1)
            money[sell] += amt-tmp # 10% 빼고 자신이득 플러스
            sell = graph[sell]
            amt = tmp
    for key,value in money.items():
        answer.append(value)
    return answer