# 피보나치 수 동적 계획으로 작성(재귀X)
N = int(input())
D = [0]*(N+1)


D[1] =1
cnt = 0
for i in range(2,N+1):
    D[i]= D[i-1]+D[i-2]
    cnt +=1
    
print(D[N] , cnt-1)

