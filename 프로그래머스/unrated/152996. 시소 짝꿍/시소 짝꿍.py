def solution(weights): #시소 짝꿍 : 탑승한 사람의 무게 == 시소 축과 좌선간의 거리의 곱
    answer = 0
    d = [2,3,4]
    dict ={}
    for w in weights:
        if dict.get(w,0) == 0:
            dict[w] = 1
        else:
            dict[w] +=1
    for w in weights:
        if w %2 ==0 : answer += dict.get(w*3//2,0)
        if w%3 == 0 : answer += dict.get(w*4//3,0)
        answer += dict.get(w*2,0)
    for w in weights:
        dict[w] -=1
        answer += dict[w]
    
    return answer