import sys
input = sys.stdin.readline
n,k = map(int,input().split())
answer = 0 #현재 지나고 있는 코스의 번호를 출력 , 지나야할 코스
course = list(map(int,input().split()))
s = sum(course)
if k >= s:
    ssum =s
    for i in range(len(course)-1,-1,-1):
        ssum += course[i]
        if ssum > k:
            answer = i+1
            break
else:
    ssum =0
    for i in range(len(course)):
        ssum += course[i]
        if ssum >k:
            answer = i+1
            break
print(answer)