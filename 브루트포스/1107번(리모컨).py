'''
리모컨 일부 숫자 버튼 고장
0~9숫자, + , - 버튼 존재
+ 누르면 현재 채널 +1
- 누르면 현재 채널 -1
채널 0에서 -1 누르면 변화 없고, 채널은 무한대 존재

N 채널로 이동하려함. 고장난 버튼이 주어질때 N으로 이동하기 위한 최소 눌러야 하는 버튼수
현재 100번 채널에 있음
0~500,000 
고장난 버튼의 개수 M 0~10

'''
N = int(input())
M = int(input())
if M > 0:
    B = list(map(int, input().split()))
else:
    B = []
    
numbers = [i for i in range(10) if i not in B]
result = 1e10
def split(num):
    tmp = []
    while num:
        tmp.append(num % 10)
        num //= 10
    return tmp[::-1]
# result = 5e6
def dfs(num_str):
    if int(num_str) > 5000000:
        return 
    global result 
    result = min(result , len(num_str) + abs(int(num_str)-N))
    for i in numbers:
        if int(num_str) == 0 and i ==0:
            continue
        dfs(num_str+str(i))
N_split = split(N)

if all(True if i in numbers else False for i in N_split )or N==100:
    result = 0
else:
    for i in numbers:
        dfs(str(i))
print(result)
    

    
        
