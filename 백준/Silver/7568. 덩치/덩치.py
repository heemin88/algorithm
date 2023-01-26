if __name__ == "__main__":
    n = int(input())
    info = []
    for i in range(n):
        temp = input().split()
        info.append((int(temp[0]), int(temp[1])))
    result = []
    for i in range(n):
        weight = info[i][0]
        height = info[i][1]
        rank = 1
        for j in range(n):
            if i == j:
                continue
            elif weight < info[j][0] and height < info[j][1]:
                rank += 1
        result.append(rank)
    for i in result:
        print(i, end=" ")