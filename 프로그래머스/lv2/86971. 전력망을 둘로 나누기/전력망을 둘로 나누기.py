
def solution(n, wires): #송전탑의 개수, 전선 정보
    # 전선들 중 하나를 끊어서 송전탑 개수가 가능한 비슷하도록 두 전력망으로 나누었을 때, 
    # 두 전력망이 가지고 있는 송전탑의 개수의 차이(절대값)을 리턴
    answer = 101
    graph = [[] for _ in range(n+1)]
    for v1,v2 in wires:
        graph[v1].append(v2)
        graph[v2].append(v1)
    visited=[False for _ in range(n+1)]
    
    def dfs(num,cnt): #연결된 송전탑 개수 세는 함수. 갯수 리턴 
        visited[num]= True
        for v in graph[num]:
            if not visited[v] and v !=-1:
                cnt = dfs(v,cnt+1)
        return cnt
    
    for num in range(1,n+1):
        for i,num2 in enumerate(graph[num]):
            if num2 < num : continue
            visited=[False for _ in range(n+1)]
            graph[num][i] = -1
            answer = min(answer,abs(dfs(num,1)- dfs(num2,1)))
            graph[num][i] =num2
        
    return answer