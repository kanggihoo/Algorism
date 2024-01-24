'''
수열 S가 어떤 수 S_k를 기준으로 조건 만족시 바이토닉 수열
S_k 좌측은 증가수열 , S_k 우측은 감소수열 만족

'''
N = int(input())
A = list(map(int , input().split()))
D_L = [1 for _ in range(N)]
D_R = [1 for _ in range(N)]
# 왼쪽=>오른쪽 증가수열 되도록 D_L 계산
for i in range(1,N):
    for k in range(i):
        if A[i] > A[k]:
            D_L[i] = max(D_L[i] , D_L[k]+1)


# 오른쪽=>왼쪽 증가수열 되도록 D_R 계산
# A_hat = list(reversed(A))
# for i in range(1,N):
#     for k in range(i):
#         if A_hat[i] > A_hat[k]:
#             D_R[i] = max(D_R[i] , D_R[k]+1)

# D_R = list(reversed(D_R))

for i in range(N-1,-1,-1):
    for k in range(i+1,N):
        if A[i] > A[k]:
            D_R[i] = max(D_R[i] , D_R[k]+1)
print(D_R)
result = max([i+j-1 for i,j in zip(D_R , D_L)])
print(result)
            