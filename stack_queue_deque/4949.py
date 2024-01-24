
import sys
input = sys.stdin.readline
while 1:
    S = input().strip()
    if S ==".":
        break

    stack = []
    for c in S:
        if c =="(" or c=="[":
            stack.append(c)
        elif c ==")" or c=="]":
            if not len(stack):
                stack.append(c)
                break
            if c==")" and stack[-1]=="(":
                stack.pop()
            elif c=="]" and stack[-1]=="[":
                stack.pop()
            else:
                break
    if len(stack):
        print("no")
    else: print("yes")
        
