
def s(num):
    k= num[1]-num[0]
    for i in range(2,len(num)):
        if k != num[i]-num[i-1]: return False
    return True


if __name__ == "__main__":
    n = int(input())
    result =0
    for i in range(1,n+1):
        num = list(map(int,str(i)))
        if len(num)<3:
            result +=1
        elif s(num) is True :
            result +=1
    print(result)
