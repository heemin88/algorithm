def solution(answers):
    answer = [] #가장 문제를 많이 맞힌 사람 
    a= [1,2,3,4,5]
    b= [2,1,2,3,2,4,2,5]
    c = [3,3,1,1,2,2,4,4,5,5]
    score=[0,0,0]
    for i in range(len(answers)):
        if a[i%5] == answers[i]: score[0] +=1
        if b[i%8] == answers[i] : score[1]+=1
        if c[i%10] == answers[i] : score[2] +=1
    tmp = max(score)
    for i,s in enumerate(score):
        if s==tmp : answer.append(i+1)
    return answer