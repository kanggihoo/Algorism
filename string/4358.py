import sys
input= sys.stdin.readline
from collections import defaultdict
trees = defaultdict(int)
total = 0
while 1:
    S = input().strip()
    if S=="":
        break
    trees[S] +=1
    total +=1
for k , v in sorted(trees.items() , key=lambda x : x):
    value = round((v/total)*100 , 4)
    print(f"{k} {value:.4f}")
