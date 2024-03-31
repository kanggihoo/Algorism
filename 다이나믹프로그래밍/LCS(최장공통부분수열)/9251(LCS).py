'''
D[i,j] = A문자열의 A[:i] 즉 i번째 길이의 부분분자열과 , B 문자열의 B[:j] 즉, j길이의 부분문자열 중 LCS로 나누기
D[i,j] = if A[i] == B[j]인경우 , A[i] != B[j] 인경우로 구분
1번의 경우 
D[i,j] = D[i-1,j-1]+1
2번의 경우
D[i,j] = max(D[i-1,j] , D[i,j-1])

'''
import sys
input = sys.stdin.readline
A = input().strip()
B = input().strip()

D = [[0]*(len(B)+1) for _ in range(len(A)+1)]




for i in range(1,len(A)+1):
    for j in range(1,len(B)+1):
        if A[i-1] == B[j-1]:
            D[i][j] = D[i-1][j-1]+1
        else:
            D[i][j] = max(D[i-1][j] , D[i][j-1])
print(D[len(A)][len(B)])
