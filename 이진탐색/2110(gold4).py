'''
N개가 수직선 위 (같은 위치 없음)
공유기 C개 설치
한집에 한개의 공유기만 가능 
이때 가장 인접한 공유기 사이 거리를 최대로
출력 : 가장 인접한 공유기 사이 최대 거리
'''

import sys
input = sys.stdin.readline
N , C = map(int , input().split())
D = []
for _ in range(N):
    D.append(int(input()))

D.sort()
