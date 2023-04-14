#엘리베이터가 위치해 있는 층과 버튼의 값을 더한 결과가 0보다 작으면 엘리베이터는 움직이지 않습니다.
def solution(storey): #현재 민수가 있는 층 
    #[-1,+1,-10,10, ...]
    answer = 0 #필요한 마법의 돌 최솟값 
    now = storey
    i=0
    while now != 0:
        n= now%10
        print(n)
        if n >5: 
            answer += 10-n
            now += 10-n
        elif n==5 and (now//10)%10 >=5:
            answer += 10-n
            now += 10-n
        else:
            answer += n
        now = now//10

    return answer