'''
노드갯수, 간선이 주어지면
주어진 그래프에서 트리

'''
from collections import deque

N , M = map(int , input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    n1, n2 = map(int , input().split())
    graph[n1].append(n2)
    graph[n2].append(n1)

parents = [i for i in range(N+1)] # 자기 자신이 부모 노드
visited = [False for i in range(N+1)] # 방문 여부 확인

def find(node):
    if node != parents[node]:
        parents[node] = find(parents[node])
    return parents[node]

def union(a ,b):
    p_a , p_b = find(a) , find(b)
    if p_a > p_b:
        parents[a] = p_b
    else:
        parents[b] = p_a

def bfs(start):
    Q = deque()
    Q.append(start)
    
    while Q:
        cur = Q.popleft()
        
        for adj in graph[cur]:
            if not visited[adj]: # 방문하지 않은 인접노드
                # 현재 노드와 인접노드가 같은 그룹인지 확인
                if find(cur) != find(adj):
                    union(cur , adj) # 합치기 연산
                    visited[adj] = True # 방문체크
                    Q.append(adj)
                else: # 인접노드와 현재 노드가 같은 그룹인 경우 순환발생
                    return False
    
    return True

                
                    
            



# 모든 노드에 대하여 검사
num_T = 0
for i in range(1,N+1):
    if not visited[i]: # 방문되지 않은 노드인 경우
        visited[i] = True 
        print("start node : " , i)
        if bfs(i): # 트리 발생시 True 반환
            print("make tree!!")
            num_T +=1
        else:
            print("can't make tree")
print(graph)  
print(num_T)
print(parents)
        
        
'''
노드갯수, 간선이 주어지면
주어진 그래프에서 트리

'''
        
# from collections import deque
# def find(node):
#     if node != parents[node]:
#         parents[node] = find(parents[node])
#     return parents[node]

# def union(a ,b):
#     p_a , p_b = find(a) , find(b)
#     if p_a > p_b:
#         parents[a] = p_b
#     else:
#         parents[b] = p_a
        
# def bfs(start):
#     Q = deque()
#     Q.append(start)
    
#     while Q:
#         cur = Q.popleft()
        
#         for adj in graph[cur]:
#             if not visited[adj]: # 방문하지 않은 인접노드
#                 # 현재 노드와 인접노드가 같은 그룹인지 확인
#                 if find(cur) != find(adj):
#                     union(cur , adj) # 합치기 연산
#                     visited[adj] = True # 방문체크
#                     Q.append(adj)
#                 else: # 인접노드와 현재 노드가 같은 그룹인 경우 순환발생
#                     return False
    
#     return True
   
# T_case =0
# while 1:
#     N , M = map(int , input().split())
#     T_case +=1
#     if N ==0 and M ==0:
#         break
#     graph = [[] for _ in range(N+1)]
#     for _ in range(M):
#         n1, n2 = map(int , input().split())
#         graph[n1].append(n2)
#         graph[n2].append(n1)

#     parents = [i for i in range(N+1)] # 자기 자신이 부모 노드
#     visited = [False for i in range(N+1)] # 방문 여부 확인

#     # 모든 노드에 대하여 검사
#     num_T = 0
#     for i in range(1,N+1):
#         if not visited[i]: # 방문되지 않은 노드인 경우
#             visited[i] = True 
#             if bfs(i): # 트리 발생시 True 반환    
#                 num_T +=1
    
#     if num_T ==0:
#         print(f"Case {T_case}: No trees.")
#     elif num_T ==1:
#         print(f"Case {T_case}: There is one tree.")
#     else:
#         print(f"Case {T_case}: A forest of {num_T} trees.")



        