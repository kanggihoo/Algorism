'''
N개의 도시(1~N) (도시간 연결이 있거나 없거나)
여행일정이 주어질 때 여행 가능한지 알아보기
=> union find로 해당 여행지의 대표값이 모두 같은지 확인해보면 될듯
'''
import sys
N = int(input())
M = int(input())
arr = []
for _ in range(N):
    arr.append(list(map(int , input().split())))

graph = [[] for i in range(N+1)] 
for i in range(N):
    for j in range(N):
        if arr[i][j] ==1:
            graph[i+1].append(j+1)

target = list(map(int , input().split()))

parents = [i for i in range(N+1)]

    
def find(x , parents):
    if x != parents[x]:
        parents[x] = find(parents[x] , parents)
    return parents[x]

def union(x,y,parents):
    p1 = find(x,parents)
    p2 = find(y,parents)
    if p1 > p2:
        parents[p1] = p2
    else:
        parents[p2] = p1
        
for i in range(1,N+1):
    for n in graph[i]:
        if find(i,parents) != find(n,parents ):
            union(i,n,parents )

if all(parents[target[0]] == parents[i] for i in target):
    print("YES")
else:
    print("NO")

    