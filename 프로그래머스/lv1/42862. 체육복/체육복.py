def solution(n, lost, reserve): #전체 학생수, 도난당한 학생들의 번호, 여벌의 체육복을 가져온 번호
    answer = n-len(lost) #체육수업을 들을 수 있는 학생의 최댓값
    lost.sort()
    res ={}
    for re in reserve:
        if re in lost:
            answer +=1
            lost.remove(re)
            continue
        res[re] = 1
    for lo in lost:
        if res.get(lo-1,0) !=0: #자신의 여벌옷을 입는 경우
            answer +=1
            res[lo-1]=0
        elif res.get(lo+1,0)!=0: #자신 번호보다 +1 여벌옷을 입는 경우
            answer +=1
            res[lo+1]=0
            
    return answer