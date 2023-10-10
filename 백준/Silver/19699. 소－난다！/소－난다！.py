import sys
from itertools import combinations

def is_prime(a):
    if a <= 1: return False
    for i in range(2, int(a ** (0.5)) + 1):
        if a % i == 0:
            return False
    return True

input = sys.stdin.readline
# 소들의 몸무게의 합이 소수가 되도록 m마리의 소를 선별할 것.
# 계획에 맞게 소를 선별했을 때 나올 수 있는 몸무게의 합을 모두 출력
n, m = map(int, input().split())  # 소들의 수, 선별할 소의 수
weight = list(map(int, input().split()))

answer = set([])
for combi in list(combinations(weight, m)):
    if is_prime(sum(combi)):
        answer.add(sum(combi))
if len(answer) == 0:
    print(-1)
else:
    print(*sorted(list(answer)))
