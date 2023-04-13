def dfs(idx, sheep, wolf, possible): #현재정점, 양의수,늑대수, 이동 가능한 정점
    global g_info, answer, graph
    #print(idx, sheep, wolf, possible)
    if g_info[idx] == 0: #양이면 
        sheep += 1
        answer = max(answer, sheep)
    else: # 늑대면 
        wolf += 1
        
    if wolf >= sheep: #늑대수가 더 크면 
        return 
    
    possible.extend(graph[idx])#자식노드들 추가 
    for p in possible: #갈 수 있는 정점 다 이동해보기
        dfs(p, sheep, wolf, [i for i in possible if i != p])
    
def solution(info, edges):
    global answer, g_info, visited, graph
    answer = 0
    g_info = info
    n = len(info)
    graph = [[] for _ in range(n)]
    
    for a, b in edges:
        graph[a].append(b)
        
    
    dfs(0, 0, 0, [])
    return answer