# 유기농 배추
import sys
sys.setrecursionlimit(100000)
t = int(input())


def check(arr, x, y):
    if visited[x][y]: return
    visited[x][y] = True
    if y > 0 and arr[x][y - 1] == 1 and not visited[x][y - 1]:  # 위
        check(arr, x, y - 1)
    if y < n - 1 and arr[x][y + 1] == 1 and not visited[x][y + 1]:  # 아래
        check(arr, x, y + 1)
    if x > 0 and arr[x - 1][y] == 1 and not visited[x - 1][y]:  # 왼쪽
        check(arr, x - 1, y)
    if x < m - 1 and arr[x + 1][y] == 1 and not visited[x + 1][y]:  # 오른쪽
        check(arr, x + 1, y)


for i in range(t):
    temp = list(map(int, input().split()))
    m = temp[0]  # 가로
    n = temp[1]  # 세로
    k = temp[2]  # 배추가 심어져 있는 위치의 개수
    loc = [[0] * n for _ in range(m)]
    num = []
    visited = [[False] * n for _ in range(m)]
    for j in range(k):
        tt = list(map(int, input().split()))
        num.append(tt)
        loc[tt[0]][tt[1]] = 1
    cnt = 0
    for num_loc in num:
        if visited[num_loc[0]][num_loc[1]]:
            continue
        check(loc, num_loc[0], num_loc[1])  # x,y
        cnt += 1
    print(cnt)
