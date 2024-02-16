S = input().strip()
E = input().strip()
S = list(S)
E = list(E)
while len(S) < len(E):
    if E[-1] =="A":
        E.pop()
    elif E[-1] == "B":
        E.pop()
        E = E[::-1]
if S==E:
    print(1)
else:
    print(0)
        