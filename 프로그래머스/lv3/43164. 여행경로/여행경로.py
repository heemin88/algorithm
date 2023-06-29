from collections import deque
from copy import deepcopy
def solution(tickets): #항공권 정보 
    answer = ["ICN"] #방문하는 공항 경로를 담아
    #주어진 항공권은 모두 사용해야 함.
    # 가능한 경로가 2개 이상일 경우 알파벳 순서가 앞서는 경로 리턴 
    tickets.sort(key = lambda x : x[1])
    path={}
    for a,b in tickets:
        if path.get(a,0)==0: 
            path[a] = [b]
        else:
            path[a].append(b)
    q = deque([])
    q.append(["ICN",["ICN"],path])
    while q:
        dep,paths,path= q.popleft()
        if len(paths)== len(tickets)+1:
            answer = paths
            break
        if path.get(dep,0) == 0 : continue
        for i in range(len(path[dep])):
            tmp = deepcopy(paths)
            tmp2 = deepcopy(path)
            tmp.append(path[dep][i])
            del tmp2[dep][i]
            q.append([path[dep][i],tmp,tmp2])
    return answer
