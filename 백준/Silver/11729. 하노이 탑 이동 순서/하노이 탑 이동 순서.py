
import sys
move = []
def hanoitop(n,a,b):
    if n==1 :
        print(a,b)
    else:
        hanoitop(n-1,a,6-a-b) # 1->2으로 옮기는 과정
        print(a,b) # 옮겼다는 뜻.
        hanoitop(n-1,6-a-b,b) # 2->3으로 옮기는 과정

if __name__ == "__main__":
    n = sys.stdin.readline() #첫번째 장대에 쌓인 원판의 개수
    print(2**int(n)-1)
    hanoitop(int(n),1,3)
