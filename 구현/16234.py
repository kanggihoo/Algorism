'''
NxN 땅, 각 땅에는 나라가 존재 
(r,c)의 나라에는 A[r][c]명 거주, 인접한 나라 사이 국경선 존재 

인구이동이 없을 때까지 계속 진행
1.인근 두 나라의 인구 차이가 L~R명 이면 두 나라의 국경선을 개방
2. 국경선이 열리면 인구 이동 시작
3. 국경선이 열려있으며 그 나라를 "연합"
4. 연합을 이루고 있는 각 칸의 인구수 = (연합 인구수) / (연합을 이루는 칸의 개수) => 소수점은 버림
5. 연합을 해체 후 국경선 닫기
인구 이동이 몇일간 발생하는지 구하기

'''
import sys
input = sys.stdin.readline
N , L , R = map(int , input().split())
A = []
for _ in range(N):
    A.append(list(map(int , input().split())))

# 모든 노드에 대하여 인접 노드 참고해서 개방가능한 노드 모두 탐색 
# 각 연합 별 총 인구수 구하고, 연합 개수 구해서 해당되는 노드의 값을 변경
# 위의 과정을 계속 반복하되 , 인구 차이 조건에 해당되는 연합이 없으면 중단

# 모든 노드에 대하여 개방 가능한 노드 탐색
def bfs(start , visited):
    y, x = start
    visited[y][x] = True
    Q = deque()
    Q.append((y,x,A[y][x]))
    dy =[0,0,1,-1]
    dx =[1,-1,0,0]
    total_count = 0
    total_p = 0
    unions = []
    while Q:
        cy,cx,p = Q.popleft()
        total_count +=1
        total_p += p
        for ddy,ddx in zip(dy,dx):
            ny,nx = ddy+cy , ddx+cx
            if 0<=ny<N and 0<= nx < N and not visited[ny][nx]:
                np = A[ny][nx]
                
                if L<=abs(np-p)<=R:
                    Q.append((ny,nx,A[ny][nx]))
                    unions.append((ny,nx))
                    visited[ny][nx] = True
    # 같은 union 값의 인구수 최신화
    if len(unions):
        avg_p = int(total_p / total_count)
        A[y][x] = avg_p
        # print(f"start : {start} | total_count : {total_count} | total_p : {total_p}",
        #     f"avg : {avg_p} , | unions : {unions}"  )
        for union in unions:
            A[union[0]][union[1]] = avg_p
        return True
    else:
        return False   
            
    


from collections import deque
step = 0
while 1:
    visited = [[False]*N for _ in range(N)]
    flag = False
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                if bfs((i,j),visited):
                    flag = True
    if flag:
        step +=1
    else:
        break
print(step)