import heapq
def solution(jobs): # [작업이 요청되는 시점, 작업의 소요시간]
    answer = 0 # 작업의 요청부터 종료까지 걸린 시간의 평균
    q=[]
#     for job in jobs:
#         heapq.heappush(q,[job[1],job[0]]) #작업 소요시간, 요청되는 시점 
#     now_time = 0
#     while q:
#         taken_time, start =heappop(q)
        
    for i,job in enumerate(jobs):
        heapq.heappush(q,[job[0],job[0]+job[1],i]) #시작시간, 예상 종료시간, idx
    now_time = 0
    finish =0 #종료한 작업의 요청부터 종료까지 걸린 시간 
    while q:
        start,end,i = heapq.heappop(q) #예상 종료시간, 시작시간, idx
        print("start,end",start,end,i)
        if now_time > start: # 현재 들어온 작업이 있을 경우
            heapq.heappush(q,[now_time,end+now_time-start,i])
        else:
            finish += end-jobs[i][0]
            now_time += jobs[i][1]
            print(finish,now_time)
    return finish//len(jobs)