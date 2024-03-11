'''
K번째 최단경로

1번 도시가 시작도시
1번 => i번 도시로 가는 k번째 최단 경로소요시간 출력
k번째 최단이 없는 경우는 -1 출력
최단경로에 같은 정점이 여러번 포함되어도 됨. 

'''
import sys
input = sys.stdin.readline
n,m,k = map(int , input())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    n1 , n2 , c = map(int , input().split())
    graph[n1].append((n2,c))
