import math
def solution(arrayA, arrayB):
    answer = 0
    # 각 배열별 최대 공약수를 구해서 그 수의 약수들이 들어간 배열을 만든다.
    # 큰 값부터 상대의 배열을 돌면서 나누어 떨어지는지 확인한다. 
    a = arrayA[0]
    b = arrayB[0]
    for i in range(1,len(arrayA)):
        a = math.gcd(a,arrayA[i])
        b = math.gcd(b,arrayB[i])
    aa = []
    bb = []
    for i in range(2,a+1):
        if a%i ==0:  
            aa.append(i)
    for i in range(2,b+1):
        if b%i ==0:  
            bb.append(i)
    for i in range(len(bb)-1,-1,-1): #b의 약수들로 a값들을 하나씩 나누어봄.
        bool_find = True
        for j in arrayA:
            if j%bb[i]==0:
                bool_find = False
                break
        if bool_find : # 다 안나눠지는 값을 찾았다면 
            answer = max(answer,bb[i])
            break 
            
    for i in range(len(aa)-1,-1,-1): #a의 약수들로 b값들을 하나씩 나누어봄.
        bool_find = True
        for j in arrayB:
            if j%aa[i]==0:
                bool_find = False
                break
        if bool_find : # 다 안나눠지는 값을 찾았다면 
            answer = max(answer,aa[i])
            break 
    return answer