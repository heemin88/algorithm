def change(n,q):
    result = ""
    while n>0:
        n,mod = divmod(n,q)
        result += str(mod)
    return result
def solution(n):
    answer = 0
    c = change(n,3)
    return int(c,3)
