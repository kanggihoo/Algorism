import sys
input = sys.stdin.readline

N = int(input())
classes = []
for _ in range(N):
    classes.append(list(map(int , input().split())))
classes.sort(key = lambda x: (x[0] , x[1]) , reverse = True)

import heapq
E = 0
c = classes.pop()
HQ = [c[1]]
while classes:
    cs , ce = classes.pop()
    if HQ[0] <= cs:
        heapq.heappop(HQ)
        
    heapq.heappush(HQ,ce)
print(len(HQ))
    