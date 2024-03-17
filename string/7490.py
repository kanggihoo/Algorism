import sys
input = sys.stdin.readline

# eval() 안쓰고 
def dfs(S , result , step, N , results,pre_num , pre_op):
    if step == N:
        if pre_op == "+":
            result+= int(pre_num)
        elif pre_op == "-":
            result-= int(pre_num)
        if result == 0:
            results.append(S)
        return 
    for op in ["+","-" ," "]:
        num = step+1
        if op =="+":
            # 이전까지 
            if pre_op =="+":
                dfs(S+f"+{num}" , result+int(pre_num) , step+1 , N , results,str(num) , "+")
            elif pre_op =="-":
                dfs(S+f"+{num}" , result-int(pre_num) , step+1 , N , results,str(num), "+")
            else: # None인 경우
                dfs(S+f"+{num}" , int(pre_num) , step+1 , N , results,str(num) , "+")
        elif op == "-":
            if pre_op =="+":
                dfs(S+f"-{num}" , result+int(pre_num) , step+1 , N , results,str(num) , "-")
            elif pre_op =="-":
                dfs(S+f"-{num}" , result-int(pre_num) , step+1 , N , results,str(num), "-")
            else: # None인 경우
                dfs(S+f"-{num}" , int(pre_num) , step+1 , N , results,str(num) , "-")
        elif op ==" ":
            dfs(S+f" {num}" , result, step+1 , N , results,pre_num+str(num) , pre_op)
# eval 쓰고
def dfs2(S , step , results):
    if step == N:
        ans = eval(S.replace(" " ,""))
        if ans == 0:
            results.append(S)
        return
    for op in [" " ,"+","-"]:
        dfs2(S+op+str(step+1) , step+1 , results)

T = int(input())
for _ in range(T):
    N = int(input())
    answer = []
    # dfs("1" , 1,1,N,answer,"1" , None)
    dfs2("1" , 1,answer)
    answer.sort()
    for i in answer:
        print(i)
    print()
