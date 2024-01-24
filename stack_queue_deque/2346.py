from collections import deque

N = int(input())
arr = list(map(int , input().split()))

Q = deque([i for i in range(1,N+1)])

# while len(Q) > 1:
#     # 터진 풍선 꺼내기
#     num = Q.popleft()
#     print(num , end = " ")
#     # 회전 방향, 얼마나 회전하는지
#     rotate = arr[num-1]
#     if rotate > 0:
#         for _ in range(rotate-1):
#             n1 = Q.popleft()
#             Q.append(n1)
#     else:
#         for _ in range(abs(rotate)):
#             n1 = Q.pop()
#             Q.appendleft(n1)
# print(Q[0])


while Q :
    # 터진 풍선 꺼내기
    num = Q.popleft()
    print(num , end = " ")
    # 회전 방향, 얼마나 회전하는지
    rotate = arr[num-1]
    if rotate >0:
        Q.rotate(-rotate+1)
        
    else:
        Q.rotate(-rotate)
