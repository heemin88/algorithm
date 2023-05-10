def solution(topping):#input : 롤 케이크에 올라가 있는 토핑들의 번호
    #동일한 가짓수의 토핑이 올라가면 공평하게 케이크가 나눠진 것.(조각크기, 토핑개수 상관 X)
    answer = 0#롤케이크를 공평하게 자르는 방법의 수
    a_dp= [1] #처음부터 가짓수를 세는 메모리제이션
    b_dp=[1] # 끝에서부터 가짓수를 세는 메모리제이션
    a= {} # 가짓수가 이전에 나왔는지 확인을 위한 배열
    b= {}

    a[topping[0]]=1
    b[topping[-1]]=1
    
    for i in range(1,len(topping)): #처음부터 돌면서 가짓수를 dp에 저장
        num = topping[i]
        if a.get(num,0)==0:#앞에서 나오지 못한 토핑 종류라면 , 0이라면
            a[num] = 1 #나왔음을 표시
            a_dp.append(a_dp[-1]+1)
        else:#나온적이 있다면 
            a_dp.append(a_dp[-1])#이전 값 저장
            
    for i in range(len(topping)-2,-1,-1):#끝에서부터 오면서 토핑 가짓수 
        if b.get(topping[i],0)==0:#앞에서 나오지 못한 토핑 종류라면
            b[topping[i]] = 1 #나왔음을 표시
            b_dp.append(b_dp[-1]+1)
        else:
            b_dp.append(b_dp[-1])
    b_dp.reverse()
    
    for i in range(len(topping)-1):
        if a_dp[i]==b_dp[i+1]:
            answer +=1
    return answer