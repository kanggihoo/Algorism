'''
1: 집있음 , 0:빈집
상하좌우에 집이 있는 경우 연결됨
총 단지수를 출력하고
각 단지에 속하는 집의 수를 오름차순 정렬하여 출력

'''
import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
arr = []
for _ in range(N):
    arr.append(list(map(int , list(input().strip()))))
    
# x,y : BFS's start position , return : total Q length 
def BFS(x:int,y:int)->int:
    total = 0
    Q = deque()
    Q.append((x,y))
    arr[y][x] = 0
    dx = [0 , 0 , 1 , -1]
    dy = [1, -1 , 0 , 0]
    while Q:
        cur = Q.popleft()
        total +=1
        for ddx , ddy in zip(dx,dy):
            next_x , next_y = cur[0]+ddx , cur[1]+ddy
            if next_x >= 0 and next_x <=N-1 and next_y >= 0 and next_y <=N-1 and arr[next_y][next_x]==1:
                Q.append((next_x,next_y))
                arr[next_y][next_x] = 0
    return total
                

# check all (x,y)
result = []
for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            result.append(BFS(j,i))

result.sort()
print(len(result))
for i in result:
    print(i)

                
        
    
    
        