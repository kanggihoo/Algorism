import sys
input = sys.stdin.readline
N = int(input())
arr = list(map(int , input().split()))


info = [[0,arr[0]] for _ in range(N)]
ans = [arr[0]]
idx = 0 

def search(s ,e , target):
    S,E = s, e
    
    while S<=E:
        mid = (S +E)//2
        
        if ans[mid] > target:
            E-=1
        elif ans[mid] < target:
            S+=1
        else: # ans[mid] = target
            return mid
    return S

for i in range(1,N):
    info[i][1] = arr[i]
    if arr[i] > ans[idx]:
        idx+=1
        ans.append(arr[i]) 
        info[i][0] = idx
    else:
        # 현재 값보다 큰 값중 가장 작은 인덱스 찾기
        p = search(0,idx , arr[i])
        ans[p] = arr[i]
        info[i][0] = p
    

new_arr = []
track = idx
for i in range(len(info)-1,-1,-1):
    if info[i][0] == track:
        new_arr.append(info[i][1])
        track -= 1
    if track == -1:
        break
    
print(idx+1)
print(*new_arr[::-1])