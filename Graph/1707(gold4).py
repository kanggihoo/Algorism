# # 각 집합에 속한 노드끼리 인접하지 않는 두 집합으로 그래프를 나눌 수 있을 때 이 그래프를 이분 그래프 라고 한다.
# # 그래프가 입력으로 주어졌을 때 이분 그래프인지 여부 판별 프로그램 작성

# import sys
# from collections import deque

# def BFS(start):
#     Q = deque()
#     Q.append(start)
#     visited[start] = 0
#     while Q:
#         node = Q.popleft()
#         for i in graph[node]:
#             if visited[i] == 1:
#                 visited[i] =0
#                 Q.append(i)
    

# input = sys.stdin.readline
# K = int(input()) # k = 2~5
# for _ in range(K):
#     V, E = map(int , input().split())
    
#     # 그래프 만들기(양버)
#     graph = [[] for _ in range(V+1)]
#     for _ in range(E):
#         n1, n2 = map(int , input().split())
#         graph[n1].append(n2)
    

    
#     flag = True
#     # 아무 노드에 대하여 BFS 후 모든 노드가 방문되면 이진 그래프 아님 
#     for i in range(1,V+1):
#         visited = [1 for _ in range(V+1)]
#         BFS(i)
#         if sum(visited[1:]) == 0:
#             print('NO')
#             flag = False
#             break
#     if flag:
#         print('YES')
    
    
    
