# '''
# 바이러스 유출, (활성, 비활성 상태) => 초기에는 비활성
# 활성화 되면 상하좌우 빈칸으로 복제 => 1초 걸림
# 바이러스 M개를 화성상태를 변경
# N N 연구소 , 활성 바이러스가 비활성 바이러스로 가면 비활성은 활성상태됨
# 0 :빈칸 , 1:벽 , 2: 바이러스 (활성상태 3)
# 모든 빈 칸에 바이러스 퍼트리는 최소 시간
# '''
# from collections import deque
# N , M = map(int , input().split())
# maps = []
# for _ in range(N):
#     maps.append(list(map(int , input().split())))

# # 바이러스 위치 찾기 
# def find_v():
#     v = []
#     cnt = 0
#     for i in range(N):
#         for j in range(N):
#             if maps[i][j] == 2:
#                 v.append((i,j))
#             if maps[i][j] == 1:
#                 cnt +=1
#     return v , cnt

# # 바이러스 M개 퍼트리기
# import copy 
# def check(maps):
#     for i in range(N):
#         for j in range(N):
#             if maps[i][j] ==0:
#                 return False
#     return True
        
# def spred(vs ,block, maps):
#     # M개 활성으로 변경
#     global mintime 
#     visited = [[False]*N for _ in range(N)]
#     for v in vs:
#         y,x = v
#         maps[y][x] = 3
#         visited[y][x] = True
#     Q = deque([(y,x,0) for y,x in vs ])
#     dx = [0,0,-1,1]
#     dy = [1,-1,0,0]
#     ttime = 0
#     while Q:
#         cy , cx ,time= Q.popleft()
#         if mintime <= time:
#             return 
#         if block == 0:
#             return time
#         ttime = max(ttime , time)
#         for ddy , ddx in zip(dy,dx):
#             ny ,nx = cy+ddy , cx+ddx
#             if 0<=ny<N and 0<= nx < N and not visited[ny][nx] and maps[ny][nx] != 1:
#                 visited[ny][nx] = True
#                 if maps[ny][nx] == 0:
#                     maps[ny][nx] =3
#                     block -=1
#                     Q.append((ny,nx,time+1))
#                 elif maps[ny][nx] == 2:
#                     Q.append((ny,nx,time+1))
#                     maps[ny][nx] =3
#     mintime = min(mintime , time)

                    
        
# # 바이러스 중 M개 선택
# from itertools import combinations
# v,block = find_v()
# vpos = combinations(v , M)
# mintime = float("inf")
# for vs in vpos:
#     spred(vs ,block, copy.deepcopy(maps))
# if mintime == float("inf"):
#     print(-1)
# else:
#     print(mintime)
    
        