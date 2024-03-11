# 색종이 만들기 
import sys
input = sys.stdin.readline
N = int(input())
MAP = []
for _ in range(N):
    MAP.append(list(map(int , input().split())))
W ,B = (0,0)
def divide(y,x,n):
    if n == 1:
        global W ,B
        if MAP[y][x] == 1:
            B+=1
        else:
            W+=1
        return
    # 4개로 분할
    for i in
    
    