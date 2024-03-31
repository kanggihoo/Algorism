import sys
input = sys.stdin.readline

'''
1~N문제 , 1번이 가장 쉬움
    1. 모든 문제 풀어야함
    2. 먼저 풀면 좋은 문제는 반드시 먼저
    3. 가능한 쉬운 문제부터
'''

import heapq 
N , M = map(int , input().split())
G = [[] for _ in range(N+1)]
degrees = [0 for _ in range(N+1)]

for _ in range(M):
    A ,B = map(int , input().split())
    G[A].append(B)
    degrees[B] +=1

hq= [idx for idx , degree in enumerate(degrees[1:],1) if degree == 0]
# print(G)
# print(hq)
result = []
while hq:
    cur = heapq.heappop(hq)
    result.append(cur)
    
    for adj in G[cur]:
        if degrees[adj] >0:
            degrees[adj] -=1
        if degrees[adj] ==0:
            heapq.heappush(hq,adj)

for i in result:
    print(i,end=" ")
    


            