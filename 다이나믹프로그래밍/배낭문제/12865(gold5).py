'''
N개의 물건은 무게 W와 가치 V를 가짐
최대 K만큼 무게를 넣어서 물건들의 가치가 최대가 되도록 하기



1) 가방의 무게가 가득 찬 경우

2) 가방의 무게가 아직 다 차지 않은 경우
 2-1 : 해당 번째 가방을 넣는다.
 2-2 : 해당 번째 가방을 넣지 않는다. 
 https://codingmovie.tistory.com/48
 
'''
import sys
input = sys.stdin.readline

N , K = map(int , input().split())
W = [0]*(N+1)
V = [0]*(N+1)
# add your's ipnut to the list W,V 
for i in range(1,N+1):
    w1 , v1 = map(int , input().split())
    W[i] = w1
    V[i] = v1 

# create D 
D = [[0]*(K+1) for _ in range(N+1)]

for i in range(1,N+1): # 1~N번째 
    w = W[i]   # i 번째 무게
    v = V[i]   # i 번째 가치
    for j in range(1,K+1): # 최대 허용무게 1~K
        
        if j < w:
            D[i][j] = D[i-1][j] # when current weight over max_weight (i)st max value == (i-1)st max value
        else:
            D[i][j] = max(D[i-1][j-w]+v , D[i-1][j])
print(D)
print(D[N][K])
            
    
    
   
## TOP DOWN 방식
def topdown(n,k):
    weight = A[n-1][0]
    v = A[n-1][1]
    if k < 0 :
        return 0
    if n ==0:
        return 0
    if k < weight :
        return D[n-1][k]
    else:
        D[n][k] = max(topdown(n-1, k-weight)+v , topdown(n-1 , k))        
        return D[n][k]
topdown(N,K)
print(D)



