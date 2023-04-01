import sys
a,b,c =map(int,sys.stdin.readline().split())
def mul(end):
    if end==1: return a%c
    temp = mul(end//2)
    if end %2 ==1:
        return (temp*temp%c)*a%c
    else:
        return temp * temp % c


print(mul(b))