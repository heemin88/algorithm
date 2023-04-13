def solution(numbers, hand):#눌러야할 번호/ 오른손잡이,왼손잡이 여부
    answer = ''
    now_left = -1 #현재 왼손 손가락 위치 
    now_right =-2 # 현재 오른손 손가락 위치
    pad = {1:(0,0), 2:(0,1), 3:(0,2),
           4:(1,0), 5:(1,1), 6:(1,2),
           7:(2,0), 8:(2,1), 9:(2,2),
           -1:(3,0), 0:(3,1), -2:(3,2)
        }
    for num in numbers:
        #print(num,"left",now_left, "right",now_right)
        if num == 1 or num ==4 or num==7:
            answer += 'L'
            now_left = num
        elif num==3 or num==6 or num==9:
            answer += 'R'
            now_right =  num
        else: #중간 키패드일때
            #거리 구하기
            left_len = abs(pad[num][0]-pad[now_left][0]) + abs(pad[num][1]-pad[now_left][1])
            right_len = abs(pad[num][0]-pad[now_right][0]) + abs(pad[num][1]-pad[now_right][1])
            if left_len < right_len: #왼손이 더 가까울때 
                now_left = num
                answer +='L'
            elif left_len > right_len:
                now_right=num
                answer +='R'
            else:
                if hand == "right":
                    now_right=num
                    answer +='R'
                else:
                    now_left = num
                    answer +='L'
        
            
    return answer