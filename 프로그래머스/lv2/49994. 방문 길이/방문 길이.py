def solution(dirs):
    answer = 0
    loc = [0,0]
    visited=[[[False for _ in range(11)]for _ in range(11)] for _ in range(4)]
    # 0 : U , 1 : D , 2 : R , 3:L
    for dir in dirs:
        print()
        if dir== 'U': # y값 증가
            if loc[1]+1 >5: continue
            
            if not visited[0][loc[0]+5][loc[1]+5] : #이 경로로 방문한 적이 없다면 
                visited[0][loc[0]+5][loc[1]+5]= True
                if not visited[1][loc[0]+5][loc[1]+5+1]: #반대로도 온 경우가 없다면
                    answer +=1
            loc[1]+=1
        elif dir =='D': # y값 감소
            if loc[1]-1 <-5: continue
            if not visited[1][loc[0]+5][loc[1]+5] :
                visited[1][loc[0]+5][loc[1]+5] = True
                if not visited[0][loc[0]+5][loc[1]+5-1]:
                    answer +=1
            loc[1]-=1
        elif dir == 'R': # x값 증가
            if loc[0]+1 >5: continue
            if not visited[2][loc[0]+5][loc[1]+5]:
                visited[2][loc[0]+5][loc[1]+5] = True
                if not visited[3][loc[0]+5+1][loc[1]+5]:
                    answer +=1
            loc[0]+=1
        else: #x값 감소
            if loc[0]-1 <-5: continue
            if not visited[3][loc[0]+5][loc[1]+5]:
                visited[3][loc[0]+5][loc[1]+5] = True
                if not visited[2][loc[0]+5-1][loc[1]+5]:
                    answer +=1
            loc[0]-=1
    return answer