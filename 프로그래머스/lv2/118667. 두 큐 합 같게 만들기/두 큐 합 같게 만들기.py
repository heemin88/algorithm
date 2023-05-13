from collections import deque
def solution(queue1, queue2):
    q1 = deque(queue1)
    q2 = deque(queue2)
    q_sum = (sum(i for i in q1)+sum(i for i in q2))//2 #만들어야 할 합
    q1_sum = sum(i for i in q1)
    q2_sum = sum(i for i in q2)
    cnt =0
    left = 0
    right = len(queue1)
    new_q = queue1+queue2
    while True:
        if left == len(new_q)-1:
            return -1
            break
        if right == len(new_q): right =0
        if q1_sum > q_sum :
            q1_sum -= new_q[left]
            q2_sum += new_q[left]
            left +=1
            cnt+=1
        if q2_sum > q_sum:
            q2_sum -= new_q[right]
            q1_sum += new_q[right]
            right +=1
            cnt+=1
        if q1_sum == q_sum and q2_sum == q_sum:
            return cnt