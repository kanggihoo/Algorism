import sys
input = sys.stdin.readline
N = int(input())
A = list(map(int , input().split()))
min_value = 2*1e10
L ,R = 0 , len(A)-1
while L < R:
    
    tsum = A[L]+A[R]
    if abs(tsum) < min_value:
        min_value = abs(tsum)
        min_idx = (L,R)
    if tsum > 0: # R이동
        R-=1
    elif tsum < 0: # L이동
        L +=1
    else:
        min_idx = (L,R)
        break

print(A[min_idx[0]] , A[min_idx[1]])

        
        
    