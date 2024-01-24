# def merge(n1:list , n2:list)->list:
#     arr =[]
#     p1, p2 = (0,0)
#     while p1 < len(n1) and p2 < len(n2):
#         if n1[p1] > n2[p2]:
#             arr.append(n2[p2])
#             p2+=1
#         else:
#             arr.append(n1[p1])
#             p1+=1
#     if p1 == len(n1):
#         while p2 < len(n2):
#             arr.append(n2[p2])
#             p2 +=1
#     else:
#         while p1 < len(n1):
#             arr.append(n1[p1])
#             p1+=1
#     return arr
    
    
# def merge_sort(arr:list)->list:
#     if len(arr) <= 1:
#         return arr
#     mid = len(arr)//2
#     n1 = arr[:mid]
#     n2 = arr[mid:]
#     n1_ = merge_sort(n1)
#     n2_ = merge_sort(n2)
#     return merge(n1_, n2_)

# print(merge_sort([1,25,1,23,12,124,241]))
    
    
    