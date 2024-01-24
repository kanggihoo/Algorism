# import sys
# input = sys.stdin.readline
# N = int(input())
# num_arr = []
# arr = list(map(int , input().split()))
# for i in range(N):
#     num_arr.append((arr[i],i))
# num_arr.sort(key = lambda x : x[0])

# D = [0]*(N)
# for i in range(1,N):
#     if num_arr[i-1][0]==num_arr[i][0]:
#         D[i] = D[i-1]
#     else:
#         D[i] = i-(i-D[i-1])+1
# # print(num_arr)
# # print(D)
# Result = [0]*(N)

# for i in range(N):
#     Result[num_arr[i][1]] = D[i]
# print(" ".join(map(str , Result)))


## 다른방법(dictionary 이용)
import sys
input = sys.stdin.readline
N = int(input())
arr = list(map(int , input().split()))
arr2 = sorted(list(set(arr)))
print(arr2)
dict = {arr2[i] :i for i in range(len(arr2))}
print(dict)
for i in arr:
    print(dict[i] , end=" ")