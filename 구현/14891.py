'''
8개의 톱니가진 바귀 4개 
각 톱니는 N극 S극 중 하나 
가장 왼쪽이 1번 , 가장 오른쪽은 4번
이때 총 K번 회전 (시계 또는 반시계)

이때 어떤 톱니를 회전시킬지와 회전방향 결정
이때 인접한 톱니와 맞닿은 극이 다르면 회저방향의 반대방향으로 회전, 
같으면 회전하지 않는다. 


톱니바퀴의 초기상태와 톱니바퀴 회전시킬 방법이 주어질때  최종 톱니바퀴사애 구하라

첫째 줄에 1번톱니 상태 => 8개의 정수 12방향부터 시계방향순서로 주어짐 
N극은 0 , S극은 1

5번째 줄부터 회전 횟수 K주어지고, 
회전시킬 방법은 [회전시킨 톱니바퀴 번호 , 방향] , 1인경우 시계 , -1경우 반시계
'''

# K번 회전시킨 이후 네 톱니바퀴의 점수의 합을 출력 
'''
1번 톱니바퀴의 12시방향이 N극이면 0점, S극이면 1점
2번 톱니바퀴의 12시방향이 N극이면 0점, S극이면 2점
3번 톱니바퀴의 12시방향이 N극이면 0점, S극이면 4점
4번 톱니바퀴의 12시방향이 N극이면 0점, S극이면 8점

N극은 0 , S극은 1
'''
from  collections import deque
Tire = [[] for _ in range(5)]
for i in range(1,5):
    Tire[i].append(deque(list(map(int , input()))))
K = int(input())
C = []
for _ in range(K):
    C.append(list(map(int , input().split())))

def rotate_disk(T , d):
    if d == 1: # 시계방향 회전
        tmp = T.pop()
        T.appendleft(tmp)
    elif d==-1:
        tmp = T.popleft()
        T.append(tmp)
def check_left(idx , L , r , rotation:list):
    
    while idx-1 >=1:
        if Tire[idx-1][0][2] != L:
            # 회전해야 하는 바퀴
            rotate = -1 if r == 1 else 1
            rotation.append((idx-1 , rotate))
            # 다음 왼쪽 확인을 위한 업데이트
            idx -=1
            r = rotate 
            L = Tire[idx][0][6]
        else:
            break
def check_right(idx , R , r , rotation:list):
    while idx+1 <=4:
        if Tire[idx+1][0][6] != R:
            rotate =  -1 if r == 1 else 1
            rotation.append((idx+1 , rotate))
            idx +=1
            r = rotate 
            R = Tire[idx][0][2]
        else:
            break
        
# 명령어 대로 회전

for c in C:
    rotation = [] # [idx , 회전방향]
    idx , r = c
    rotation.append((idx,r))
    L, R = Tire[idx][0][6] , Tire[idx][0][2]
    # 총 몇개 회전해야 하는지 확인
    check_left(idx , L , r , rotation)
    check_right(idx , R ,r , rotation)
    # print(rotation)
    # roration대로 회전
    for rotate in rotation:
        idx , r = rotate
        rotate_disk(Tire[idx][0] , r)

# 점수 계산
result = 0
for i in range(1,5):
    if Tire[i][0][0] == 1:
        result += 2**(i-1)
print(result)
    
    
    
   
    
    

