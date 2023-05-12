import math
def solution(fees, records): # 주차 요금(기본시간, 기본요금,단위시간,단위요금) , 자동차의 입/출력 내역
    answer = [] # 차량 번호가 작은 자동차부터 '청구할 주차 요금'을 담아서 리턴하자.
    cars = {}
    for i,record in enumerate(records):
        tmp = record.split()
        a,b = map(int,tmp[0].split(":"))
        time = b+a*60 
        if cars.get(int(tmp[1]),0)==0: 
            cars[int(tmp[1])]=[[time,tmp[2]]]
        else:
            cars[int(tmp[1])].append([time,tmp[2]])
    for car in cars.items():
        all_time = 0 
        count = 0
        for time,in_out in car[1]:
            if in_out == "IN":
                all_time -= time
            else:
                all_time +=time
            count +=1
        if count%2 !=0: # 출차가 안됐다면 
            all_time += 1439
        if all_time >fees[0] :
            answer.append([car[0],math.ceil((all_time-fees[0])/fees[2])*fees[3]+fees[1]])
        else: #기본요금
            answer.append([car[0],fees[1]])
    answer.sort()
    for i in range(len(answer)):
        answer[i] = answer[i][1]
    return answer