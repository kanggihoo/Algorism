import sys
from collections import deque

N, M = map(int, input().split())

graph = [[0]*M for i in range(N)]
check = [[-1]*M for i in range(N)]

for i in range(N):
    n = list(input())
    for j in range(M):
        graph[i][j] = int(n[j])
        if graph[i][j]:
            check[i][j] = 0

# BFS

start = [0, 0]
target = (N-1, M-1)
depth = 0
dx = [1, 0]
dy = [0, 1]
queue = deque([start])
check[start[0]][start[1]] = depth
depth += 1
while queue:
    cur = queue.popleft()
    for ddx, ddy in zip(dx, dy):
        print(cur, ddx, ddy)
        new_cur = [cur[0] + ddx, cur[1] + ddy]
        if (new_cur[0] >= 0 and new_cur[1] >= 0) and (new_cur[0] <= N-1 and new_cur[1] <= M+1):
            if graph[new_cur[0]][new_cur[1]] != 0:
                queue.append([new_cur])
                # dpeth 값 집어넣기
                check[new_cur[0]][new_cur[1]] = depth
                depth += 1

print(f"graph : {graph}")
print("")
print(check)
