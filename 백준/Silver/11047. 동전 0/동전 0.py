arr = input().split()
n = int(arr[0])
k = int(arr[1])
num = []
cnt = 0
for i in range(n):
    temp = int(input())
    if temp > k:
        break
    num.append(temp)
idx = len(num) - 1
while k > 0:
    if k < num[idx]:
        idx -= 1
        continue
    cnt += k // num[idx]
    k = k % num[idx]
    idx -= 1
print(cnt)