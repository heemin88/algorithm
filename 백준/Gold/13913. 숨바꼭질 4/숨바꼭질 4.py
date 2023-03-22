# 숨바꼭질 3
from collections import deque

MAX = 100001


def BFS(n, k):
    q = deque([n])
    path = deque([])
    while q:
        v = q.popleft()
        if v == k:
            print(arr[k][0])
            path.append(k)
            while k != n:
                path.appendleft(arr[k][1])
                k = arr[k][1]
            print(*path)
            return
        for next_v in (v - 1, v + 1, v * 2):
            if 0 <= next_v < MAX and not arr[next_v][0]:
                arr[next_v][0] = arr[v][0] + 1
                arr[next_v][1] = v
                q.append(next_v)


n, k = map(int, input().split())
arr = [[0, 0] for _ in range(MAX)]
BFS(n,k)
