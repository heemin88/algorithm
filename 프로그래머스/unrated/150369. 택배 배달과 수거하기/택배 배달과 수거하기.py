def solution(cap, n, deliveries, pickups):#트럭에 실을 수 있는 상자 수, 배달할 집의 개수, 각 집에 배달할 택배 상자 개수, 수거할 상자 개수
    #트럭에는 재활용 택배 상자를 최대 cap개 실을 수 있음.
    #각 집에 배달 및 수거할 때, 원하는 개수만큼 택배를 배달 및 수거할 수 있음.
    answer = 0 # 트럭 하나로 모든 배달과 수거를 마치고 물류 창고까지 돌아올 수 있는 최소 이동 거리
    d_cnt = 0
    p_cnt =0
    for i in range(len(deliveries)-1,-1,-1): # i는 배달 갈 가장 끝 집 위치를 나타냄
        d_cnt -= deliveries[i] #배달할 택배 상자 갯수 
        p_cnt -= pickups[i]
        #print(d_cnt,p_cnt ,i)
        cnt = 0
        while d_cnt <0 or p_cnt <0:
            d_cnt += cap
            p_cnt += cap
            cnt +=1
        answer += (i+1)*2*cnt
    return answer