import sys
input = sys.stdin.readline
N ,L,R,X = map(int , input().split())
A = list(map(int,input().split()))

def count_1(N):
    if N ==0:
        return 0
    return N%2 + count_1(N//2)

ans = 0
for i in range(1<<N):
    cnt = 0
    tsum =0
    if count_1(i) < 2:
        continue
    max_l = 0
    min_l = 1e6
    for j in range(N):
        if i & (1<<j):
            cnt +=1
            tsum+=A[j]
            max_l = max(A[j] , max_l)
            min_l = min(A[j] , min_l)
        if tsum > R:
            break
    if L<=tsum<=R and max_l-min_l >=X:
        ans+=1
print(ans)
        
            
            
'''
N개 문제, 난이도 A , 2문제 이상
문제 난이도 합은 L 이상 R이하
가장 어려운 문제 , 가장 쉬운문제 차이 X이상
'''



    
    



