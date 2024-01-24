# RGB 문제 1463과 유사한 문제
# 
import sys
input = sys.stdin.readline
N = int(input())
Trianlge = []
for _ in range(N):
    Trianlge.append(list(map(int , input().split())))

# D는 N*N 2차원 배열
D = [[0]*N for _ in range(N)]
D[0] = Trianlge[0]

for i in range(1,N): # 1~N-1 행
    
    for j in range(i+1): # 0~i-1열 
        if j ==0:
            D[i][j] = D[i-1][j]+Trianlge[i][j]
        elif j == i:
            D[i][j] = D[i-1][j-1]+Trianlge[i][j]
        else:
            D[i][j] = max(D[i-1][j-1] , D[i-1][j]) + Trianlge[i][j]
print(max(D[N-1]))

