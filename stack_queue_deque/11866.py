# 1~N명 원, K가 주어지면 k번재 사람 제거
from collections import deque

N , K = map(int , input().split())
Q = deque([i for i in range(1,N+1)])
sequence = []
while Q:
    for _ in range(K-1):
        num = Q.popleft()
        Q.append(num)
    sequence.append(Q.popleft())
sequence = ", ".join(map(str , sequence))
print("<"+sequence+">")
    
