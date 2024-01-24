# # 벨만포드 인접 노드만 검사하는 것이 아닌 모든 엣지를 검사해야 해서 데이터 저장을 다른방식으로 함

# N개의 도시, M개의 버스 
# A,B,C : 시작 , 도착 , 비용 (C<0인경우 존재)
# 1번 도시에서 출발하여 나머지 도시로 가는 가장 빠른 시간 구하기
# 만약 음수 순환 간선이 존재하는 경우 -1 출력
# 그렇지 않다면 2, 3, 4,,,N번 도시로 가장 빠른 시간 순으로 출력 해당 도시로 가능 경로 없으면 -1 출력
import sys
import math

input = sys.stdin.readline
N,M = map(int, input().split())

edges = []
# 모든 엣지 정보 저장
for _ in range(M):
    S , E , C = map(int , input().split())
    edges.append((S,E,C))
# 거리정보
INF = int(1e9)
distance = [INF for _ in range(N+1)]
distance[0] = 0
distance[1] = 0
Start = 1
Negative_Circle = False 
# N번 반복(N-1번 반복 후 1번 더 반복했을 때 거리변화 있으면 음의순환 있는 것으로 판단.)
for step in range(N):
    
    # 모든 간선 조사
    for i in range(M):
        cur , next , cost = edges[i]
        # 현재 노드에서의 거리 정보가 INF 아 아닌 경우 , 업데이트 필요한 경우
        if distance[cur] != INF and distance[next] > distance[cur]+cost:
            distance[next] = distance[cur]+cost
            
            # N-1 일때 값에 변화가 발생하면 음의 순환 있는 것으로 판단
            if step == N-1:
                Negative_Circle = True

# 결과 출력
if Negative_Circle:
        print(-1)
else:
    for i in range(2,N+1):
        if distance[i] == INF:
            print(-1)
        else:
            print(distance[i])
        
    
    
    




