maxx =0
a=0
b=0
for i in range(9):
    temp =list(map(int,input().split()))
    if max(temp)> maxx :
        maxx = max(temp)
        a=i
        b=temp.index(maxx)

print(maxx)
print(a+1,b+1)