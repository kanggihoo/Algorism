arr = []
for _ in range(5):
    arr.append(int(input()))

# 평균
print(int(sum(arr)/len(arr)))

# 중앙값
arr.sort()
print(arr[5//2])