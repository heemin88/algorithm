if __name__ == "__main__":
    n = int(input())
    result =0
    for i in range(n):
        word = list(input())
        string = []
        boo = True
        for j in range(len(word)):
            if word[j] in string and word[j-1]!=word[j]:
                boo = False
                break
            string.append(word[j])
        if boo :
            result +=1
    print(result)
