# 연속합 중 가장 최대가 되는 경우 구하기
N = int(input())
arr = list(map(int , input().split()))
D = [0]*(N)
D[0] = arr[0]

# D[i] = i번째 위치에서의 최대값
# arr[i] < D[i-1]+arr[i] 이면 계속 더하고
# arr[i] > D[i-1]+arr[i] 이면 연속합을 중단하고 다시 arr[i] 부터 더해나간다. 
for i in range(1,N):
    D[i] = max(arr[i] , D[i-1]+arr[i])
print(max(D))