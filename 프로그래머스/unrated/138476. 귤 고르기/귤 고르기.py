def solution(k, tangerine):
    answer = 0
    dic ={}
    for i in tangerine:
        if dic.get(i,0)==0:
            dic[i] = 1
        else:
            dic[i]+= 1
    sorted_t = sorted(dic.items(),key = lambda x : -x[1])
    for num , cnt in sorted_t : #크기, 갯수 
        if cnt >= k:
            answer +=1
            break
        else:
            answer +=1
            k -= cnt
        
    return answer