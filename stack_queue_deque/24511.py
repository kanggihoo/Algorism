import sys
from collections import deque
input = sys.stdin.readline
N = int(input())
QS = list(map(int , input().split()))
QS_num = list(map(int , input().split()))
M = int(input())
arr_M = list(map(int , input().split()))

DEQUE = deque()
# QS 가 0인 경우에만 deque에 저장 
for i in range(N):
    if QS[i] == 0:
        DEQUE.append(QS_num[i])

# QS에 저장된 값이 없는 경우는 M의 원소를 그대로 출력
if len(DEQUE):
    for i in arr_M:
        DEQUE.appendleft(i)
        print(DEQUE.pop() , end = " ")
else:
    for i in arr_M:
        print(i , end = " ")
        

        
