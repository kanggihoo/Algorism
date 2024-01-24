import sys
input = sys.stdin.readline
T = int(input())
S = []
for i in range(T):
    S.append(input().strip())

# isPalindrome
def recurions(string , start,end,count):
    if start >= end:
        return 1 ,count+1
    if string[start] == string[end]:
        return recurions(string , start+1 , end-1,count+1)
    else:
        return 0 , count+1

# recursion
def isPalindrome(string):
    return recurions(string , 0 , len(string)-1,0 )
    

# 모든 문자열 확인
for s in S:
    result = isPalindrome(s)
    if result[0]:
        print(1, result[1])
    else:
        print(0,result[1])
    
    
