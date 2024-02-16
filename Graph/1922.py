'''
모든 컴퓨터가 연결 할때 최소 비용으로 연결
연결 비용이 주어졌을 때 모든 컴퓨터를 연결하는데 필요한 최소 비용
spainning tree 만들기 

'''
import sys
input = sys.stdin.readline
N = int(input())
E = int(input())
edges = []

for i in range(E):
    n1 , n2 , c = map(int,input().split())
    edges.append((n1,n2,c))
edges.sort(key = lambda x : x[2])

P = [i for i in range(N+1)]

def find_p(x):
    if P[x] != x:
        P[x] = find_p(P[x])
    return P[x]

def union(x1,x2):
    p1 = find_p(x1)
    p2 = find_p(x2)
    if p1 > p2:
        P[p1] = p2
    else:
        P[p2] = p1
result = 0
# MST = set()
for e in edges:
    n1,n2,c = e
    if find_p(n1) != find_p(n2):
        union(n1,n2)
        result += c
        # MST.add(n1)
        # MST.add(n2)
        # print(f"{n1} , {n2}" , c)
print(result)
# print(MST)
        
        