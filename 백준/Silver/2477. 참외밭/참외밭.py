if __name__ == "__main__":
    k = int(input())
    arr = []
    for i in range(6):
        list = input().split()
        arr.append([int(list[0]),int(list[1])])
    w =0; w_idx =0
    h =0; h_idx = 0
    # 가로 최댓값, 세로 최댓값 찾
    for i in range (len(arr)):
        if arr[i][0] ==1 or arr[i][0]==2:
            if w < arr[i][1]:
                w=arr[i][1]
                w_idx=i
        else:
            if h < arr[i][1]:
                h=arr[i][1]
                h_idx=i
    big_len = w * h
    sub_w = abs(arr[(w_idx-1)%6][1] - arr[(w_idx+1)%6][1])
    sub_h= abs(arr[(h_idx-1)%6][1] - arr[(h_idx+1)%6][1])
    print(k * (big_len-(sub_w * sub_h)))