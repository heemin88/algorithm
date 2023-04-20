def solution(order):
    #보조 컨테이너 - stack 
    # 1 2 3 4 5 -cur_order
    # 5 4 3 2 1 - order[i]
    answer = 0
    sub =[]
    cur_order =1
    i=0
    while True:
        if len(order)+1 == cur_order or i == len(order) : break
        #print(cur_order,order[i])
        if cur_order == order[i]:
            answer +=1
            i+=1
        else:
            sub.append(cur_order)
        while len(sub)!=0 and sub[len(sub)-1] == order[i] :
                answer +=1
                i+=1
                sub.pop()
        cur_order+=1
        
    return answer