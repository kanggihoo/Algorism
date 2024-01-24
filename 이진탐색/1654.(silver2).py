import sys
input = sys.stdin.readline

K , N = map(int , input().split())
length = []
for _ in range(K):
    length.append(int(input()))

'''
start가 0이 되고 계속 반복문이 돌다가 mid=0이되면
getnum함수의 인자로 0이 들어가게 되어 while 문에서 무한반복돔.
'''

start = 1
end = sum(length)

def getnum(arr,N):
    total_num = 0
    for i in arr:
        while i >= N:
            i -= N
            total_num +=1
    return total_num

while start <= end:
    mid = (start+end)//2
    num = getnum(length , mid)
    if num < N:
        end = mid-1
    elif num >= N:
        start = mid +1
print(end)
    
    
    