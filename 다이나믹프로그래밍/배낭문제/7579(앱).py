import sys
input = sys.stdin.readline


'''
메모리 부족시 , 활성화 된 앱 중 몇개 선택하여 삭제=>비활성화
 => 비활성화시 재실하는데 비용 있음 

현재 N개의 앱이 활성화 상태, 각각 m바이트 만큼 사용, 
각각 비활성화시 다시 실행하는데 드는 비용을 c
이때 새로운 B를 실행하여 M 의 추가 메모리가 필요한 상황
Ci를 최소화 하여 M을 확보하는 방법

'''
N , M = map(int ,input().split())
A = list(map(int , input().split()))
C = list(map(int , input().split()))

'''
D[i][j] => 최대 j비용을 고려하여 i번째 앱 까지 활성,비활성에 따른 바이트 수

'''
range_cost = sum(C)
D= [[0]*(range_cost+1) for i in range(N+1)]
ans = 100*100+1
for i in range(1, N+1):
    for j in range(range_cost+1):
        if j >= C[i-1]:
            D[i][j] = max(D[i-1][j-C[i-1]]+A[i-1],D[i-1][j])
        else:
            D[i][j] = D[i-1][j]
        if i == N:
            if D[i][j] >= M:
                ans = min(ans , j)
# for i in range(1,N+1):
#     for j in range(range_cost+1):
#         print(D[i][j] , end ="  ")
#     print()
print(ans)


