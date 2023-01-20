if __name__ == "__main__":
    n = list(input())
    n.sort()
    for i in range(len(n)-1,-1,-1):
        print(n[i],end='')


