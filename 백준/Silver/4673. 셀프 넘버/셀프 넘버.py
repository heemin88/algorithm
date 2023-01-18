def self_number(n):
    a = list(map(int,str(n)))
    num = n
    for i in range(len(a)):
        num += a[i]
    return num

if __name__ == "__main__":
    check = [False for i in range(10001)]
    for i in range(10001):
        n = self_number(i)
        if n<10001:
            check[n] = True
    for i in range(len(check)):
        if check[i] is False:
            print(i)
