'''
N = 3의 거듭제곱 꼴(3~3^7)

'''
N = int(input())
squre = [[0]*N for _ in range(N)]


def show_result(N , suqre):
    for i in range(N):
        for j in range(N):
            if squre[i][j]:
                print(" " , end ='')
            else:
                print("*" , end = '') 
        print()

def make_block(size , i_,j_ , suqre):
    for i in range(i_,i_+size):
        for j in range(j_,j_+size):
            squre[i][j] = 1
    

def recursion(N,start , end):
    if N <=3:
        squre[start+1][end+1] = 1
        return
    # 가운데 구멍 뚫기
    
    # 재귀호출
    for i in range(start,start+N,N//3):
        for j in range(end,end+N,N//3):
            if i == start+ N//3 and j == end + N//3:
                make_block(N//3 , i , j , squre)
            else:
                recursion(N//3 , i,j)
    

recursion(N,0,0)

show_result(N , squre)
