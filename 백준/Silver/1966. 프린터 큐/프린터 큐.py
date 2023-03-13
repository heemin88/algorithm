# 큐
k = int(input()) #test case
result =[]
for i in range(k):
    temp = list(map(int,input().split()))
    n = temp[0] #문서의 개수
    m = temp[1] # 현재 큐에서 몇번째에 놓여있는지
    imp = list(map(int, input().split()))
    printer =[]
    index =0
    for num in imp:
        printer.append((num,index))
        index += 1
    cnt =0
    value = imp[m]
    while True:
        check = printer.pop(0)
        #if check[0] >= max(imp):
        if all(check[0]>=x[0] for x in printer):
          cnt +=1
        else:
            printer.append(check)
        if (value,m) not in printer:
            result.append(cnt)
            break
for i in result:
    print(i)
