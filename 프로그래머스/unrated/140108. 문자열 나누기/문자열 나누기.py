def solution(s):
    answer = 0 #분해한 문자열의 개수 
    while True:
        if len(s)==0: break
        standard = s[0]
        same =1
        not_same = 0
        for i in range(1,len(s)):
            if same == not_same : break
            if s[i] == standard:
                same +=1
            else:
                not_same +=1
            
        answer +=1
        s = s[same*2:len(s)]
        
    return answer