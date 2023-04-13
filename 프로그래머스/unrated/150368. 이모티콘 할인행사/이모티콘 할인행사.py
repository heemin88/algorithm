        
rate =[10,20,30,40]
answer =[-1,-1]
def solution(users, emoticons): # n개의 사용자 구매기준,  이모티콘 m개의 정가
    n,m = len(users),len(emoticons)
    discount_list = [0]*m
    def search(idx):
        global answer
        if idx == m: 
            regis,cost =0,0
            for i in range(n):
                tmp =0
                for j in range(m):
                    if users[i][0] <= discount_list[j]:
                        tmp += emoticons[j] *(100-discount_list[j])//100
                if tmp >= users[i][1]:
                    regis +=1
                else:
                    cost +=tmp
            if answer[0]<regis or answer[0]==regis and answer[1]<cost:
                answer = [regis,cost]
            return
                    
        for i in range(4):
            discount_list[idx] = rate[i]
            search(idx+1)
                    
    search(0)
    return answer