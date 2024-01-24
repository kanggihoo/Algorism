
# 어떤 수와 그 수의 숫자 순서를 뒤집은 수가 일치하는 수를 '팰린드롬'
# 어떤 수 N이 주어졌을 떄 N보다 크거나 같고 소수이면서 팰린드롬인 수 중 가장 작은수
import math
N = int(input())

arr  = [ i if i > 1 else 0 for i in range(10000000)]

# 소수 찾기
for i in range(2,int(math.sqrt(len(arr)))+1):
    if arr[i] ==0:
        continue
    for j in range(i+i , len(arr) , i):
        arr[j] = 0

for i in range(N, len(arr)):
    if arr[i]:
        str_number = str(i)
        if str_number == str_number[::-1]:
            print(i)
            break
    