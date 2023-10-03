import sys
input = sys.stdin.readline
# n명의 원생들을 키 순서대로 줄 세우고, k개의 조로 나눔.
# 가장 키가 큰 원생과 가장 키가 작은 원생 키 차이만큼 비용이 듬
n,k = map(int,input().split())
people = list(map(int,input().split())) #정렬이 되어있음
array =[]
for i in range(1,n):
    array.append(people[i]-people[i-1])
array.sort(reverse = True)
print(sum(array[k-1:]))