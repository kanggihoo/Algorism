# dictcionary 로 풀이 가능
N = int(input())
N_arr = list(map(int , input().split()))
N_arr_dict = {i:True for i in N_arr}
M = int(input())
M_arr = list(map(int , input().split()))


# dictcionary 로 풀이 가능
# for num in M_arr:
#     if N_arr_dict.get(num):
#         print(1)
#     else:
#         print(0)
        
# 이분탐색으로 해결(재귀 이용)
# N_arr.sort() 

# def BinarySearch(start , end , num):
#     # 종료 조건
#     if start > end :
#         return False
#     mid = int((start+end)/2)
#     if N_arr[mid] == num:
#         return True 
#     if N_arr[mid] > num:
#         return BinarySearch(start , mid-1 , num)
#     elif N_arr[mid] < num:
#         return BinarySearch(mid+1,end,num)


# for i in M_arr:
#     if BinarySearch(0,len(N_arr)-1 , i):
#         print(1)
#     else:
#         print(0)


# 이분탐색 while 문으로
# N_arr.sort()

# for i in M_arr:
#     start = 0
#     end = len(N_arr)-1
#     find = False
#     while start <= end:
#         mid = int((start+end)/2)
#         if N_arr[mid] == i:
#             find = True
#             break
#         if N_arr[mid] > i:
#             end = mid -1
#         elif N_arr[mid] < i:
#             start = mid+1
#     if find:
#         print(1)
#     else:
#         print(0)

N_arr.sort()
for i in M_arr:
    start = 0
    end = N-1
    is_find = False
    while start <=end:
        mid = (start+end)//2
        if N_arr[mid] == i:
            is_find = True
            break
        if N_arr[mid] < i:
            start = mid+1
        else:
            end = mid -1
    if is_find:
        print(1)
    else:
        print(0)
            


