import sys
input = sys.stdin.readline

'''
예산 분배, 총액은 고정, 가능한 최대의 예산 배정.
1. 요청이 배정가능한 경우, 그대로 배정
2. 없는 경우, 특정 정수 상한액을 계산하여, 상한액 넘기면 모두 상한 액을 배정
    상한 이하는 그대로 배정
'''

N = int(input())
arr = list(map(int , input().split()))
M = int(input())
start,end = 0 , max(arr)

def cal(min):
    tsum=0
    for i in arr:
        if i <= mid:
            tsum += i
        else:
            tsum += mid
    return tsum
ans = 0
while start <= end :
    mid = (start+end)//2
    tsum = cal(mid)
    if tsum == M:
        ans = mid
        break
    elif tsum < M:
        ans = max(ans , mid)
        start = mid+1
    elif tsum > M:
        end = mid-1
print(ans)
