import sys
input = sys.stdin.readline
a = list(input().rstrip())
b= list(input().rstrip())
dp = [[0 for _ in range(len(b)+1)] for _ in range(len(a)+1)]
for i in range(1,len(a)+1):
    for j in range(1,len(b)+1):
        if a[i-1] == b[j-1]:
            dp[i][j] = dp[i-1][j-1]+1
        else:
            dp[i][j] = max(dp[i-1][j],dp[i][j-1])
result =""
i,j = len(a),len(b)
while i>0 and j>0:
    if dp[i][j] == dp[i][j-1]:
        j-=1
    elif dp[i][j] == dp[i-1][j]:
        i-=1
    else:
        result = b[j-1]+result
        i-=1
        j -=1
print(dp[-1][-1])
print(result)
