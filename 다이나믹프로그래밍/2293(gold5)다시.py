'''
n가지 종류의 동전을 이용하여 합이 k원이 되도록 하는 모든 경우의 수 
(각각의 동전은 몇개라도 가능 , 사용한 순서 다른 경우도 포함)

'''
import sys
input = sys.stdin.readline
N , K = map(int , input().split())
values = []
D = [0]*(10001)
for _ in range(N):
    # 주어지는 가치를 정렬해야 하나?
    values.append(int(input()))
    

#동전 1개 가치가 K를 넘어가는 경우는 제거 해야할듯
values = list(filter(lambda x : True if x < K else False , values))

# 초기화 
for i in values:
    D[i] = 1
print(D[:K+1])
for i in range(1,K+1):
    acc_sum = 0
    for value in values:
        if i-value >0:
            acc_sum += D[i-value]
        if i == value:
            acc_sum += 1
    D[i] = acc_sum
print(D[:K+1])

        
            
    


    