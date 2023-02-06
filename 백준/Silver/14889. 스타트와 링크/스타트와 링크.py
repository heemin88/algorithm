n = int(input())
arr=[] # 입력 값 저장
s = [0] # 팀
result = []
def dfs():
    if len(s)==n/2:
        start =0
        link =0
        for i in range(n):
            for j in range(i+1,n):
                if i in s and j in s :
                    start += arr[i][j]+arr[j][i]
                elif i in s or j in s :
                    continue
                else:
                    link += arr[i][j]+arr[j][i]
        result.append(abs(start-link))
        return
    for i in range(1,n):
        if i not in s and s[len(s)-1]<i:
            s.append(i)
            dfs()
            s.pop()



for i in range(n):
    temp = input().split()
    for j in range(n):
        temp[j] = int(temp[j])
    arr.append(temp)
dfs()
print(min(result))