from collections import deque
S = list(input().strip())
S = deque(S)
perfix = []
while S:
    perfix.append("".join(S.copy()))
    S.popleft()
perfix.sort()
for i in perfix:
    print(i)
