# 동전 개수의 최솟값 구하기

## N개의 동전 종류를 이용하여 합이 K가 되도록 만드는 최소 동전 개수

# 첫번째 줄에 N,K가 주어지고
# 두번째 줄에 N개의 동전이 오름차순으로 주어짐

# import sys
# from collections import deque
# input = sys.stdin.readline

# # 초기화
# N, K =  map(int , input().split())
# Q = deque()
# for _ in range(N):
#     Q.append(int(input()))
# result = 0
# while(K > 0):
#     if Q[-1] > K:
#         Q.pop()
#         continue
#     coin = Q.pop()
#     result += (K//coin)
#     K%= coin
# print(result)
###########################################################################################
    
## 간결화

import sys
from collections import deque
input = sys.stdin.readline
result = 0
N, K =  map(int , input().split())
arr = []
for _ in range(N):
    my_input = int(input())
    if my_input <= K:
        arr.append(my_input)
while(K > 0):
    coin = arr.pop()
    result += (K//coin)
    K%= coin
print(result)
    
