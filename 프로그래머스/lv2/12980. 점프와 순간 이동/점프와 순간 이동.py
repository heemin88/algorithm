def solution(n):
    ans = 0
    while n >0:
        n,w = divmod(n,2)
        ans +=w
    return ans