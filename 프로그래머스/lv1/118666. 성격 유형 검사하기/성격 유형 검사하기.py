def solution(survey, choices): #질문마다 판단하는 지표, 각 질문마다 선택한 선택지
    answer = ''
    type= {'R':0,'T':0,'C':0,'F':0,'J':0,'M':0,'A':0,'N':0}
    for i,sur in enumerate(survey):
        if choices[i]<=3:
            type[sur[0]] += 4-choices[i]
        elif choices[i]>=5:
            type[sur[1]]+= choices[i]-4
    i =0
    now = 0
    t = ''
    for key,val in type.items():
        if i%2 ==0:
            now = val
            t = key
            i+=1
            continue
        if now <val:
            answer+=key
        else:
            answer+=t
        t= ''
        now = 0
        i+=1
        
    return answer