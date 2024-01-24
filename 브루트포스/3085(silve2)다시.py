# N*N 사탕 넣기 (색은 같지 않을수도 있음)

from collections import Counter
import sys
input = sys.stdin.readline
N = int(input())
game_board = []
for i in range(N):
    game_board.append(list(input()))
    

def checkRowColMax(row , col):
    cnt = 1
    max_cnt = 1
    for i in range(1,N):
        if game_board[row][i-1] == game_board[row][i]:
            cnt +=1
        else:
            cnt = 1
        max_cnt = max(cnt , max_cnt)
        
    cnt = 1
    for i in range(1,N):
        if game_board[i-1][col] == game_board[i][col]:
            cnt +=1
        else:
            cnt = 1
        max_cnt = max(cnt , max_cnt)
    
    return max_cnt



max_value = 0
dx = [1 , 0 ]
dy = [0 , 1]
# 모든 좌표값 조사 
def findAllPosition(max_value):
    for i in range(N):
        for j in range(N):
            for ddx ,ddy in zip(dx , dy):
                cur = (i,j)
                move = (i+ddy , j+ddx)
                if (i+ddy > N-1) or (j+ddx > N-1):
                    continue
                c1 ,c2 = game_board[i][j] ,game_board[i+ddy][i+ddx]
                if c1 == c2:
                    continue
                # 서로 위치 변경
                game_board[i][j] , game_board[i+ddy][i+ddx] = game_board[i+ddy][i+ddx] , game_board[i][j]

                max_value = max(max_value , checkRowColMax(i,j))
                max_value = max(max_value , checkRowColMax(i+ddy,j+ddy))
                if max_value == N:
                    return max_value
                
print(findAllPosition(max_value))       
            
        

    
    
    
    