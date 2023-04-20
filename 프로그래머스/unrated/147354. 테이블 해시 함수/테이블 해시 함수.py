def solution(data, col, row_begin, row_end):
    #열 : 컬럼 , 행 : 튜플 
    answer = 0
    data= sorted(data,key = lambda x: [x[col-1],-x[0]] )
    for i in range(row_begin,row_end+1):
        tmp =0
        for num in data[i-1]:
            tmp += num % i 
        answer = answer ^ tmp
    return answer