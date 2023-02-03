arr= input().split()
n= int(arr[0])
m = int(arr[1])
s =[]
def dfs():
    if len(s)==m:
        print(' '.join(map(str,s)))
        return
    for i in range(1,n+1):
        if len(s)>=1 and i < s[len(s)-1]:# 오름차순 (바로 앞 숫자랑 비교)
            continue
        s.append(i)
        dfs()
        s.pop()

dfs()
