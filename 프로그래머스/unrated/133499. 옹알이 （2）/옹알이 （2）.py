def solution(babbling):
    answer = 0
    possible =['aya','ye','woo','ma']
    for s in babbling:
        last =""
        while s !="":
            if s[:2] in possible and last != s[:2]:
                last = s[:2]
                s = s[2:]
            elif s[:3] in possible and last != s[:3]:
                last = s[:3]
                s = s[3:]
            else:
                break
        if s =="":
            answer +=1
            
    return answer