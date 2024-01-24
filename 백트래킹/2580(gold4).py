'스도쿠 문제'
# 스도쿠 
board = []
for _ in range(9):
    nums = list(map(int, input().split()))
    board.append(nums)

def is_valid(num , row , col):
    return not (in_row(num , row) or in_col(num , col) or in_box(num , row , col))

def in_row(num , row):
    return num in board[row]

def in_col(num , col):
    return num in (board[i][col] for i in range(9))

def in_box(num , row , col):
    S_row = row//3 *3
    S_col = col//3*3
    for i in range(S_row , S_row+3):
        for j in range(S_col , S_col+3):
            if board[i][j] == num:
                return True
    return False

def find_empty_position():
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return i,j
    return None

def find_solution():
    empty_pose = find_empty_position()
    if not empty_pose: # 빈칸이 없으면 스도쿠 종료
        return True
    row , col = empty_pose
    for num in range(1,9+1):
        if is_valid(num , row , col):
            board[row][col] = num
            if find_solution():
                return True
            board[row][col] = 0
    return False

find_solution()
def show_reulst(board):
    for i in range(9):
        for j in range(9):
            print(board[i][j] , end=" ")
        print("")
show_reulst(board)




