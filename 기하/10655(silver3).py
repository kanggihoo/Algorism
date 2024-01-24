'''
마라톤1

마라톤 코스는 N개의 (3~100000) 체크 포인트 존재하며
1번 부터 순서대로 방문 후 N번 체크포인트에서 종료
주인공이 체크포인트 한개를 건너뛰면서 달릴 수 있을 때 최소거리
(이때 1번, N번 체크 포인트는 건너뛸 수 없다.)



'''



import sys
input = sys.stdin.readline
N = int(input())
checks = []

for _ in range(N):
    x,y = map(int , input().split())
    checks.append((x,y))
    
# 모든 체크 포인트 통과시 걸리는 거리 계산
total_D = 0
for i in range(N-1):
    total_D += abs(checks[i][0] - checks[i+1][0]) + abs(checks[i][1] - checks[i+1][1])

# 특정 체크 포인트 스큅 시 걸리는 거리 계산
min_D = total_D
for skip in range(1,N-1):
    tmp = total_D
    tmp -= (abs(checks[skip-1][0] - checks[skip][0]) + abs(checks[skip-1][1] - checks[skip][1]))
    tmp -= (abs(checks[skip][0] - checks[skip+1][0]) + abs(checks[skip][1] - checks[skip+1][1]))
    tmp += (abs(checks[skip-1][0] - checks[skip+1][0]) + abs(checks[skip-1][1] - checks[skip+1][1]))
    if tmp < min_D:
        min_D = tmp
print(min_D)


    