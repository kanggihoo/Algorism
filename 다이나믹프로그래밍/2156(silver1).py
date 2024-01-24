
'''
포도주가 일렬로 놓여 있음.
D[i] i개의 포도주가 있을때 연속으로 3번 먹지 않고 최대먹을 수 있는 량
'''
import sys
input = sys.stdin.readline
N = int(input())
arr = [0]*10001
D = [0]*10001
for i in range(1,N+1):
    arr[i] = int(input())

D[1] = arr[1]
D[2] = arr[2]+arr[1]

for i in range(3,N+1):

    D[i] = max(arr[i]+arr[i-1]+D[i-3] , arr[i] +D[i-2] , D[i-1])
    
print(D[N])




