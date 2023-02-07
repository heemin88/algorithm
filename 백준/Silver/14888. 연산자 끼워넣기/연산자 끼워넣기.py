n = int(input())
num =list(map(int,input().split()))
s= []
opr = list(map(int,input().split())) # + , - , x , // 갯수
result =[]
def dfs(opr):
    if len(s) == n-1:
        val =num[0]
        for i in range(len(s)):
            if s[i] == 0 : val = val + num[i+1]
            elif s[i] == 1: val = val - num[i + 1]
            elif s[i] == 2 :val = val * num[i+1]
            else :
                if val <0:
                    val = -val
                    val = -(val // num[i+1])
                else: val = val // num[i+1]
        result.append(val)
        return

    for i in range(4):
        if opr[i]==0: continue
        s.append(i)
        opr[i] -=1
        dfs(opr)
        opr[i] +=1
        s.pop()

dfs(opr)
print(max(result))
print(min(result))
