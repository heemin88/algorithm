def pibo(n,a,b,k):
    if n==k:
        print(a)
        return
    pibo(n,b,a+b,k+1)

if __name__ == "__main__":
    n = int(input())
    pibo(n,0,1,0)
