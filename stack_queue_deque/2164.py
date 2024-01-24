from collections import deque

N = int(input())
Q = deque([i for i in range(1,N+1)])

while len(Q) > 1:
    Q.popleft()
    num = Q.popleft()
    Q.append(num)
print(Q[0])