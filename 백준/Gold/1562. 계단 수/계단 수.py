n = int(input())
bit_range= 1<<10 # 2^10
num_range = 10
mod = 1000000000
dp = [[[0] * bit_range for _ in range(num_range)]for _ in range(n+1)] # dp[자리수][마지막숫자][사용된 숫자들의 비트값] = 갯수
for i in range(1,num_range): # 0 제외
    dp[1][i][1<<i] = 1

for i in range(1,n): # 자리수
    for j in range(num_range): # 숫자 범위
        for k in range(bit_range): # 숫자 비트 표현
            if j >0 : # 맨 뒤에 있는 숫자가 0보다 크면 해당 숫자보다 1작은 숫자들이 올 수 있음
                next = k | 1 << (j-1) #자신보다 1작은 값
                dp[i+1][j-1][next] += dp[i][j][k]
                dp[i+1][j-1][next] %= mod
            if j <9: # 맨 뒤에 있는 숫자가 9보다 작으면 해당 숫자보다 1 큰 숫자들이 올 수 있음
                next = k | 1 << (j+1) # 자신보다 1 큰값
                dp[i+1][j+1][next] += dp[i][j][k]
                dp[i+1][j+1][next] %=mod
res =0
for i in range(num_range):
    res += dp[n][i][bit_range-1]
    res %= mod
print(res)
