import math
MAX = 100001
def gcd(a,b):
    while b>0:
        a,b = b, a%b
    return a
n, k = map(int, input().split()) # 동생수, 수빈이의 현재 위치
sister = list(map(int,input().split())) # 동생 위치
result =[]
D = 25
for i in sister:
    result.append(abs(i - k))
d = min(result)
for i in range(n):
    d = math.gcd(result[i],d)
print(d)
