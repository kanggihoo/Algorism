'''
검정색 루피 획득시 보요 소지금 감소
NxN 맵에서 (0,0)에 위치 => (N-1,N-1)로 이동
동굴의 각 칸마다 검정 루피가 있는데 해당 크기만큼 소지금 잃음
잃는 금액을 최소로 하여 출구까지 이동 , 상하좌우 이동가능

'''
import heapq
import sys
input = sys.stdin.readline
step = 1
while 1:
    N = int(input())
    if N == 0:
        break
    maps = []
    for _ in range(N):
        maps.append(list(map(int , input().split())))
    hq = []
    heapq.heappush(hq, (maps[0][0],0,0))
    INF = float("inf")
    distance = [[INF]*N for _ in range(N)]
    distance[0][0] = maps[0][0]
    dx = [0,0,-1,1]
    dy = [1,-1,0,0]
    while hq:
        
        dist, cy , cx  = heapq.heappop(hq)
        if distance[cy][cx] == INF:
            continue
        for ddy ,ddx in zip(dy,dx):
            ny ,nx = ddy+cy , ddx+cx
            if 0<=ny < N and 0<=nx<N:
                weight = maps[ny][nx]
                tmp = dist + weight
                if distance[ny][nx] > tmp:
                    distance[ny][nx] = tmp
                    heapq.heappush(hq , (tmp , ny,nx))

    print(f"Problem {step}:",distance[N-1][N-1])
    step +=1