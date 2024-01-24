# 길이가 N인 수열의 각 수를 적절히 묶어서 합을 최대로

# 1은 다른 수와 묶여져서 곱해지는 것보단 각각 더하는게 이득
# 음수들은 짝수개면 서로 곱해져서 양수 되게 하고, 마지막 음수는 그냥 더하기 이때 0이 있으면 마지막 음수랑 곱해져서 더하기
#

import sys
from queue import PriorityQueue

input = sys.stdin.readline
N = int(input())

Positive_numberQ = PriorityQueue() 
Negative_numberQ = PriorityQueue()
Zero_Q = PriorityQueue()
result = 0
# 1보다 큰 양수만 추가, 음수 추가, 0인경우 추가, 1인경우는 그냥 더하기
for _ in range(N):
    my_num = int(input())
    if my_num > 1:
        Positive_numberQ.put(my_num*-1) 
    elif my_num == 1:
        result +=1
    elif my_num ==0:
        Zero_Q.put(my_num)
    elif my_num < 0:
        Negative_numberQ.put(my_num)

# 1보다 큰 양수 끼리 더하기 
while(Positive_numberQ.qsize() > 1):
    n1 = Positive_numberQ.get()*-1
    n2 = Positive_numberQ.get()*-1
    result += (n1*n2)
if not Positive_numberQ.empty():
    result += (-1*Positive_numberQ.get())
    
# 음수끼리 더하기
while(Negative_numberQ.qsize() > 1):
    n1 = Negative_numberQ.get()
    n2 = Negative_numberQ.get()
    result +=(n1*n2)

# 음수가 홀수인경우
if not Negative_numberQ.empty():
    if not Zero_Q.empty():
        Negative_numberQ.get() # 마지막 남은 음수와 0이 곱해져서 합이 0이므로 그냥 버리기
    else:
        result += Negative_numberQ.get() # 0이 없는 경우는 그냥 혼자서 결과에 더해지기
print(result)


        
        

