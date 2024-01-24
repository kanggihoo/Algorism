def quick_sort(arr , start , end):
    # 종료 조건
    if start > end :
        return
    pivot = end
    i = start -1    
    for j in range(start , end):
        if arr[j] <= arr[pivot]:
            i +=1
            arr[i] , arr[j] = arr[j] , arr[i]
    i+=1
    arr[i] , arr[pivot] = arr[pivot] , arr[i]
    pivot = i
    
    quick_sort(arr , start , pivot-1)
    quick_sort(arr , pivot+1 , end)


arr = [1,12,51,21,12,15,21,12] 
print(arr)
arr.sort()
quick_sort(arr,0,len(arr)-1)
print(arr)




            
        
    