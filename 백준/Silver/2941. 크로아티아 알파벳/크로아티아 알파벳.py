if __name__ == "__main__":
    chro = ["c=","c-","dz=","lj","nj","s=","z=","d-"]
    chr = ['c','=','-','d','z','l','j','n','s']
    input = list(input())
    ch = ""
    result=0
    for i in range(len(input)):
        if input[i] in chr :
            ch = ch + input[i]
            if ch in chro:
                result += 1
                ch = ""
            elif len(ch) ==2 and ch !="dz":
                result +=1
                ch= input[i]
            elif len(ch)==3:
                result +=2
                ch = input[i]
        else :
            ch = ch+input[i]
            result += len(ch)
            ch =""
    print(result+len(ch))
