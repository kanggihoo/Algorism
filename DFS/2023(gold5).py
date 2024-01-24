# N자리수 중 N번 재귀호출 을 해서 모두 소수이면 그 숫자 출력
import math
N = int(input())

def isPrime(num):
    for i in range(2,int(math.sqrt(num))+1):
        if num % i==0:
            return False
        
    return True

# def DFS(number):
#     if len(str(number)) == N:
#         print(number)
#     else:
#         for i in range(1,9+1,2):
#             if isPrime(number*10+i):
#                 DFS(number*10+i)

# DFS(2)
# DFS(3)
# DFS(5)
# DFS(7)


result = []
def DFS(number,depth):
    # 종료 시점
    if depth ==N :
        result.append(number)
    else:
        for i in range(1,9+1,2):
            if isPrime(number*10+i):
                DFS(number*10+i,depth+1)
        

DFS(2,1)
DFS(3,1)
DFS(5,1)
DFS(7,1)

for i in result:
    print(i)
