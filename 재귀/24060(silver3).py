import sys
# sys.setrecursionlimit(10000)
input = sys.stdin.readline
N , K = map(int , input().split())
arr = list(map(int , input().split()))
cnt = 0
cnt_arr = [0]
def merge_sort(A:list,start:int , end:int): # sorting by ascending order 
    if start < end:
        mid =(start+end)//2
        merge_sort(A,start , mid) 
        merge_sort(A,mid+1 , end)
        merge(A , start , mid , end)
        
    
    
'''
p: start point of first list
q: end point of first list
r: end point of last list
'''
def merge(A:list , p:int , q:int , r:int)->list:
    #A[p~q] , A[q+1~r] 은 이미 오름차순 정렬 되어 있음
    #p1 = A[p~q] , p2 = A[q+1~r]
    p1_S , p1_E , p2_S , p2_E = p , q , q+1 ,r
    tmp = []
    # 둘 중 먼저 채워지면 종료
    while p1_S<=p1_E and p2_S <= p2_E:
        if A[p1_S] < A[p2_S]:
            tmp.append(A[p1_S])
            p1_S +=1
        else:
            tmp.append(A[p2_S])
            p2_S +=1
    # p1이 먼저 채워졌다면 p2의 모든 값을 채운다. (p2는 이미 오름차순 정렬되어 있으므로)
    if p1_S > p1_E:
        while p2_S <= p2_E:
            tmp.append(A[p2_S])
            p2_S+=1
    # p2가 먼저 채워졌다면 p1의 모든 값을 채운다. (p1는 이미 오름차순 정렬되어 있으므로)
    else:
        while p1_S <= p1_E:
            tmp.append(A[p1_S])
            p1_S+=1
    # tmp 배열의 모든 값을 A배열에 업데이트 
    global cnt
    global cnt_arr
    for i in range(p,r+1):
        A[i] = tmp[i-p]
        cnt_arr.append(tmp[i-p])
        cnt +=1    
    # for i in range(len(tmp)):
    #     A[i+p] = tmp[i]

merge_sort(arr , 0 , N-1)
if cnt < K:
    print(-1)
else:
    print(cnt_arr[K])

