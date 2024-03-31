import sys
input = sys.stdin.readline
from collections import deque

N , M = map(int , input().split())
G = [[] for _ in range(N+1)]
degrees = [0 for i in range(N+1)]
start = []
for _ in range(M):
    orders = list(map(int , input().split()))
    for i in range(1,len(orders)-1):
        a , b = orders[i] , orders[i+1]
        G[a].append(b)
        degrees[b] +=1
    start = [idx for idx , i in enumerate(degrees[1:],1) if i ==0]
# print(degrees)
# print(G)
# print(start)
def bfs(result:list):
    Q = deque()
    check = [False for i in range(N+1)] 
    for i in start:
        Q.append(i)
        result.append(i)
        check[i] = True
    while Q:
        cur = Q.popleft()
        for adj in G[cur]:
            if check[adj] == True: # degree가 0인데 다시 등장한 경우 오류 
                return False
            degrees[adj] -=1
            if degrees[adj] == 0:
                check[adj] = True
                result.append(adj)
                Q.append(adj)
    return True

result = []
if bfs(result) and len(result) == N: # 최종 결과물에 N명이 없으면 오류
    for i in result:
        print(i)
else:
    print(0)


        
        
