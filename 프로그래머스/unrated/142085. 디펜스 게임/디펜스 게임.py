import heapq
def solution(n, k, enemy): # 가지고 있는 병사수, 무적권 횟수, 적의 수
    answer = 0 #막을 수 있는 라운드
    # if len(enemy)<= k: return len(enemy) #무적권사용할 수 있는 횟수보다 라운드수가 같거나 작으면 라운드수만큼 이김.
    q=[]
    for e in enemy:
        heapq.heappush(q,-e)
        if e > n: # 가지고 있는 병사수마다 적의 수가 더 많으면 
            if k !=0 and len(q)!=0: # 무적권 횟수가 남아 있고, 큐에 값이 있다면
                n += -heapq.heappop(q) #내 병사수만 큼 더해줌.
                k-=1#무적권 횟수 하나 차감.
            else: break
        n -=e
        answer +=1
    return answer