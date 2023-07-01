def solution(n, times): #입국 심사 기다리는 사람/ 심사관이 한 명을 심사하는데 걸리는 시간
    
    answer =0 
    left= min(times)
    right = max(times)*n #가장 비효율적일 때 검사한 시간 
    
    while left<=right:
        mid = (left+right) //2
        people =0 # mid시간동안 입국심사할 수 있는 사람 수
        for time in times:
            people += mid//time # 각 time마다 mid시간동안 입국심사할 수 있는 사람
            if people >=n: #모든 심사관을 안거쳐도 n보다 많거나 같으면 탈출
                break
        if people >= n:
            answer = mid
            right = mid-1
        else:
            left = mid +1 
    return answer