# 계단은 1개 또는 2계산씩
# 연속된 세개의 계단을 모두 밟으면 안됨
# 마지막 계단은 꼭 밟아야 함. 
# 밟은 계단의 최대값 구하기 


'''
1개 계단 오른 횟수 카운트 변수 => 1개 계단을 연속해서 2번 오른
경우에는 2번째 계단 오르고 변수 초기화

'''
# import sys
# input = sys.stdin.readline
# N = int(input())
# arr = [0]*(N+1)
# for i in range(1,N+1):
#     arr[i] = int(input())
    
# D = [0]*(N+1)

# if N >= 3:
#     D[1] = arr[1]
#     D[2] = sum(arr[1:2+1])
#     for i in range(3,N+1):
#         D[i] = max(D[i-2] + arr[i] , arr[i-1]+D[i-3]+arr[i])
#     print(D[N])
# else:
    
#     print(sum(arr))
# # print(arr)
# # print(D)
    

    


'''
한계단 또는 2계단, 연속 세개의 계단 밝기 안됨
마지막 계단은 밟아야 한다.


'''
import sys
input = sys.stdin.readline
N = int(input())
steps = [0 for i in range(300+1)]
for i in range(1,N+1):
    steps[i] = int(input())
D = [0 for i in range(300+1)]
D[1] = steps[1]
D[2] = steps[1]+steps[2]

for i in range(3,N+1):
    D[i] = max(D[i-2] ,  D[i-3] + steps[i-1]) + steps[i]
print(D[N])
    
    




