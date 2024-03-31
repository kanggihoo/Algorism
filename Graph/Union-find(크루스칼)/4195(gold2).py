'''
친구 관계가 주어졌을 때 , 두 사람의 친구 네트워크에 몇 명이 있는지 
친구 네트워크 : 친구 관계만으로 이동할 수 있는 사이
F : 친구 관계의수 < 100,000
친구 관계는 두 사용자의 아이디로 이루어짐(문자열)
친구 관계가 생길 때마다 해당 그룹의 맴버가 몇명인지 출력
'''
import sys
input = sys.stdin.readline
def find(x):
    if parents[x] == x:
        return x
    parents[x] = find(parents[x])
    return parents[x]

def union(x1,x2):
    p1 = find(x1)
    p2 = find(x2)
    if p1 > p2:
        parents[p1] = p2
        size[p2] += size[p1]
    elif p1 < p2:
        parents[p2] = p1
        size[p1] += size[p2]
 
    
T = int(input())
for _ in range(T):
    F = int(input())
    parents = {}
    size = {}
    for f in range(F):
        f1 , f2 = input().split()
        if not parents.get(f1):
            parents[f1] = f1
            size[f1] = 1
        if not parents.get(f2):
            parents[f2] = f2
            size[f2] = 1
        
        if find(f1) != find(f2):
            union(f1 , f2)
        print(size[find(f1)])    
# print(parents)      
    

    
        
    