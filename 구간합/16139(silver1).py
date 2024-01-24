'''
문자열 S에서 구간 [l,r] 사이에 특정 알파벳이 얼마나 나오는지에 
대한 질문을 q번 진행
S는 소문자로만 이루어짐. 
'''
import sys

input = sys.stdin.readline
S = input().strip()
q = int(input())
Q = []
for i in range(q):
    question = input().split()
    Q.append((question[0] , int(question[1]) , int(question[2])))

# find number of the appearence for each letter of the alphabet
alphabet_dict = {}

for i in S:
    alphabet_dict[i] = []

for alphabet in alphabet_dict.keys():
    count = 0
    for i in range(len(S)):
        if S[i] == alphabet:
            count +=1
        alphabet_dict[alphabet].append(count) 


# return for question
for q in Q:
    # when the alphabet exists in dictionary
    alphabet , start , end = q
    if alphabet_dict.get(alphabet):
        end_num = alphabet_dict[alphabet][end]
        start_num = alphabet_dict[alphabet][start]
        
        if S[start] == alphabet:
            print(end_num-start_num+1)
        else:
            print(end_num - start_num)
    else:
        print(0)
            


    