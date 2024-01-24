import random
from collections import deque


def counting_sort(arr):
    MAX = max(arr)
    C = [0]*(MAX+1)
    for i in range(len(arr)):
        C[arr[i]] += 1
    for i in range(len(C)-1):
        C[i+1] += C[i]
    print(C)
    B = [0]*(len(arr)+1)
    for i in reversed(range(len(arr))):
        B[C[arr[i]]] = arr[i]
        C[arr[i]] -= 1
    return B


def counting_sort2(arr):
    MAX = max(arr)
    C = [deque() for _ in range(MAX+1)]
    B = [0]*(len(arr)+1)

    for i in range(len(arr)):
        C[arr[i]].append(arr[i])

    for c in C:
        while c:
            num = c.popleft()
            B.append(num)
    return B


arr = [random.randint(10, 30) for _ in range(10)]
print(arr)
B = counting_sort(arr)
print(B)
