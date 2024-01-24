'''
정수 A를 B로 변경하기 위한 규칙
 - 2를 곱하기
 - 1을 가장 오른쪽에 추가
 최소 연산횟수 반환

'''
# A ,B = map(int , input().split())

# result = []
# dfs 구현
# def dfs(num:int,depth:int):
#     if num > B:
#         return
#     elif num == B:
#         result.append(depth)
#         return
        
#     # 1을 오른쪽에 추가
#     dfs(int(str(num)+"1") , depth+1)
#     # 2곱하기
#     dfs(num*2 , depth+1)
# dfs(A,0)
# if len(result):
#     print(min(result)+1)
# else:
#     print(-1)

# bfs 구현
A ,B = map(int , input().split())
result = None
from collections import deque
Q = deque()
Q.append((A,0))
while Q:
    cur_num , cur_depth = Q.popleft()
    
    # bfs 방법은 최단 거리 즉 최소한의 연산횟수를 보장하므로 Q에서 B값이 나오면 중단
    if cur_num == B:
        result = cur_depth
    # 오른쪽에 1추가
    n1 = int(str(cur_num)+"1")
    # 2곱하기
    n2 = cur_num*2
    if n1 <= B:
        Q.append((n1,cur_depth+1))
    if n2 <= B:
        Q.append((n2,cur_depth+1))    
if result:
    print(result+1)
else:
    print(-1)
            
    
