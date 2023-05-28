from collections import Counter
def solution(X, Y):
    answer = ''
    X = dict(Counter(list(X)))
    Y = dict(Counter(list(Y)))
    tmp =[]
    cnt_0 = 0
    for key in X:
        if Y.get(key,-1)!=-1:
            
            for i in range(min(X[key],Y[key])):
                if key =='0':
                    cnt_0 +=1
                tmp.append(key) 
    tmp.sort(reverse=True)
    if len(tmp)==0 : return '-1'
    elif len(tmp) == cnt_0 : return '0'
    else:
        for i in tmp:
            answer += i
    return answer