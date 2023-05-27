#N개의 랜선을 만들어야함. K개의 랜선을 가지고 있음.
# 만들 수 있는 최대 랜선의 길이를 구하자.
answer = 0
k,n = map(int,input().split()) # 이미 가지고 있는 랜선의 개수, 필요한 랜선의 개수
def find_maxLan():
    global answer
    start =1
    end = Lan[-1]
    while start <= end:
        result =0
        mid = (start+end)//2
        for lan in Lan:
            result += lan//mid
        if result >= n:
            start = mid+1
            answer = max(mid,answer)
        else:
            end = mid-1
    return answer
Lan = []
for i in range(k):
    Lan.append(int(input())) #이미 가지고 있는 랜선의 길이
Lan.sort()
print(find_maxLan())
