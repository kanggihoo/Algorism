# 부등호 k개 나열된 순열 A존재
# 부등호 앞뒤에 한자리 숫자넣어서(0~9) 모든 부등호 관계 만족 하도록 만들고 부등호 제거했을때 최대, 최소 되도록
# 숫자는 0~9까지 중에서 선택해야 하며 중복안됨

K = int(input())
EQ = list(input().split())
number = list(range(9+1))
MAX = "0"
MIN = "100000000000"

# def findNum(num , str): # 부동호 조건을 만족하는 숫자 찾기
#     next_num = None
#     if str =='>':
        
        
#     elif str =='<':
        
#     else:
#         print("오류!")
        
#     return next_num
        
    

def dfs(num,result):
    if len(result) == K+1: # result 배열에 K+1개 원소가 저장되면 중단
        final_num_str = "".join(map(str,result))
        final_num = int(final_num_str)
        
        global MAX , MIN
        if final_num > int(MAX):
            MAX = final_num_str
        if final_num < int(MIN):
            MIN = final_num_str
        
        
        return
    idx = len(result)-1
    sign = EQ[idx]
    
    next_num = None
    if sign =='>':
        for i in number:
            if i not in result and result[idx] > i:
                result.append(i)
                dfs(i , result)
                result.pop()
        return    
    elif sign =='<':
        for i in number:
            if i not in result and result[idx] < i:
                result.append(i)
                dfs(i , result)
                result.pop()
        return
        

for num in number:
    result = []
    result.append(num)
    dfs(num, result)

print(MAX)
print(MIN)

