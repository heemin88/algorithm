n,m = map(int, input().split()) #사람수 , 파티 수
temp = list(map(int,input().split()))
known = temp[0] #진실을 아는 사람의 수
temp.remove(temp[0])
known_num = set(temp) #진실을 아는 사람의 번호
result =0
party_num = [] #파티에 참가한 사람들 번호
for i in range(m):
    temp = list(map(int,input().split()))
    temp.remove(temp[0])
    bool = True
    for num in temp:
        if num in known_num: #파티에 참가한 사람 중에 진실을 아는 사람이 있는 경우
            bool = False
            break
    if not bool:
        for num in temp:
            known_num.add(num)
    party_num.append(temp)

if known==0 : print(m)
else:
    i =0
    num_result=[]
    nn = 0
    while nn <= m*m:
        if i == m : i=0
        bool = True
        for num in party_num[i]:
            if num in known_num :
                bool = False
                break
        if bool :
            if i not in num_result:
                result +=1
                num_result.append(i)
        else:
            for num in party_num[i]:
                known_num.add(num)
            if i in num_result:
                num_result.remove(i)
                result -=1
        i+=1
        nn+=1
    print(result)