def fac(n):
    if n<=1:
        return 1
    return n*fac(n-1)

if __name__ == "__main__":
    n = int(input())
    print(fac(n))
