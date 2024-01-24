# k층 n호에는 몇명 거주하는지 출력
# 아파트는 0 층 부터 각층에는 1호부터 존재 , 0 층의 i호에는 i명 거주
import sys
input = sys.stdin.readline
T = int(input())

for _ in range(T):
    K = int(input())
    N = int(input())

    # 리스트 초기화
    D = [[0]*(N+1) for _ in range(K+1)]
    # 0층의 i호는 i명 거주
    for i in range(1,N+1):
        D[0][i] = i
        
    for i in range(1,K+1):
        for j in range(1,N+1):
            D[i][j] = sum(D[i-1][x] for x in range(1,j+1))
    print(D[K][N])

    
        
    