import sys
input = sys.stdin.readline
N = int(input())
num = list(map(int , input().split()))
orders = dict()
values = set()
MAX = 0
for idx , i in enumerate(num):
    orders[i] = idx
    values.add(i)
    MAX = max(MAX , i)
orders = dict(sorted(orders.items() , key= lambda x: x[0]))
score = {idx:0 for idx in range(N)}



for i , idx in orders.items():
    for j in range(i*2 , MAX+1, i):
        if j in values:
            score[idx] +=1
            score[orders[j]] -=1
print(score)
for i in score.values():
    print(i,end =" ")
        





