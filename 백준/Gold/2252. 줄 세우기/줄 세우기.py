from collections import deque
n,m = map(int,input().split())#학생 수 , 키 비교 횟수
compare = [[]for _ in range(1,n+1)]
cnt = [0 for _ in range(n)]
q =deque()
result =[]
for i in range(m):
    a,b = map(int,input().split())
    compare[a-1].append(b-1) #자신이 갈 수 있는 정점 저장
    cnt[b-1] +=1
for i in range(n):
    if cnt[i]==0: #나에게 오는 정점이 없을 경우
        q.append(i)
while q:
    tmp = q.popleft()
    result.append(tmp+1)
    for i in compare[tmp]:
        cnt[i] -= 1
        if cnt[i]==0:
            q.append(i)
print(*result)