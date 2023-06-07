def check(s) : #올바른 괄호인지 확인
    stack =[]
    for i in s:
        if i == '[' or i=='(' or i=='{':
            stack.append(i)
        else:
            if len(stack)==0: return False
            prev = stack.pop()
            if (i ==']' and prev!='[') or (i==')' and prev != '(') or (i=='}' and prev != '{'):
                return False
    if len(stack)!=0 : return False
    return True
                
                
def solution(s):
    answer = 0
    length=len(s)
    for i in range(length):
        string = s[i:]+s[:i]
        if check(string):
            answer +=1
    
    return answer