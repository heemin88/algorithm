arr = input().split()
x = int(arr[0]) # 게임 횟수
y= int(arr[1]) # 이긴 게임
z = (y*100) // x
left =1
right = x
if z >=99 : print(-1)
else:
    while left <= right:
        mid = (left+right)//2
        if ((mid+y)*100)//(x+mid) > z:
            right = mid - 1
        else:
            left = mid + 1
    print(left)
