def solution(park, routes):
    parks=[[]for _ in range(len(park))]
    h = len(park)
    w=0
    start_x=0
    start_y=0
    dx=[0,0,-1,1] # w e n s
    dy=[-1,1,0,0]
    def move(x,y,idx):
        xx = x+dx[idx]
        yy = y+dy[idx]
        if 0<=xx<h and 0<=yy<w and parks[xx][yy]!='X':
            return xx,yy
        else:
            return -1,-1
    
    for i in range(len(park)):
        tmp = list(park[i])
        for k,j in enumerate(tmp):
            if j == 'S':
                start_x=i
                start_y=k
        parks[i]=tmp
    w = len(parks[i])
    for r in routes:
        s,num =r.split()
        result =[start_x,start_y]
        for i in range(int(num)):
            if s == 'W': tmp,tmp2 = move(start_x,start_y,0)
            elif s == 'E': tmp,tmp2 = move(start_x,start_y,1)
            elif s == 'N':tmp,tmp2 =  move(start_x,start_y,2)
            elif s == 'S':tmp,tmp2 =  move(start_x,start_y,3)
            if tmp == -1: 
                start_x,start_y = result[0],result[1]
                break
            start_x,start_y = tmp,tmp2
    return start_x,start_y
    