from itertools import combinations
def solution(orders, course): #각 손님이 주문한 단품메뉴, 추가하고 싶은 코스요리를 구성하는 단품메뉴들의 깃수
    #메뉴는 최소 2가지 이상의 단품메뉴
    #최소 2명 이상의 손님으로부터 주문된 단품메뉴 조합
    answer = []
    pos_dict ={}
    for c in course:
        for order in orders:
            if len(order)<c: 
                continue
            tmp = list(combinations(order,c))
            for t in tmp:
                list_tmp = list(t)
                list_tmp.sort()
                string =''
                for s in list_tmp:
                    string+=s
                if pos_dict.get(string,0)!=0:
                    pos_dict[string] +=1
                else: 
                    pos_dict[string] = 1
    max_cnt = 0
    now_len = 0
    for st,cnt in sorted(pos_dict.items(),key = lambda x : (x[1]),reverse=True):
        if cnt <2: break
        if now_len < len(st):
            now_len = len(st)
            max_cnt = 0
        if max_cnt <=cnt:
            max_cnt = cnt
            answer.append(st)
    answer.sort()
    return answer