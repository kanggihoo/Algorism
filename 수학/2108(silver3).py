# 1. 산술평균
# 2. 중앙값
# 3. 최빈값
# 4. 범위 (최대-c치소)

# N은 홀수
import sys
import math
from collections import Counter
input = sys.stdin.readline
N= int(input())
arr = []
for _ in range(N):
    arr.append(int(input()))

arr.sort()
# 산술평균 구하기
print(int(round(sum(arr)/len(arr),0)))
# 중앙값 구하기 
print(arr[N//2])
# 최빈값 구하기
C = Counter(arr)
count = C.most_common()
max_count = count[0][1]
count_filter = list(filter(lambda x : x[1] if x[1]==max_count else False  ,count))
# print(count_filter)
if len(count_filter) > 1:
    count_filter.sort(key=lambda x : x[1])
    # print(count_filter)
    print(count_filter[1][0])
else:
    print(count_filter[0][0])

# 범위구하기
print(max(arr)-min(arr))
        
    

