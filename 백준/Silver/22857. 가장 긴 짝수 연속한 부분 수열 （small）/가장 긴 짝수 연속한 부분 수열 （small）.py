import sys
input = sys.stdin.readline
n,s = map(int,input().split())
#수열 s에서 최대 k번 원소를 삭제한 수열에서 짝수로 이루어져 있는 연속한 부분 수열 중 가장 긴 길이를 구해보자.
num = list(map(int,input().split()))
dp = [[0 for _ in range(n)]for _ in range(2) ]
answer = 0
for i in range(n):
    if num[i] %2 ==1: #홀수면 패스
        continue
    if n-i < answer: break
    right = i+1
    cnt = s
    ans = 1
    while cnt >=0 and right <n:
        if num[right]%2 ==1: #홀수
            cnt -=1
        else: ans +=1
        right +=1
    answer = max(answer,ans)
print(answer)