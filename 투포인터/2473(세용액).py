import sys
input = sys.stdin.readline
'''
3가지 용액 혼합 0에 가장 가깝도록
1개는 고정하고, 나머지 2개값에 대해 two pointer 적용
'''
N = int(input()) 
arr = list(map(int , input().split()))
arr.sort()

ans =4000000000+1
ans_index = None
for i in range(N-2):
    fix = arr[i]
    S,E = i+1,N-1
    while S<E:
        csum = arr[S] + arr[E] +fix
        if ans > abs(csum):
            ans = abs(csum)
            ans_index = (i,S,E)
        if csum > 0:
            E-=1
        elif csum < 0:
            S +=1
        else:
            break
    if ans ==0:
        break

print(" ".join([str(arr[i]) for i in ans_index]))
    
    
        
        
    