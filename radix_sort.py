from collections import deque
import sys

input = sys.stdin.readline


def radix_sort(arr):
    max_value = max(arr)
    cur_ten = 1
    Q = deque(arr)
    buckets = [deque() for _ in range(10)]

    while max_value >= cur_ten:
        while Q:
            num = Q.popleft()
            num_digit = (num // cur_ten) % 10
            buckets[num_digit].append(num)

        for bucket in buckets:
            while bucket:
                Q.append(bucket.popleft())

        cur_ten *= 10
    return list(Q)


N = int(input())
arr = [0]*N
for i in range(len(arr)):
    arr[i] = int(input())

result = radix_sort(arr)
for i in result:
    print(i)
