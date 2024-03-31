import sys
input = sys.stdin.readline

A = input().strip()
B = input().strip()
len_A = len(A)
len_B = len(B)
D= [[""]*(len_B+1) for _ in range(len_A+1)]

for i in range(1,len_A+1):
    for j in range(1,len_B+1):
        if A[i-1] == B[j-1]:
            D[i][j] = D[i-1][j-1]+A[i-1]
        else:
            D[i][j] = D[i-1][j] if len(D[i-1][j]) > len(D[i][j-1]) else D[i][j-1]
ans = D[len_A][len_B]
if len(ans):
    print(len(ans))
    print(ans)
else:
    print(0)

# for i in range(1,len(A)+1):
#     for j in range(1,len(B)+1):
#         print(f"{D[i][j]:4}" , end =" ")
#     print()
    