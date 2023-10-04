import sys
input = sys.stdin.readline
n,s = map(int,input().split())
#수열 s에서 최대 k번 원소를 삭제한 수열에서 짝수로 이루어져 있는 연속한 부분 수열 중 가장 긴 길이를 구해보자.
num = list(map(int,input().split()))
answer = 0
left,right = 0,0
tmp = 0 # 지금까지 삭제한 갯수
cnt = 0 #지금까지 짝수 갯수
while right < n:
    if num[right] %2 ==1: #right가 홀수면
        tmp +=1
        answer = max(answer, cnt)
    else: #right가 짝수면
        cnt +=1
        answer = max(answer, cnt)
    right += 1
    if tmp >s : #삭제할 수 있는 기회를 다 썼다면
        if num[left]%2 ==1: tmp -=1
        else : cnt -=1
        left +=1
print(answer)