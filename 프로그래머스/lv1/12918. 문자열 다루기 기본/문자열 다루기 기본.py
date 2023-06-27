def solution(s):
    if len(s) == 4 or len(s)==6 :
        for ss in s:
            if 48<=ord(ss)<= 57:
                continue
            else:
                return False
    else:
        return False
                
    return True