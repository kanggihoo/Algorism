
import sys
input = sys.stdin.readline
N ,K = map(int , input().split())

def count_1(n):
    if n==0:
        return 0
    return n%2 + count_1(n//2)
cost = 0
while count_1(N) > K:
    N+=1
    cost+=1
print(cost)
# cost = 0
# while bin(N).count("1") > K:
#     N+=1
#     cost +=1
# print(cost)
    
    



