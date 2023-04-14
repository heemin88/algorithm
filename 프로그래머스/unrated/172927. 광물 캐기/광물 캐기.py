def solution(picks, minerals): #갖고 있는 곡괭이 개수 , 캐야할 광물의 순서 
    # 곡괭이 종류에 상관없이 광물 5개를 캔 후에는 더 이상 사용할 수 없음(한번 사용하면 사용못할때까지 사용)
    # 광산에 있는 모든 광물을 캐거나, 더 사용할 곡괭이가 없을때까지 곽물 캐기
    answer = 0 # 가장 적은 피로도 다이아곡괭이 > 철 곡괭이 > 돌 곡괭이
    type ={
        "diamond": 0,
        "iron": 1,
        "stone":2}
    #광물순서는 못바꾸지만, 5개씩 끊어서 다이아몬드가 많은 곳에 다이아몬드 곡괭이를 써야하구나
    sccuess=False
    tired = [[1,1,1],[5,1,1],[25,5,1]]
    #광물들을 5개씩 끊기 
    divided =[]
    for i in range(0,len(minerals),5):
        divided.append(minerals[i:i+5])
    #끊은 광물들로 모든 곡괭이에 적용시켜 cost를 구하자.
    costs=[]
    for section in divided:
        cost =[0,0,0] #다이아 곡괭이, 철곡괭이, 돌 곡괭이 
        for m in section:
            if m == "diamond":
                cost[0] += tired[0][0]
                cost[1] += tired[1][0]
                cost[2] += tired[2][0]
            elif m =="iron":
                cost[0] += tired[0][1]
                cost[1] += tired[1][1]
                cost[2] += tired[2][1]
            else:
                cost[0] += tired[0][2]
                cost[1] += tired[1][2]
                cost[2] += tired[2][2]
        costs.append(cost)
    while len(costs)> sum(picks):
        costs.pop() # 곡괭이 수만큼만 실행할 수 있기 때문에
    costd_sorted=sorted(costs,key=lambda x: x[2], reverse=True ) # 돌 곡괭이 기준 큰 값 부터 
    
    for cost in costd_sorted:
        if picks[0]>0:
            answer += cost[0]
            picks[0] -=1
        elif picks[1]>0:
            answer += cost[1]
            picks[1]-=1
        else:
            answer += cost[2]
            picks[2]-=1
    
    # for i, n in enumerate(picks):
    #     for j in range(5*n): #한 곡괭이당 5번 사용할 수 있으므로 
    #         if len(minerals)==0: 
    #             sccuess = True 
    #             break
    #         mineral = minerals.pop(0)
    #         answer+= tired[i][type[mineral]]
    #     if sccuess : break

    return answer