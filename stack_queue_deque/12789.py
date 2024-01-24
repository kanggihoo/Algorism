import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
arr = list(map(int , input().split()))
Q = deque(arr)
stack = []
for idx in range(1,N+1):
    # 스택에 마지막 값에 해당번호가 있으면 pop
    if stack and stack[-1] == idx:
        stack.pop()
        continue

    # 없으면 큐에서 해당번호가 나올 때까지 pop 하고 stack에 집어넣음
    if idx in Q:
        while Q[0] != idx:
            num = Q.popleft()
            stack.append(num)
        Q.popleft()
    else:
        print("Sad")
        break

if not Q and not stack:
    print("Nice")
    
            
        


    