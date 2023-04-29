def solution(numbers):
    answer = [-1 for _ in range(len(numbers))]
    stack =[]
    i,index = 0,0
    while i <= len(numbers)-1:
        if len(stack)==0 or numbers[i] < numbers[stack[-1]] :
            stack.append(i)
            i+=1
            continue
        else:
            while numbers[i] > numbers[stack[-1]]:
                num = stack.pop()
                answer[num] = numbers[i]
                if len(stack)==0: break
        stack.append(i)
        i +=1
    return answer