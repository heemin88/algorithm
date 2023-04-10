a,b = map(int,input().split())
result =0
def find(num,cnt):
    global result
    if num == b :
        result = cnt
        return
    if num > b: return
    find(num*2,cnt+1)
    find(int(str(num)+'1'),cnt+1)

find(a,1)
if result : print(result)
else: print(-1)

