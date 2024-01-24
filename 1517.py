

import sys
input = sys.stdin.readline
Total = 0
def merge_sort(arr):
    global Total
    if len(arr) < 2:
        return arr
    
    mid = len(arr)//2
    arr1 = merge_sort(arr[:mid])
    arr2 = merge_sort(arr[mid:])
    
    # 합병
    merged = [0]*len(arr)
    i = j = 0
    k=0
    while  i < len(arr1) and j < len(arr2):
        if arr1[i] > arr2[j]:
            merged[k] = arr2[j]
            Total += abs(mid+j -k)
            j+=1
        else:
            merged[k] = arr1[i]
            i+=1
        k+=1
        
    while i < len(arr1) :
        merged[k] = arr1[i]
        i+=1
        k+=1
    while j < len(arr2) :
        merged[k] = arr2[j]
        j+=1
        k+=1

    return merged

arr = [1,1,2,1,1,2,2,1] 
arr = merge_sort(arr)
# print(arr)
print(Total)
        
    
        