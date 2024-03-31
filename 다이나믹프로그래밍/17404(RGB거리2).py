import sys
input = sys.stdin.readline
'''
빨 : 0 , 초 :1 , 파 :2

'''
N = int(input())
cost= []
for _ in  range(N):
    cost.append(list(map(int , input().split())))
D = [[0]*3 for _ in range(1000+1)]
ans = 1e7
INF = 3000
for rgb in range(3):
    # 초기화
    D[0] = [INF if k !=rgb else cost[0][rgb] for k in range(3)]
    D[1] = [INF if k ==rgb else D[0][rgb]+cost[1][k] for k in range(3)]
    for i in range(2, N):
        D[i][0] = min(D[i-1][1], D[i-1][2])+cost[i][0]
        D[i][1] = min(D[i-1][0], D[i-1][2])+cost[i][1]
        D[i][2] = min(D[i-1][1], D[i-1][0])+cost[i][2]
    # rgb값에 대한 마지막 최소 값 계산
    if rgb == 0:
        ans = min(ans,D[N-1][1] ,D[N-1][2])
    elif rgb == 1:
        ans = min(ans,D[N-1][0] ,D[N-1][2])
    else :
        ans = min(ans,D[N-1][1] ,D[N-1][0])
print(ans)
    
        