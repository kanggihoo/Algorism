'''
0과 1로 이루어진 숫자
1. 0으로 시작 하지 않음
2. 1이 두번 역속 나타나지 않음
N이 주어졌을 때 N자리 이친수의 개수 구하라

D[i][j]에서 i: 이친수 자릿수 , j: 끝자리 숫자 0또는 1
'''
N = int(input())
D = [[0]*2 for i in range(90+1)]
D[1][0] = 0
D[1][1] = 1

for i in range(2,N+1):
    D[i][0] = D[i-1][0] + D[i-1][1]
    D[i][1] = D[i-1][0]
print(D[N][0]+D[N][1])
