import sys
if __name__ == "__main__":
    n = int(sys.stdin.readline())
    list = []
    for i in range(n):
        list.append(int(sys.stdin.readline()))
    list.sort()
    for i in list :
        print(i)
