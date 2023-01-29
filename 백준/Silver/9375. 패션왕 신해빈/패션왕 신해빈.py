if __name__ == "__main__":
    n = int(input()) #테스트 케이스
    results=[]
    for i in range(n):
        t = int(input())
        clothes = {}
        for j in range(t):
            temp = input().split()
            if clothes.get(temp[1],0)==0:
                clothes[temp[1]] =1
            else:
                clothes[temp[1]] += 1
        result = 1
        for key,val in clothes.items():
            result *= val+1
        results.append(result-1)
    for i in results:
        print(i)