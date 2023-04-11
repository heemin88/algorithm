import heapq
def solution(plans): #name, start,playtime 
    answer = []
    newplans=[]
    # q=[]
    for name,start,playtime in plans:
        h,m = map(int,start.split(':'))
        mm = h*60 +m #분으로 바꾸기 
        newplans.append([mm,name,int(playtime)]) #시작시간, 이름, playtime
        #heapq.heappush(q,[mm,name,playtime]) #시간
    newplans.sort()
    now = newplans[0][0]+newplans[0][2] #현재 시간 
    stack = [] #멈춰둔 과제 저장 
    for i in range(1,len(newplans)+1):
        if i == len(newplans):
            answer.append(newplans[i-1][1])
            break
        m,name,playtime = newplans[i]
        if m >= now:#앞 작업이 다 끝나있으면 
            answer.append(newplans[i-1][1])
            if m >now and len(stack):#널널하게 끝났고 멈춘 과제가 있다면 
                tmp = m-now  #널널한 시간 
                while tmp <=0:
                    mm,nname = stack.pop()
                    if mm <=tmp:
                        answer.append(nname)
                        tmp -=mm 
                    else:
                        stack.append([mm-tmp,nname])
        elif m < now:
            stack.append([now - m,newplans[i-1][1]]) #끝날 때까지 남은 시간과 이름 
        now = m+playtime 
        
    while len(stack)!=0:
            m , name = stack.pop()
            answer.append(name)
        
        
    return answer