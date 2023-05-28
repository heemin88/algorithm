from itertools import combinations
def solution(number):
    answer = 0 #삼총사를 만들 수 있는 방법의 수
    a = list(combinations(number,3))
    for i in range(len(a)):
        if sum(a[i])==0:
            answer +=1
    return answer