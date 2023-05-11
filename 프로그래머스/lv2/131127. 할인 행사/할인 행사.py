# 회원등록 - 10일 , 이 기간동안 원 하는 제품을 다 살 수 있는 경우의 수를 다 구하는 문제
from collections import Counter
def solution(want, number, discount):
    answer = 0 # 회원등록시 원하는 제품과 수량을 모두 할인 받을 수 있는 회원 등록 날짜의 총 일수
    product={} #원하는 제품과 수량을 저장하는 딕셔너리
    pro_num = 0 #원하는 제품 수량의 합산
    for i in range(len(want)):
        product[want[i]] = number[i]
        pro_num += number[i]
        
    for i in range(len(discount)):
        if len(discount)-i <10:
            break
        dis = Counter(discount[i:i+10])
        boolean = True
        for j in product:
            if dis[j] != product[j]:
                boolean = False
                break
        if boolean:
            answer +=1
            
        
    
    
    return answer