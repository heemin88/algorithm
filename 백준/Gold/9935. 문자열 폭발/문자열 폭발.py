arr =input()
boom = input()
stack =[]
for c in arr:
    stack.append(c)
    if len(stack) >= len(boom)and stack[-1]==c and ''.join(stack[-len(boom):]) == boom:
        for i in range(len(boom)):
            stack.pop()
if len(stack) ==0: print("FRULA")
else:print(*stack,sep="")
