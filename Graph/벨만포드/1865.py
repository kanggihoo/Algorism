'''
N개의 지점, N개의 지점 사이에는 M개의 도로와 W개의 웜홀(도로 방향X, 웜홀은 방향존재)
웜홀은 시작 -> 도착위치로 가는 하나의 경로이며 도착시 웜홀내에서는 시계가 거꾸로 간다.

한지점에서 출발하여 다시 출발위치로 돌아왔을때 시간이 되돌아가는 경우 있는지 확인

'''
import sys
input = sys.stdin.readline
import math 

INF = math.inf
def start(s , E):
    distance = [200000000]*(N+1)  
    distance[s] = 0
    for i in range(N-1):
        for n1 , n2 , cost in E:
            if distance[n2] > distance[n1] + cost:
                distance[n2] =  distance[n1] + cost
    
    for n1, n2 , cost in E:
        if distance[n2] > distance[n1]+cost:
            return True
    return False
                    
T = int(input())
for _ in range(T):
    N , M , W = map(int , input().split()) # 지점수 , 도로수 , 웜홀 수 
    E = []
    for _ in range(M): # 도로정보
        n1 , n2 , time = map(int , input().split())
        E.append((n1,n2,time))
        E.append((n2,n1, time))
    for _ in range(W) : # 웜홀정보 
        n1 , n2 , time = map(int , input().split())
        E.append((n1,n2,-time))
    
    if start(1,E):
        print("YES")
    else:
        print("NO")
            
    