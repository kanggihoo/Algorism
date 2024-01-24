import sys 
input = sys.stdin.readline
N = int(input())
arr = []
for _ in range(N):
    arr.append(input().strip())
arr_remove_duplicate = list(set(arr))
arr_remove_duplicate.sort(key= lambda x: (len(x),x)  )


for i in arr_remove_duplicate:
    print(i)

