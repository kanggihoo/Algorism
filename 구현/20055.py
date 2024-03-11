'''
길이 N 밸트가 위 아래 존재 하며 돌고 잇음 총(1~2N)
밸트가 한 칸 회전하면 1->2 ... 2N -> 1번 칸으로 이동
i번칸의 내구도는 A_i , 
1번 칸의 위치를 올리는 위치 , N번 칸이 내리는 위치  컨베이어 밸트에 로봇 올릴때 항상 올리는 위치에만 가능
내리는 위치 도달 시 즉시 내림. 
로봇 스스로 이동 가능, 올리는 위치에 올리거나 로봇이 특정 칸으로 이동시 칸의 내구도 1감소


1. 밸트가 각 칸의 로봇과 한칸 회전
2. 로봇이 이동하기 위해서는 이동하려는 칸에 로봇이 없고 내구도가 1이상 있는 경우
3. 올리는 위치의 내구도가 0이 아니면 로봇 올림
4. 내구도가 0인 칸이 K개 이상이면 종료
'''
from collections import deque
N , K = map(int , input().split())
A = list(map(int , input().split()))
A = deque(A)
step =1
cnt = 0
robots = deque([False for _ in range(N)])
def rotate(A , robots):
    n = A.pop()
    A.appendleft(n)
    n = robots.pop()
    robots.appendleft(False)
    robots[-1] = False
def move(robots,A):
    for i in reversed(range(N-1)):
        if robots[i] and not robots[i+1] and A[i+1] >0:
            robots[i+1] = robots[i]
            robots[i] = False
            A[i+1] -=1
    robots[-1] = False
def putrobot(robots , A):
    if not robots[0] and A[0] >0:
        robots[0] = True
        A[0] -=1
def check(A):
    cnt = 0
    for i in range(2*N):
        if A[i] == 0:
            cnt +=1
    if cnt >= K:
        return True
    else:
        return False
 
def show(A , robots):
    print(A)
    print(robots)           
    
while cnt < K:
    # print(step)
    # 회전
    rotate(A, robots)
    # show(A,robots)
    # move
    move(robots, A)
    # show(A,robots)
    # 로봇 올리기
    putrobot(robots , A)
    # show(A,robots)
    # 내구도 0인 것 확인
    if check(A):
        break
    
    # print(A)
    # print(robots)
    step+=1
print(step)
    
    


