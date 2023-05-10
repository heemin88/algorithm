import math
def solution(k, d): # a*k , b*k에 점을 찍는 반면 거리가 d를 넘는 위치는 찍지 않음.
    answer = 0
    count=0
    dd = d*d
    for x in range(0,d+1,k):
        answer += (math.floor((dd-x*x)**0.5))//k +1
    return answer