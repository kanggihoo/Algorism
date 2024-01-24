'''
바이러스 막기 위한 벽세우기
NxM 연구소, 빈칸 또는 벽으로(벽은 한칸차지)
일부 칸은 바이러스 존재, 상하좌우로 퍼지기 가능
벽은 3개 세우기 가능(꼭 3개 세우기)
0=> 빈칸
1=> 벽
2=> 바이러스
벽을 3개 세운 뒤 바이러스가 퍼질 수 없는 안전 영역의 최대값
'''

N , M = map(int , input().split())
MAP = []
for _ in range(N):
    MAP.append(list(map(int , input().split())))

# 빈칸인 좌표, 바이러스 위치 저장
def findPose_0_B():
    P_0 = []
    P_B = []
    for i in range(N):
        for j in range(M):
            if MAP[i][j] == 0:
                P_0.append((i,j))
            elif MAP[i][j] == 2:
                P_B.append((i,j))
    return P_0 , P_B

# 빈칸인 좌표들의 3가지 조합 구하기
result = []
def bfs(i,curL , tarL):
    if len(curL) == 3:
        result.append(curL.copy())
        return
    for j in range(i, len(tarL)):
        if j not in curL:
            bfs(j , curL+[j] , tarL)

def block(MAP , P_0 , *blocks):
    for b in blocks:
        y , x = P_0[b]
        MAP[y][x] = 1

def count(MAP):
    total = 0
    for i in range(len(MAP)):
        for j in range(len(MAP[0])):
            if MAP[i][j] == 0:
                total +=1
    return total

def print_map(MAP):
    for i in range(len(MAP)):
        for j in range(len(MAP[0])):
            print(f"{MAP[i][j]} " , end="")
        print()
    

P_0 , P_B = findPose_0_B()
bfs(0,[],P_0 )

safe_max = 0
# result에 들어가 있는 후보군에 벽돌 세우고 바이러스 이동
from collections import deque
import copy
for b1,b2,b3 in result:  
    MAP_ = copy.deepcopy(MAP)
    size_N , size_M = len(MAP_) , len(MAP_[0])
    # 벽돌 막기
    block(MAP_ ,P_0,b1,b2,b3)
    # 바이러스 이동
    dx = [0 , 0, 1,-1]
    dy = [1,-1 , 0 ,0]
    for vy,vx in P_B:
        Q = deque()
        Q.append((vy,vx))
        MAP_[vy][vx] = 2
        while Q:
            cy,cx = Q.popleft()
            
            for ddx , ddy in zip(dx,dy):
                ny,nx = cy+ddy , cx+ddx
                if ny >= 0 and ny < size_N and nx >=0 and nx < size_M and MAP_[ny][nx]==0:
                    Q.append((ny,nx))
                    MAP_[ny][nx] = 2
    # 바이러스 이동 종료(안전 범위 세기)
    
    safe_max = max(safe_max , count(MAP_))
    
    # MAP_ 삭제
    # if b1 ==0 and b2 == 4 and b3 == 16:
    #     print(b1,b2,b3)
    #     print(P_0[b1] , P_0[b2] , P_0[b3])
    #     print_map(MAP_)
    #     print(safe_max)
    #     break
    MAP_ = None
print(safe_max)

    
    
    

            

            
            
    
