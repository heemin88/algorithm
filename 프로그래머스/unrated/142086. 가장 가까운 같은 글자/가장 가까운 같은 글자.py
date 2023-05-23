def solution(s):
    answer = [-1]*len(s)
    s_dic = {}
    for i in range(len(s)):
        if s_dic.get(s[i],-1)!= -1:
            answer[i] = i - s_dic[s[i]]
        s_dic[s[i]] = i
    
    return answer