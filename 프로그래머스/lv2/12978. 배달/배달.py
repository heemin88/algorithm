import heapq
def solution(N, road, K): # 마을 개수, 도로 정보(a,b,c) , 음식 배달이 가능한 시간
    # n개의 마을 중에서 k시간 이하로 배달이 가능한 마을에서만 주문을 받음. 
    answer = 0 #음식을 받을 수 있는 마을의 개수 
    graph=[[] for _ in range(N+1)]
    for i in road: #road정보들을 그래프 형태로 저장하기 위함 .
        a,b,time = i[0],i[1],i[2]
        graph[a].append([b,time]) 
        graph[b].append([a,time]) #양방향이므로
    q = []
    visited = [False for _ in range(N+1)]
    heapq.heappush(q,[0,1]) 
    while q:
        cnt,num = heapq.heappop(q) #걸리는 시간, 마을 번호 
        if visited[num]: continue
        visited[num] = True 
        if cnt > K : # 걸리는 시간이 배달 가능한 시간보다 크면 
            continue
        #print(cnt,num)
        answer += 1
        for i in graph[num]:
            if not visited[i[0]]:
                heapq.heappush(q,[cnt + i[1] ,i[0]]) 
    return answer