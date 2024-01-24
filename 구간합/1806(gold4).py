'''
N개의 수에서 연속된 수들의 부분합 중에 그 합이 S이 이상이면서 가장 짧은 길이구하기
만일 그러한 합을 만드는 것이 불가능하면 0을 출력
'''

N , S = map(int, input().split())
arr = list(map(int , input().split()))

start , end = (0,0)
min_L = N
acc_s = arr[0]
total_sum = sum(arr)
if total_sum < S:
    print(0)
else:
    while end < N-1:
        # print(start , end  , acc_s)
        if acc_s < S:
            end +=1 
            acc_s += arr[end]
        elif acc_s >= S:
            min_L = min(min_L , end - start+1)
            if min_L == 1:
                break
            acc_s -= arr[start]
            start +=1
    # 이제 start만 앞으로 전진하면서 S보다 커지는 경우 있는지 확인
    # 없으면 바로 종료 
    while start < N:
        # print(start , end  , acc_s)
        if acc_s >= S:
            min_L = min(min_L , end - start+1)
            acc_s -= arr[start]
            start +=1
        else:
            break
    print(min_L)
            
