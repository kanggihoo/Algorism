'''
3x3배열 A , 인덱스는 1부터 시작
1초 지날때마다 배열에 연산 적용
R연산 : 모든 행에 대해 정렬,(행의개수 >= 열의개수인경우)
C연산: 열에 대해 정렬 (행 <열 개수)
정렬할때 수의 등장횟수가 커지도록 정렬, 여러개 이면 수가 커지는 순으로 
[수, 등장횟수]

100을 넘어가는 경우에는 처음 100개를 제외한 나머지는 버린다.
'''
from collections import Counter
def show(A):
    for i in range(len(A)):
        for j in range(len(A[0])):
            print(f"{A[i][j]:2}" , end="")
        print()
    print()
R ,C ,K = map(int , input().split())
A = []
for  _ in range(3):
    A.append(list(map(int , input().split())))
time =0
if R-1 < len(A) and C-1 < len(A[0]) and  A[R-1][C-1] == K:
    print(time)
else:
    while time <= 100:
        time +=1
        if len(A)>= len(A[0]): # R연산
            maxcol = 0
            new_a = []
            for i in range(len(A)):
                c = Counter([k for k in A[i] if k !=0])
                # 카운터 정렬 => 등장횟수, 수에 대해 오름차순
                c = list(sorted(c.items() , key = lambda x : (x[1],x[0])))
                tmp = []
                for j in c :
                    tmp.extend(j)
                if len(tmp) >=100:
                    tmp = tmp[:100]
                maxcol = max(maxcol , len(tmp))
                new_a.append(tmp)
            A = [[0]*maxcol for _ in range(len(A))]
            for idx , a in enumerate(new_a):
                for i in range(len(a)):
                    A[idx][i] = new_a[idx][i]
        else: # C연산
            maxrow = 0
            new_a = []
            for i in range(len(A[0])):
                cal = [A[j][i] for j in range(len(A)) if A[j][i] !=0]
                c = Counter(cal)
                c = list(sorted(c.items() , key = lambda x : (x[1],x[0])))
                tmp = []
                for j in c :
                    tmp.extend(j)
                if len(tmp) >=100:
                    tmp = tmp[:100]
                maxrow = max(maxrow , len(tmp))
                new_a.append(tmp)
            A = [[0]*len(A[0]) for _ in range(maxrow)]
            for idx , a in enumerate(new_a):
                for i in range(len(a)):
                    A[i][idx] = new_a[idx][i]
        
        if R-1 < len(A) and C-1 < len(A[0]) and  A[R-1][C-1] == K:
            break
        else:
            continue
    if time >= 101:
        print(-1)
    else:
        print(time)
                
                
                
        
 
        
        
        

 
# A[r-1][c-1] = k