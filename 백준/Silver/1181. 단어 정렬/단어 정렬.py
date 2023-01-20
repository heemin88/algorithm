if __name__ == "__main__":
    n = int(input())
    words = []
    for i in range(n):
        words.append(input())
    words = list(set(words)) #중복제거
    words.sort(key=lambda x : (len(x),x))
    for i in words:
        print(i)