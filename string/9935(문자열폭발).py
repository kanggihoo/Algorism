import sys
input = sys.stdin.readline


S = input().strip()
target = input().strip()
stack = []

def check(stack , target):
    size = len(stack)-1
    tsize = len(target)-1
    # if all([if i  for i in reversed(range(len(target)))]):
    #     pass
    flag = True
    for i in range(len(target)):
        if stack[size-tsize+i] != target[i]:
            flag = False
            break
    if flag:
        for _ in range(tsize+1):
            stack.pop()


for idx, s in enumerate(S):
    stack.append(s)
    if len(stack) >= len(target):
        check(stack , target)
if len(stack):
    print("".join(stack))
else:
    print("FRULA")
            