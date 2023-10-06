import sys
input = sys.stdin.readline
n,q = map(int,input().split()) #땅 개수, 오리 수
num =[]
for _ in range(q):
    num.append(int(input()))
visited=[False for _ in range(max(num)+1)]
for i in range(len(num)):
    tmp = num[i]
    check = 0 #가장 작은 점유 된 땅 번호를 구하기 위함. 
    while tmp >=1 : #root까지 탐색 
        if visited[tmp] : check = tmp #점유된 땅이면 번호 저장
        tmp = tmp//2
    if check==0 : print(0)
    else: print(check)
    visited[num[i]] = True  # 방문 check
