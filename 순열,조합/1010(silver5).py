# 동과서를 나누는 강이 있고 이를 건너기 위한 다리 설계
# 서쪽에는 N개 , 동쪽에는 M개 (N<=M)
# 항상 서쪽의 N개의 다리 지으려고 할때 만들 수 있는 다리 경우의 수

# 1<N<=M<30
# M combination N

from itertools import combinations
import sys
input = sys.stdin.readline

T = int(input())
D = [[0]*30 for _ in range(30)]

#  N = 0 일때는 항상 1 , N = 1일때는 항상 M
for i in range(1,30):
    D[i][0] = 1
    D[i][1] = i
    D[i][i] = 1

# 점화식 계산
for j in range(2,30):
    for i in range(j+1,30):
        D[i][j] = D[i-1][j-1] + D[i-1][j]


for _ in range(T):
    N , M = map(int , input().split())
    print(D[M][N])
