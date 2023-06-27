
def int2base(num,k):
    res = ''
    while num>0:
        num , mod = divmod(num,k)
        res+=str(mod)
    return res[::-1]#String값을 거꾸로 변환해줘야 원하는 진수값이 들어가 있음.
def is_sosu(num):
    if num <=1 : return False
    for i in range(2,int(num**(0.5))+1):
        if num%i == 0 :
            return False
    return True

def solution(n, k):
    #소수는 각 자릿수에 0을 포함하지 않는 소수
    answer = 0 #n을 k진수로 바꿨을 때, 변환된 수 안에서 찾을 수 있는 소수의 개수 
    n = int2base(n,k)
    result =''
    loc = -1 #0의 마지막 위치 
    num = n.split('0')
    for i in num:
        if i != '' and is_sosu(int(i)):
            answer +=1
        
    return answer