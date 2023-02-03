arr= input().split()
n= int(arr[0])
m = int(arr[1])
s =[]
def dfs():
    if len(s)==m:
        print(' '.join(map(str,s)))
        return
    for i in range(1,n+1):
        s.append(i)
        dfs()
        s.pop()

dfs()