import sys
input = sys.stdin.readline
S = input().strip()
stack = []

def check(stack,compare):
    size = len(stack)
    for i in range(4):
        if stack[size-4+i] != compare[i]:
            return False
    return True

compare = "PPAP"

for s in S:
    stack.append(s)
    if len(stack) >= 4:
        if check(stack,compare):
            for _ in range(3):
                stack.pop()
if len(stack) == 1 and stack[-1] =="P":
    print("PPAP")
else:
    print("NP")