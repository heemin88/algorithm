def solution(numbers): #서로 다른 인덱스에 있는 두 개의 수를 뽑아 더해서 만들 수 있는 모든 수
    answer = set()
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            answer.add(numbers[i]+numbers[j])
    answer = sorted(answer)
    return list(answer)