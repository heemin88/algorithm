
success=False
cnt=0
answer = 0
def solution(word):
    dic = ['A','E','I','O','U']
    cnt = 0
    def dfs(string):
        global success,cnt,answer
        if len(string)>5: return
        
        cnt +=1
        if string == word:
            answer = cnt
            success=True
            return cnt
        for s in dic:
            dfs(string+s)
            if success : 
                return 
    dfs("")
    
    return answer-1
