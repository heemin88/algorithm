from itertools import product
def solution(n, info): #화살의 개수 , 어피치가 맞힌 과녁 점수의 개수 
    #한 과녁에 많이 맞힌 사람이 점수를 가져감. 같은경우 어피치가 가져감
    # 최종 점수가 더 높은 선수가 우승자, 점수가 같은 경우 어피치가 우승자
    #현재는 어피치가 화살 n발을 다 쏜 후이고 라인언이 쏠 차례.
    answer = [-1] # 라이언이 큰 점수 차이로 이기기 위해, n발의 하살을 어떤 과녁 점수에 맞혀야하는지 .
    # 방법이 여러가지인 경우, 가장 낮은 점수를 더 많이 맞힌 경우를 리턴
    cases = list(product([True,False],repeat = 11))
    answer_cnt =0
    info.reverse()
    for case in cases :
        count = 0 # 현재까지 쓴 화살 수를 나타냄.
        r_score = 0 #라이언의 과녁점수
        a_score = 0 #어피치의 과녁점수
        for i in range(11): # 라이언이 쏜 화살 수와 score를 갱신해줌. 
            if case[i]:
                count += info[i]+1
                r_score += i
            if not case[i] and info[i]:
                a_score += i
        if count <=n:
            d = r_score-a_score
            if d > answer_cnt:
                answer_cnt = d
                answer=[info[i]+1 if case[i] else 0 for i in range(11)]
                answer[0] += n-count
    answer.reverse()
    return answer