N , K = map(int , input().split())
arr = list(map(int , input().split()))

start = 0
end = K-1
max_sum = sum(arr[:K])
total_sum = max_sum
while end < len(arr)-1:
    end +=1
    total_sum -= arr[start] 
    total_sum += arr[end]
    start += 1
    if total_sum > max_sum:
        max_sum = total_sum
print(max_sum)
    