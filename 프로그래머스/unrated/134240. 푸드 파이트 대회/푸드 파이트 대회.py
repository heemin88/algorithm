def solution(food): #칼로리가 적은 순서대로 나타냄.
    #음식의 종류 양이 같아야함. 음식 먹는 순서 같아야함. 칼로리낮은 음식부터 배열
    answer = ''
    food.pop(0)
    for i in range(len(food)):
        food[i]= food[i]//2
    for i in range(len(food)):
        answer += str(i+1)*food[i]
    return answer+'0'+answer[::-1]