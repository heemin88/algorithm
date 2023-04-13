def solution(name, yearning, photo): # 사람 이름 / 사람별 그리움 점수 / 찍힌 인물이름
    answer = []
    dict = {}
    for i ,n in enumerate(name):
        dict[n]= yearning[i] 
    for i in range(len(photo)):
        ans = 0
        for j in range(len(photo[i])):
            if dict.get(photo[i][j],0)!=0:
                ans += dict[photo[i][j]]
        answer.append(ans)
    return answer