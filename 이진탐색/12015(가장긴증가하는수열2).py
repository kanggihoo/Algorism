import sys
input = sys.stdin.readline
N = int(input())
A = list(map(int , input().split()))

ANS = [0]*N
idx = 0
ANS[idx] = A[idx]

def serch(start , end , target):
    S ,E = start , end
    # target보다 커지는 지점이 어디인지
    while S<=E:
        mid = (S+E)//2
        if ANS[mid] > target: # 왼쪽으로 디오
            E = mid-1
        elif ANS[mid] < target : # L이동
            S = mid +1
        elif ANS[mid] == target:
            return
    ANS[S] = target
    return
     

for i in range(1,N):
    if A[i] > ANS[idx]: 
        idx +=1
        ANS[idx] = A[i]
    else:
        serch(0,idx , A[i])
    # print(ANS , idx)
print(idx+1)

        
        
        
    