def solution(weights): #시소 짝꿍 : 탑승한 사람의 무게 == 시소 축과 좌선간의 거리의 곱
    answer = 0
    dict={}
    for i in weights:
        if dict.get(i,0)==0:
            dict[i]=1
        else : dict[i]+=1
    for i in weights:
        if i%2 ==0:
            answer += dict.get(i*3//2,0)
        if i%3 ==0:
            answer += dict.get(i*4//3,0)
        answer += dict.get(i*2,0)
    for i in weights:
        dict[i]-=1
        answer += dict[i]
    
    return answer