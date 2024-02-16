N = int(input())
A = list(map(int , input().split()))
sub  = [[i] for i in A]
D = [1 for _ in range(N)]

for i in range(1,N):
    sub_list = [D[k] for k in range(i) if A[i] > A[k]]
    if len(sub_list):
        idx = D.index(max(sub_list))
        max_len = max(sub_list)
        D[i] = D[idx]+1
        sub[i].extend([sub[k] for k in range(i) if D[k] == max_len and sub[k][0] < sub[i][0]][0])

        

print(max(D))
max_len = sorted(sub[D.index(max(D))]) 
print(" ".join(map(str , max_len)))
