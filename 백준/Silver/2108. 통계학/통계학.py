from collections import Counter
import sys
if __name__ == "__main__":
    n = int(sys.stdin.readline())
    num = []
    for i in range(n):
        num.append(int(sys.stdin.readline()))
    print(round(sum(num)/n))
    num.sort()
    print(num[n//2])

    #최빈값 구하기
    cnt = Counter(num) # 각 숫자들의 등장횟수를 카운트 해서 몇 회 등장했는지 딕셔너리로 표현
    tmp = cnt.most_common() # 빈도수가 가장 많은 것부터 (숫자,등장횟수)의 형태로 반환
    if len(tmp)>1:
        if tmp[0][1] == tmp[1][1]:
            print(tmp[1][0])
        else:
            print(tmp[0][0])
    else:
        print(tmp[0][0])

    print(num[n-1]-num[0])