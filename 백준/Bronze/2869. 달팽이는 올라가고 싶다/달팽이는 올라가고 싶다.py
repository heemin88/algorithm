if __name__ == "__main__":
    a,b,v = input().split()
    len = int(a) - int(b)
    v = int(v)
    a = int(a)
    days = 0

    v= v-a
    days += v // len
    if v%len >0 : days +=2
    else : days += 1
    print(days)

