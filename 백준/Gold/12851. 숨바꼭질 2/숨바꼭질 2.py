# 숨바꼭질 2
from collections import deque

MAX = 100001


def BFS(n):
    q = deque([n])
    num = [0 for _ in range(MAX)]
    result = 0
    if n == k: print(0);print(1); return
    while q:
        v = q.popleft()
        if v == k:
            print(result, num[result], sep="\n")
            return
        for next_v in (v - 1, v + 1, v * 2):
            if 0 <= next_v < MAX:
                if 0 < arr[next_v] < arr[v] + 1:
                    continue
                arr[next_v] = arr[v] + 1
                if next_v == k:
                    if result == 0:
                        result = arr[next_v]
                    num[arr[next_v]] += 1
                q.append(next_v)
    print(result, num[result], sep="\n")


n, k = map(int, input().split())
arr = [0 for _ in range(MAX)]
BFS(n)
