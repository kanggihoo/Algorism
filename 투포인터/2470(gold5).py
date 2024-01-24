'''
산성 : 양수
알칼리 : 음수 

1. 용액의 혼합은 합으로 정의
2. 두 용액을 혼합하여 0에가장 가깝도록
3. 산성끼리 혼합 또는 알칼리 끼리 혼합가능
4. N개의 용액들의 특성값은 모두 다름

0에 가장 가까운 용액을 만들어 내는 두 용액의 특성값을 출력(오름차순)
여러개인 경우 아무거나 한개 출력

'''


'''
1)양수만 존재하는 경우에는 가장 작은 양수 2개
2)음수만 존재하는 경우에는 가장 큰 음수 2개 
3) 양 , 음 둘다 존재하면 정렬 후 가장 좌측과 우측에서 움직이면서 값 비교

'''
N = int(input())
arr = list(map(int , input().split()))
arr.sort()

# import random
# arr = random.sample(range(-100,-1), 30)
# arr.sort()

S = 0 
E = len(arr)-1

adjacent_zero_idx = (S,E)
adjacent_zero_value = abs(arr[S] + arr[E])

if arr[S] < 0 and arr[E] < 0:
    print(arr[E-1] , arr[E] ,sep=" ")
elif arr[S] >0 and arr[E] >0 :
    print(arr[S] , arr[S+1] , sep=" ")
else:
    while S < E:
        tmp = arr[S] + arr[E]
        if tmp == 0:
            adjacent_zero_idx = S , E
            break
        elif tmp >0:
            if tmp < adjacent_zero_value:
                adjacent_zero_value =tmp
                adjacent_zero_idx = (S,E)
            E -=1
        elif tmp <0:
            if abs(tmp) < adjacent_zero_value:
                adjacent_zero_value = abs(tmp)
                adjacent_zero_idx = (S ,E)
            S +=1

    print(arr[adjacent_zero_idx[0]] , arr[adjacent_zero_idx[1]])

