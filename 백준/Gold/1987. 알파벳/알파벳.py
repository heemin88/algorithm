import sys
r , c = map(int,sys.stdin.readline().split())
alpa = []
for i in range(r):
    alpa.append(list(sys.stdin.readline()))
paths=[] #지나간 알파벳 저장
paths = set(paths)
ans = 0
def DFS(i,j,cnt):
    global ans
    ans = max(ans,cnt)
    if i >0 and alpa[i-1][j] not in path: #위
        path.add(alpa[i-1][j])
        DFS(i-1,j,cnt+1)
        path.remove(alpa[i-1][j])

    if i < r-1 and alpa[i+1][j] not in path: #아래
        path.add(alpa[i+1][j])
        DFS(i+1,j,cnt+1)
        path.remove(alpa[i+1][j])

    if j >0 and alpa[i][j-1] not in path : #왼쪽
        path.add(alpa[i][j-1])
        DFS(i,j-1,cnt+1)
        path.remove(alpa[i][j-1])

    if j < c-1 and alpa[i][j+1] not in path: #오른쪽
        path.add(alpa[i][j+1])
        DFS(i,j+1,cnt+1)
        path.remove(alpa[i][j + 1])

path = {alpa[0][0]}
DFS(0,0,1)
print(ans)
