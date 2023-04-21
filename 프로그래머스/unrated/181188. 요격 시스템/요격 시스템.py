def solution(targets):
    answer = 0
    #targets= sorted(targets, key = lambda x : x[1])
    targets.sort()
    result =[]
    for s,e in targets:
        if len(result)==0 :
            result.append([s,e])
        else:
            ps,pe =result[len(result)-1]
            if ps<= s <pe:
                continue
            else:
                result.append([s,e])
    return len(result)