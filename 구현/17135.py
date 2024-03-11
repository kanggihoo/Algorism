'''
NxM 격자판 
각 칸에 포함된 적의 수는 한명
격자판의 N+1행의 모든 칸은 성

성을 지키기 위해 궁수 3명 배치
궁수는 성에 배치 가능 , 
각 턴마다 적 하나 공격하며 모든 궁수는 동시에 공격
궁수는 사거리 D이내의 가장 가까운 적 공격, 그러한 적이 여럿일 경우
가장 왼쪽에 있는 적을 공격(같은 적이 여러 궁수에게 공격당할 수 있음)
공격받은 적은 게임에서 제외,

궁수 공격 후 적이 이동(적은 아래로 한칸 이동, 성에 도착시 게임에서 제외)
모든 적이 제외되면 게임 종료


궁수를 배치한 이후의 게임 진행은 정해져 잇음. 
격자판이 주어질때 , 궁수의 공격으로 제거 가능한 적의 최대수 계산
'''
# 0은 빈칸 , 1은 적있는 칸 
N , M , D = map(int , input().split())
maps = []
for _ in range(N):
    maps.append(list(map(int , input().split())))
from  itertools import combinations
from collections import deque
def attack(archer,maps):
    y,x = N , archer
    dx = [-1,0,1]
    dy = [0,-1,0] 
    Q = deque()
    Q.append((y,x,0))
    visited = [[False]*M for _ in range(N)]
    while Q:
        cy,cx,depth = Q.popleft()
        tmp = []
        for ddy , ddx in zip(dy,dx):
            ny , nx = cy+ddy , cx+ddx 
            if 0<=ny<N and 0<=nx<M and depth < D and not visited[ny][nx]: 
                if maps[ny][nx] == 1:
                    tmp.append((ny,nx,depth))
                Q.append((ny,nx,depth+1))
                visited[ny][nx] = True
        if tmp:
            tmp.sort(key= lambda x : (x[2],x[1],x[0]) , reverse=True)
            y,x = tmp.pop()[:2]
            return y,x
    return False        
        
def move(maps):
    # 성문에 도착하여 제외되는 경우
    exclude_m = sum(maps[-1])
    for i in reversed(range(1,N)):
        maps[i] = maps[i-1]
    maps[0] = [0 for _ in range(M)]
    return exclude_m

case = list(combinations(range(M) , 3))
result = 0
total_m = sum(sum(m) for m in maps)
import copy 
for c in case:
    Archers = c
    T = 0
    TM = total_m
    ans = 0
    new_map = copy.deepcopy(maps)
    # print(c)
    while TM and T < N+1:
        # 공격 동시에 공격해야 하나!! 
        attacked = []
        for A in Archers:
            monster_p = attack(A,new_map)
            if monster_p:
                attacked.append(monster_p)
        # 업데이트
        for a in set(attacked):
            y, x = a
            new_map[y][x] = 0
            ans+=1
            TM -=1
        # 이동
        TM -= move(new_map)
        # show()
        T+=1
    result = max(result , ans)
print(result)
    
    
    

