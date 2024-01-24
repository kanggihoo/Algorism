


'''
1~N까지의 순열, 사전순으로 오름차순 정렬

입력으로 주어지는 순열의 다음에 오는 순열 출력
맨 마지막 순열인 경우 -1출력
'''
import sys

input = sys.stdin.readline
N = int(input())
arr = list(map(int , input().split()))
i,j = N-1 , N-1

# 
while i-1 >=0 and arr[i-1] > arr[i]:
    i-=1
# i가 이면 주어진 수열은 사전에서 맨 마지막 수열
if i==0:
    print(-1)
else:
    # i-1과 끝에서 부터 값을 비교한 뒤 swap
    while arr[i-1] > arr[j]:
        j-=1
    # swap을 완료하면 i~N-1 인덱스 값이 내림차순 정렬됨
    arr[i-1] , arr[j] = arr[j] , arr[i-1]
    
    L = arr[:i]
    # 오른쪽 부분만 오름차순 정렬 후 합치기
    R = sorted(arr[i:])
    next = L+R
    for i in next:
        print(i , end = " ")

    

        
    








