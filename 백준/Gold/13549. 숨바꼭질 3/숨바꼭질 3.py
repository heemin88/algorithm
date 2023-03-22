# 숨바꼭질 3
from collections import deque

MAX = 100001


def BFS(n):
    q = deque([n])
    visited = [0 for _ in range(MAX)]
    while q:
        v = q.popleft()
        if v == k:
            print(arr[k])
            return
        for next_v in (v - 1, v + 1,v*2):
            if 0 <= next_v < MAX and not visited[next_v]:
                if next_v != v * 2 :
                    if arr[next_v] !=0 and arr[next_v] <= arr[v]+1: continue
                    arr[next_v] = arr[v] + 1
                    q.append(next_v)
                else : # v*2라면
                    if arr[next_v] !=0 and arr[next_v] <= arr[v] : continue
                    arr[next_v] = arr[v]
                    q.append(next_v)
                    visited[next_v] = 1



n, k = map(int, input().split())
arr = [0 for _ in range(MAX)]
BFS(n)
