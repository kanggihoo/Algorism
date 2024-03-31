import sys
input = sys.stdin.readline

'''
가로, 세로줄 , 3*3안의 정사각형 1~9한번씩
'''

MAP = []
for _ in range(9):
    MAP.append(list(map(int , input().split())))

def find_zero():
    p = []
    for i in range(9):
        for j in range(9):
            if MAP[i][j] == 0:
                p.append((i,j))
    return p
def find_candidate(y,x): # 현재 값이 0인 (y,x)에서 가능한 후보찾기
    candi = [i for i in range(1,9+1)]
    candi = check_col(y,x,candi) 
    candi = check_row(y,x,candi)
    candi = check_box(y,x,candi)
    return candi

def check_col(y,x , candi):
    compare = [MAP[y][i] for i in range(9)]
    return [i for i in candi if i not in compare]    
    
def check_row(y,x,candi):
    compare = [MAP[i][x] for i in range(9)]
    return [i for i in candi if i not in compare]    
    
def check_box(y,x,candi):
    y_start , x_start = 3*(y//3) , 3*(x//3)
    compare = [MAP[i][j] for i in range(y_start, y_start+3) for j in range(x_start , x_start+3)]
    return [i for i in candi if i not in compare]

def show():
    for i in range(9):
        for j in range(9):
            print(MAP[i][j] , end=" ")
        print()
            
def backtracking(idx):
    global flag 
    if idx == len(positions) and flag:
        # 출력
        show()
        flag = False
        return
    if not flag:
        return 
    y,x = positions[idx]
    candi = find_candidate(y,x)
    if len(candi):
        for can in candi:
            MAP[y][x] = can
            # show()
            backtracking(idx+1)
            MAP[y][x] = 0
    else:
        return
    
flag = True
positions = find_zero()
backtracking(0)
# y = 1 ; x =4
# print([(check_col(y,x,i),check_row(y,x,i),check_box(y,x ,i)) for i in range(1,9+1)])
# print(find_candidate(y,x) , MAP[y][x])


    