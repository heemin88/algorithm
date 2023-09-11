import bisect
l = int(input())
s = list(map(int,input().split()))
n = int(input())
answer =0 #n을 포함하는 좋은 구간의 개수
s.sort()
idx = bisect.bisect_left(s,n)
if n in s :
    print(0)
    exit()
if idx != 0:
    for k in range(s[idx-1]+1,n+1): # A
        for i in range(n, s[idx]):  # B
            if k>= i: continue
            answer += 1
else:
    for k in range(1,n+1):
        for i in range(n,s[idx]):
            if k >= i: continue
            answer +=1
print(answer)

