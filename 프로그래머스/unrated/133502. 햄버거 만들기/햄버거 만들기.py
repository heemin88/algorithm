def solution(ingredient):
    answer = 0 # 포장하는 햄버거 개수 
    # 1: 빵 , 2: 야채, 3: 고기
    # 1 - 2 - 3 - 1 순으로 포장
    stack =[]
    i=0
    for i in ingredient:
        stack.append(i)
        if len(stack)>=4 and stack[-4:] ==[1,2,3,1]:
            answer +=1
            del stack[-4:]
    return answer