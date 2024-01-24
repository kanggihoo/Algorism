# N명(짝수) , N/2명인 A,B팀으로 분리
from itertools import combinations
import sys
input = sys.stdin.readline
N = int(input())
S = []

for _ in range(N):
    S.append(list(map(int , input().split())))

def minValue(arr):
    total_sum = 0
    for i in arr:
        for j in arr:
            if i >=j :
                continue
            total_sum += (S[i][j]+S[j][i])
    return total_sum

Result = 1e7

def dfs(i,A):
    if len(A) == int(N/2):
        # 모든 쌍 합 구하기
        global Result
        B = [i for i in range(N) if i not in A ]
        
        total_A = minValue(A)
        total_B = minValue(B)
        # print(A,B)
        Result = min(Result , abs(total_A-total_B))
        
    for j in range(i+1,N):
        A.append(j)
        dfs(j,A)
        A.pop()
            
for i in range(int(N/2)):
    A = []
    A.append(i)
    dfs(i,A)



print(Result)

    
