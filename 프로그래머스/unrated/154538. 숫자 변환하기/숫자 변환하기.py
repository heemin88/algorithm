from collections import deque
def solution(x, y, n):
    
    answer = 0
    dp =[1000001 for _ in range(y+1)]
    dp[x]= 0 
    for i in range(x,y):
        if i+n <=y:
            dp[i+n] = min(dp[i]+1,dp[i+n])
        if i*2 <=y:
            dp[i*2] = min(dp[i]+1,dp[i*2])
        if i*3 <=y:
            dp[i*3]= min(dp[i]+1,dp[i*3])
    
    # q = deque([])
    # q.append([x,0])
#     while q:
#         t,cnt = q.popleft()
#         if t == y : 
#             answer = cnt
#             break 
#         if t*3 <=y:
#             q.append([t*3,cnt+1])
#         if t*2 <= y:
#             q.append([t*2,cnt+1])
#         if t+n <=y : 
#             q.append([t+n,cnt+1])
        
    if dp[y] == 1000001:
        return -1
    return dp[y]