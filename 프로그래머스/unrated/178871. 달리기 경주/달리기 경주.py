def solution(players, callings):
    answer = {}
    answer2 ={}
    for i in range(len(players)):
        answer[players[i]] = i
        answer2[i] = players[i]
    for player in callings:
        answer[player] -=1
        tmp = answer2.get(answer[player])
        answer[tmp]+=1
        answer2[answer[player]] = player
        answer2[answer[tmp]]=tmp
    for key,val in answer.items():
        players[val] = key
    return players