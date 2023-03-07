# 그리디 알고리즘
n = int(input())
meet = []  # [start time ,end time]
for i in range(n):
    temp = list(map(int, input().split()))
    meet.append(temp)
meet.sort(key=lambda x: (x[1],x[0]))
cnt = 1  # 회의의 최대 개수
end = meet[0][1]
for i in range(1,n):
    if meet[i][0]>=end:
        cnt +=1
        end= meet[i][1]
print(cnt)