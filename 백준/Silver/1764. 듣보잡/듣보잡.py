if __name__ == "__main__":
    temp = input().split()
    n = int(temp[0])
    m = int(temp[1])
    dict = {}
    num =0
    result =[]
    for i in range(n):
        name = input()
        dict[name]=1
    for i in range(m):
        name = input()
        if name in dict :
            num+=1
            result.append(name)
    print(num)
    result.sort()
    for i in result:
        print(i)
