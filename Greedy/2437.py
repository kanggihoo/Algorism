
'''
무게추의 개수 N이 주어지고 N개의 무게추의
무게가 주어질때 
만들수 없는 무게의 최솟값 출력

참고 : https://aerocode.net/392#%EC%B6%94%EA%B0%80-%ED%85%8C%EC%8A%A4%ED%8A%B8%EC%BC%80%EC%9D%B4%EC%8A%A4
'''

N = int(input())
W = list(map(int , input().split()))
W.sort()
value_range = [0,0] # min_max 
result = 0
for w in W:
    if value_range[1]+1 < w: # 
        result = value_range[1]+1
        break
    else:
        value_range[1] += w
# 주어진 추로 만들 수 있는최대 범위까지 모두 만들 수 경우
# 즉 더 큰 무게는 측정 불가
if sum(W) == value_range[1]:
    result = value_range[1]+1
   
print(result)
        

        