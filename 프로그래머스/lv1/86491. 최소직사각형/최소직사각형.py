import copy
def solution(sizes):
    answer = float('inf') # 모든 명함을 수납할 수 있는 가장 작은 지갑 
    w =[]
    h =[]
    for size in sizes:
        w.append(max(size))
        h.append(min(size))
    return max(w)*max(h)