# 왼쪽도시 -> 오른쪽 도시로 이동
# 1km 마다 1리터 사용
# 도시마다 주유소는 1개 있으며, 리터당 가격은 도시마다 다름

N = int(input())
distance = list(map(int , input().split()))
cost = list(map(int , input().split()))

min_cost = cost[0]
total_cost = 0
for i in range(N-1):
    
    if cost[i] < min_cost:
        min_cost = cost[i]
        total_cost += min_cost*distance[i]
    else:
        total_cost += min_cost*distance[i]
print(total_cost)
        