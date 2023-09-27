# 소시지 수와 평론가의 수가 주어졌을 때, 모든 평론가에게 같은 양의 소시지를 주기 위해 필요한 칼질의 수
import sys
input = sys.stdin.readline
n,m = map(int,input().split()) #소시지의 수, 평론가의 수
def gcp(a,b):
    while b != 0:
        t = a%b
        a,b = b,t
    return abs(a)
print(m-gcp(n,m))