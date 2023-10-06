from itertools import permutations
def solution(numbers):
    # 정수를 이어 붙여 만들 수 있는 가장 큰 수 
    answer = ''
    number_str = [str(x) for x in numbers]
    number_str = sorted(number_str,key = lambda x : x*3,reverse = True)
    return str(int(''.join(number_str)))