# N개의 집이 존재 하면 각 집을 R,G,B로 색칠하려고 할때 최소 비용으로 색칠
# 이때 이웃한 집의 색은 모두 달라야함.

# 입력받은 값들 저장
N = int(input())
Cost = [[0] for i in range(N+1)]
for i in range(1,N+1):
    RGB = list(map(int , input().split()))
    Cost[i]= RGB

# D는 2차원 배열로 D[i][k] : i는 각 단계, k는 R,G,B로 i번째에 k를 선택했을 때의 최소 비용 
# 최종적으로 D[N][0] , D[N][1], D[N][2] 즉 N번째에 R,G,B를 선택했을 때의 각각의 최소 비용을 구한뒤 3개 값들 중 가장 작은 비용을 최종출력한다.
D = [[0]*3 for _ in range(N+1)]
# D[1] = Cost[1] 로 초기화 
D[1] = Cost[1]

# D[]
for i in range(2,N+1):
    # i번째 R 선택 비용은 i-1의 G, B 선택했을 때의 최소 비용합 + 현재 비용
    D[i][0] = min(D[i-1][1] , D[i-1][2]) + Cost[i][0]
    
    D[i][1] = min(D[i-1][0] , D[i-1][2]) + Cost[i][1]
    D[i][2] = min(D[i-1][0] , D[i-1][1]) + Cost[i][2]
    
print(min(D[N]))

