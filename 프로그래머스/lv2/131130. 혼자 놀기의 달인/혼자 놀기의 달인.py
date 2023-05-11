def solution(cards):
    #열어야하는 상자가 이미 열려있다면 첫번째 게임 종료. 또 다시 임의로 한 박스를 선정
    answer = 0# 이 게임에서 얻을 수 있는 최고 점수 구하기
    open = [False for _ in range(len(cards)+1)]
    group =[]
    for i in range(len(cards)):
        if open[i] == True: continue
        n=i
        group_cnt = 0
        while True:
            n = cards[n]-1
            if open[n] : break #상자그룹 만들어짐.
            group_cnt +=1
            open[n]= True
        group.append(group_cnt)
    group.sort()
    if len(group)<2:return 0
    answer = group[-1]*group[-2]
    return answer