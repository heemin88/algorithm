import heapq #priority 큐 사용을 위함.
def solution(n, roads, sources, destination):
    #총 지역의 수, 길 정보, 부대원이 위치한 지역들, 강철부대 지역
    answer = [-1 for _ in range(n+1)] # sources의 원소 순서대로 강철 부대로 복귀할 수 있는 최단 시간을 담아서 리턴
    graph =[[] for _ in range(n+1)]
    count = len(sources)
    for a,b in roads:
        graph[a].append(b)
        graph[b].append(a)
    q =[]
    #visited=[[False for _ in range(n+1)] for _ in range(n+1)] #출발지 마다 다른 visited처리를 위해 이차원
    heapq.heappush(q,[0,destination]) #도착번호를 큐에 넣음
    visited=[False for _ in range(n+1)]
    visited[destination]=True
    while q:
        cnt,num= heapq.heappop(q)
        if num in sources:
            answer[num] = cnt
            count -=1
            if count ==0: break
        for i in graph[num]:
            if not visited[i]:
                visited[i] = True
                heapq.heappush(q,[cnt+1,i])
    
    # for num in sources:
    #     heapq.heappush(q,[0,num,num]) #거리, 번호, 시작번호
    #     visited[num][num]=True
    # while q:
    #     cnt,num,start = heapq.heappop(q)
    #     print(num,start)
    #     if num == destination:
    #         answer[start] = cnt 
    #         count-=1
    #         if count == 0: break
    #         continue
    #     for i in graph[num]:
    #         if not visited[start][i]:
    #             visited[start][i]=True
    #             heapq.heappush(q,[cnt+1,i,start])
    result =[]
    for i in sources:
        result.append(answer[i])
    return result