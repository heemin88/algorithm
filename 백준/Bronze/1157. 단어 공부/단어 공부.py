if __name__ == "__main__":
    input = list(input().upper())
    max = 0
    result = ''
    c = list(set(input))
    for i in range(len(c)):
        num = input.count(c[i])
        if max == num : result = '?'
        if max < num:
            max = num
            result = c[i]
    print(result)