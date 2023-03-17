def solution(keymap, targets):
    answer = []
    n = len(keymap)
    dict ={}
    for i in range(n):
        temp=list(keymap[i])
        for j in range(len(temp)):
            if dict.get(temp[j],0) ==0:
                dict[temp[j]] = j+1
            else:
                dict[temp[j]] = min(dict[temp[j]], j+1)
    for i in range(len(targets)):
        input = list(targets[i])
        cnt = 0
        for j in range(len(input)):
            if dict.get(input[j],0)==0:
                cnt = -1
                break
            else:
                cnt +=dict[input[j]]
        answer.append(cnt)
    return answer