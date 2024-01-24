import sys 
input = sys.stdin.readline
N = int(input())
arr = []
for idx in range(N):
    age , name = input().split()
    arr.append((int(age),name,idx))
arr.sort(key=lambda x : (x[0],x[2]))

for i in arr:
    print(i[0],i[1] , sep=' ')

