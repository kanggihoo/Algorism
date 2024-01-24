import sys 
input = sys.stdin.readline
N = int(input())
arr = []
for _ in range(N):
    n1 , n2 = map(int , input().split())
    arr.append((n1,n2))
arr.sort(key= lambda x : (x[1],x[0]) )

for x,y in arr:
    print(x,y,sep=" ")