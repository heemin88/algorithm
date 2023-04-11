string = input()
while string != '.':
    string = list(string)
    balance = []
    sccess = True
    for c in string:
        if c == '[' or c =='(':
            balance.append(c)
        elif c ==']' or c==')': # balance에 서 pop해서 c랑 같은지 비교
            if len(balance) ==0: # 스택이 비어있으면
                sccess = False
                break
            tmp = balance.pop()
            if tmp =='[' and c ==']':
                continue
            elif tmp =='(' and c==')':
                continue
            else:
                sccess = False
                break
    string = input()
    if len(balance) != 0 or not sccess:
        print('no')
    else:print('yes')




