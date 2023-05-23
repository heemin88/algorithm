def cal(num): #약수구하기 
    cnt =[1]
    for k in range(2,num+1):
        tmp =0
        for i in range(1,int(k**0.5)+1):
            if k%i ==0:
                tmp+=1
                if (i**2)!= k:
                    tmp +=1
        cnt.append(tmp)
    return cnt
            
def solution(number, limit, power): #기사단원의 수, 정해진 공격력 제한수치, 제한수치를 초과한 기사가 사용할 무기의 공격력
    answer = 0 # 무기를 모두 만들기 위해 필요한 철의 무게
    cnt = cal(number)
    for c in cnt:
        if c >limit:
            answer += power
        else:
            answer += c
    
    return answer