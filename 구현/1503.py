# 14503 gold5
'''
로봇 청소기 청소 영역 구하기
NxM 직사각형 (좌상단이 (0,0) , 우 하단이 (n-1,m-1))
1. 현재 칸을 청소
2. 현재 칸의 상하좌우 모두 청소 완료시
    1. 방향 유지한채 후진 하고 1번 반복
    2. 후진 안되는 경우 중단
3. 주변이 청소되지 않은 경우
    1. 반시계 방향 회전(북 -> 서 -> 남 -> 동)
    2. 해당 방향 앞이 청소안됬고 빈칸이면 전진
    3. 1번으로 이동

0 : 청소 되지 않은 빈칸
1 : 벽
방향
    0 : 북쪽 , 1:동 , 2:남 , 3: 서
출력 : 작동 정지까지 청소하는 칸 출력
'''
import sys
input = sys.stdin.readline
N , M = map(int , input().split())
y,x , d = map(int , input().split())
maps = []
for _ in range(N):
    maps.append(list(map(int , input().split())))

visited = [[False]*M for _ in range(N)]

directions = {0:(-1,0) , 1:(0,1) , 2:(1,0) , 3:(0,-1)}
result = 0
        
def is_allclean(y,x):
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    for ddx ,ddy in zip(dx,dy):
        ny , nx = ddy+y , ddx+x
        if 0<=nx<M and 0<=ny<N and maps[ny][nx] ==0 and not visited[ny][nx]:
           return False
    return True     
def back_p(y,x,d):
    if d ==0:
        return (y+1,x)
    elif d==1:
        return (y,x-1)
    elif d==2:
        return (y-1,x)
    elif d==3:
        return (y,x+1)
def is_vaild(y,x,check_visited = True):
    if 0<=y<N and 0<= x <M and maps[y][x] == 0 :
        if check_visited:
            if not visited[y][x]:
                return True
        else:
            return True
    return False

# print("현재 로봇 위치 : ",(y,x,d))
def dfs(y,x,d):
    # 현재 위치 청소
    if maps[y][x] == 0 and not visited[y][x]: 
        global result 
        result +=1
        visited[y][x] = True
        # print("청소 : " , (y,x,d,result))
    # 주변이 모두 청소가 된 경우
    if is_allclean(y,x):
        # 후진 가능한 경우 현재 방향 유지 후 1칸 후진
        # print("주변 모두 청소!")
        by , bx = back_p(y,x,d)
        if is_vaild(by,bx,check_visited=False):
            y,x,d = by,bx,d
            # print("후진 가능! => " , (y,x,d))
            dfs(y,x,d)
        else: # 후진 불가한 경우
            # print("후진 불가!! 중단" , (y,x,d))
            return 
    else: # 청소할 곳이 남은 경우 
        # print("주변 모두 안되었음!")
        for i in range(4):
            # 다음 방향 계산
            next_d = (d+3-i) % 4  
            next_P = directions[next_d]
            # 다음 이동 좌표 계산
            next_y , next_x = y+next_P[0] , x+next_P[1]
            # 다음 이동좌표가 청소가 안됬고, 빈칸인 경우 전진
            if is_vaild(next_y , next_x,check_visited=True):
                y,x,d = next_y , next_x , next_d
                # print("다음 이동 =>" , (y,x,d))
                
                # for i in range(N):
                #     for j in range(M):
                #         if i == y and j == x:
                #             print(f"*", end = "")  
                #         elif visited[i][j]:
                #             print("X" , end = "")
                #         else: print(f"{maps[i][j]}", end ="")  
                #     print()
                # print()
                dfs(y,x,d)
                break
    
dfs(y,x,d)
print(result)  