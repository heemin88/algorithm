def solution(elements):
    #원형 수열 : 일반적인 수열에서 처음과 끝이 연결된 형태의 수열
    answer = 0 # 원형 수열의 연속 부분 수열 합으로 만들 수 있는 수의 개수
    num = set()
    elen = len(elements)
    cnt = 1
    for k in range(elen):
        for i in range(elen):
            if i+cnt > elen:
                num.add(sum(elements[i:elen])+sum(elements[0:(i+cnt)%elen]))
            else: 
                num.add(sum(elements[i:i+cnt]))
        cnt +=1
    
    return len(num)