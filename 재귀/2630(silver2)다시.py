import sys
input = sys.stdin.readline

N = int(input())
arr = []
for _ in range(N):
    arr.append(list(map(int , input().split())))

def getSum(arr):
    total_sum=0
    for i in range(len(arr)):
        total_sum += sum(arr[i])
    return total_sum

def split(start , end):
    global White 
    global Blue
    # n1
    tmp = arr[0][0]
    for i in range(start , end+1):
        for j in range(start , end +1):
            arr[i][j] == 
            
        

White = 0
Blue = 0
# 처음에 모두 1이거나 0인경우는 확인 후 분할
if getSum(arr) == 1:
    Blue+= 1
    print(White)
    print(Blue)
elif getSum(arr) == 0:
    White+=1
    print(White)
    print(Blue)
else:
    split(len(arr))



    
    
    
    
    