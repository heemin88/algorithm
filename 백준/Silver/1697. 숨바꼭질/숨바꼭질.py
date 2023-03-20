from collections import deque
MAX = 100001
def BFS(n):
    q = deque([n])
    while q:
        v = q.popleft()
        if v == k: return arr[v]
        for next_v in (v-1,v+1,v*2):
            if 0<= next_v <MAX and not arr[next_v]:
                arr[next_v] = arr[v]+1
                q.append(next_v)
n,k= map(int,input().split())
arr = [0 for _ in range(MAX)]
print(BFS(n))
