def solution(n, m, section): # 벽 갯수 , 롤러 길이 , 다시 칠해야할 구역 
    answer = 1
    j=0
    wall =[0 for _ in range(n)] # 1이 다시 칠해야할 구역인 것 
    num =0
    tmp =section[0]
    for i in range(1,len(section)):
        #wall[i-1] = 1
        if section[i]-tmp<m: 
            continue
        else: 
            answer +=1
            tmp = section[i]
#     for i in range(len(wall)):
#         wall[]
#         if num == n : break#다 칠했으면 리턴 
#         if i+m <=n:
#             if wall[i] ==1 :
#                 answer+=1
#                 num+=1
#                 for j in range(i,i+m):
#                     wall[j]=0
    
#         #print(wall)
    return answer