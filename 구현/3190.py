'''
사과 먹으면 뱀 길이 늘어남, 뱀이 움직이다가 벽또는 자기와 부딪히면 게임 종료
NxN 보드, 특정 칸에는 사과 , 보드의 상하좌우 끝에는 벽
L : 왼쪽으로 90도 회전
D : 오른쪽으로 90도 회전
'''
N = int(input())
K = int(input())
apples = []
for _ in range(K):
    apples.append(list(map(int , input().split())))
L = int(input())
from collections import deque
D = deque()
for _ in range(L):
    time , direction = input().rstrip().split()
    D.append((int(time) , direction))

boards = [[0]*(N+2) for _ in range(N+2)] # 0이거나, N+1이 되면 벽을 만남
# 사과 위치를 반영(1이면 사과)
for apple in apples:
    y,x = apple
    boards[y][x] = 1
directions = {0:"북" , 1:"서" , 2:"남" , 3:"동"}
# 반시계 방향 : 북 -> 서 -> 남 -> 동 
# 시계 방향 : 북 -> 동 -> 남 -> 서
time = 0 
cx , cy = (1,1) 
d = 3
bodys = [[cy,cx]]
boards[cy][cx] = -1
eat_apple = False
def find_next(cx,cy , d):
    if d == 0:
        return cx , cy-1
    elif d == 1:
        return cx-1 , cy
    elif d ==2:
        return cx , cy+1
    elif d ==3:
        return cx+1 , cy
def show():
    for i in range(N+2):
        for j in range(N+2):
            if boards[i][j] == -1:
                print("*" , end ="")
            else:
                print(boards[i][j] , end ="")
        print()
    print()
    
         
while 1:
    # 시간 업데이트
    time +=1
    # 다음 방향 변화는지 여부 확인
    # print("cur : " ,(cy,cx))
    # 다음 위치 정보 구하기 
    nx , ny = find_next(cx,cy,d)
    # print("next : " , (ny,nx) ,"time: ",time , "dir : ",d)
    # 다음 위치가 벽인경우
    if ny ==0 or ny == N+1 or nx ==0 or nx ==N+1:
        break
    # 다음 위치가 사과 인경우(꼬리 고정 후 몸 늘림)
    elif boards[ny][nx] == 1:
        # 몸 늘리기
        bodys.append([ny,nx])
        eat_apple = True
        boards[ny][nx] = 0
    elif boards[ny][nx] == -1:
        break
    # 움직이기 
    if eat_apple:
        eat_apple=False
    else:
        boards[bodys[0][0]][bodys[0][1]] = 0 # 꼬리 위치의 좌표 0으로 변경
        for idx in range(len(bodys)-1):
            bodys[idx] = bodys[idx+1]
        # 몸의 맨 마지막 인덱스는 다음 위치로 변경
        bodys[-1] = [ny,nx]
    # 움직인 이후 자신의 몸과 만나는지 확인
    if boards[ny][nx] == -1:
        break
    # 다음 위치 업데이트
    boards[ny][nx] = -1
    cy , cx = ny, nx
    # 방향 전환
    if len(D) and D[0][0] == time:
        _, direct = D.popleft()
        if direct =="D": # 오른쪽 회전(시계방향)
            d = (d+3)%4
        else :           # 왼쪽 회전(반시계 방향)
            d = (d+1)%4
    # show()
    
print(time)  
