'''
R:뒤집기, D:첫번째 수 버리기
배열 비어 있는데 D인경우 에러발생

배열초기값과 수행함수 주어질때 최종 결과 구하기 

'''
import sys
input = sys.stdin.readline
from collections import deque
T = int(input())
for _ in range(T):
    funcs = list(input().strip())
    N = int(input())
    arr = input().strip()
    if N >=2:
        arr = deque(arr[1:-1].split(","))
    elif N == 1:
        num = arr[1:-1]
        arr = deque()
        arr.append(num)
    else:
        arr = deque()
    R = "F" # 정방향
    flag = True
    for f in funcs:
        if f =="R":
            R = "B" if R =="F" else "F"
        else:
            if not len(arr):
                flag = False
                break  
            if R =="F":
                arr.popleft()
            elif R=="B":
                arr.pop()
    if flag:
        if R=="B":
            answer = "["+",".join(reversed(arr))+"]"
        else:
            answer = "["+",".join(arr)+"]"
        print(answer)
    else:
        print("error")

    
