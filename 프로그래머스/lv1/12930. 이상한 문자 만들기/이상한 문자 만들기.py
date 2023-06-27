def solution(s):
    answer = '' # 각 단어의 짝수번째 알파벳은 대문자, 홀수번째는 소문자로 바꾼 문자열을 리턴
    S= s.split(" ")
    for k,ss in enumerate(S):# 각 단어마다
        for i in range(len(ss)):
            if i%2 == 0: #짝수면 
                answer += ss[i].upper()
            else: # 홀수면 
                answer += ss[i].lower()
        if k != len(S)-1:
            answer += " "
    return answer