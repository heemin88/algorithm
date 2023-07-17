def solution(A, B): #A팀원들이 부여받은 수, B팀원들이 부여받은 수
    answer = 0 # B팀원들이 얻을 수 있는 최대 승정
    #A팀의 점수 중에서 가장 가깝지만 큰 값을 넣자.
    A.sort()
    B.sort()
    i=0
    for a in A:
        left = a
        while True:
            if i == len(B) : break
            right= B[i]
            if left >= right:
                i+=1
            elif left<right:
                break
        if i == len(B): #a값보다 큰 값을 찾지 못했을 경우 
            break #그 이상 진행해도 못찾을 것이기 때문.
        else:
            B[i] = 0
            answer +=1
            i = i+1
    return answer