def solution(s): #튜플을 표현하는 집합 
    answer = [] #s가 표현하는 튜플 
    stack =[]
    string =[]
    for i in s:
        
        if i =='}':
            tmp=[]
            num = ''
            while True:
                temp = stack.pop()
                if temp=='{': break
                elif temp ==',':
                    tmp.append(int(num[::-1]))
                    num =''
                    continue
                else: num += temp
            if len(num) != 0 :tmp.append(int(num[::-1]))
            tmp.reverse()
            if len(tmp) !=0:string.append(tmp)
        else:
            if i==',' and stack[-1]=='{':continue
            stack.append(i)
    
    string.sort(key = lambda x : len(x))
    for s in string:
        for ss in s:
            if ss not in answer :
                answer.append(ss)
    return answer