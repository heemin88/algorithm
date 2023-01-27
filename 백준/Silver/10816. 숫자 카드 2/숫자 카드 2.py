if __name__ == "__main__":
    n = int(input())
    dict = {}
    list = input().split()
    for i in list:
        if dict.get(i,0) >=1:
            dict[i] +=1
        else:
            dict[i]= 1
    m = int(input())
    list2 = input().split()
    for i in list2:
        print(dict.get(i,0),end=" ")
