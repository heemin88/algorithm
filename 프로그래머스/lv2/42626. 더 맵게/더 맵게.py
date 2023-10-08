import heapq
def solution(scoville, K): #음식의 스코빌 지수, 원하는 스코빌 지수
    # 모든 음식의 스코빌 지수를 k이상으로 만들기 위해 섞어야 하는 최소횟수 
    q = []
    for s in scoville:
        heapq.heappush(q,s)
    answer = 0
    success = True
    while q:
        a = heapq.heappop(q)
        if a >=K: break #모든 스코빌 지수가 k이상인 경우 -> success
        if len(q) ==0 : #모든 스코빌 지수가 K미만 인 경우 -> false
            success = False 
            break
        b = heapq.heappop(q)
        heapq.heappush(q,a+b*2)
        answer +=1
    if not success : return -1
    return answer