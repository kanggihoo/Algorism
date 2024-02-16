'''
NxM 지도 
지도 위 주사위 (x,y)에 위치 초기 모든 면은 0으로 적힘
지도의 각 칸은 정수가 쓰여져 있음. 
주사위 굴렸을때 0이 나오면 주사위 바닥면에 쓰인 수가 칸에 복사
0이 아닌 경우 칸에 쓰인 수가 주사위의 바닥면으로 복사 후 칸은 0으로 변경

주사위가 이동시마다 주사위 상단에 쓰여 있는 값을 구하시오, 
지도 바깥으로 나가는 명령은 아무런 동작 하지 않음(출력도 안함)



x가 배열상 y값 , y가 배열상 x값
처음 주사위 놓는 칸은 항상 0 
각 칸의 수는 0~9 
동:1 , 서:2 , 북:3 , 남:4
'''
import sys
from collections import deque
input = sys.stdin.readline
N , M , x,y, K  = map(int , input().split())
maps = []
for _ in range(N):
    maps.append(list(map(int , input().split())))
    
C = list(map(int , input().split()))
DICE = [0]*7

def value_move(C , D):
    if C == 1:
        D[1],D[4],D[3],D[6] = D[3],D[1],D[6],D[4]
    elif C==2:
        D[3],D[1],D[6],D[4] = D[1],D[4],D[3],D[6]
    elif C==3:
        D[1],D[5],D[6],D[2] = D[2],D[1],D[5],D[6]
    elif C == 4:
        D[2],D[1],D[5],D[6] = D[1],D[5],D[6],D[2]
def position_move(C, x,y):
    if C == 1:
        return x,y+1
    elif C==2:
        return x , y-1
    elif C==3:
        return x-1 , y
    elif C==4:
        return x+1,y
        
# K번 반복
for c in C:
    nx,ny = position_move(c , x,y)
    if 0<=nx<N and 0<=ny < M :
        value_move(c , DICE)
        if maps[nx][ny] ==0: # 주사위 바닥면 값으로 변경
            maps[nx][ny] = DICE[1]
            # 주사위 윗면 출력
            print(DICE[6])
        elif maps[nx][ny] !=0: # 주사위 바닥면 값 변경
            DICE[1] = maps[nx][ny]
            maps[nx][ny] = 0
            print(DICE[6])
        # 현재 위치 변경
        x,y = nx,ny
        


        
            
        
    
        
    

