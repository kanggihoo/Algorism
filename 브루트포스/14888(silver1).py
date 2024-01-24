'''
N개로 이루어진 수열 , 수열 사이 끼워넣을 N-1개 연산자(+,-,x,/)
(주어진 수열의 순서 임의 변경x)
연산자 우선 순위 무시하고 앞에서 부터 진행
나머지 연산자는 나눈 몫이 결과이고
음수를 양수로 나눌 때는 , 양수로 변경후 몫을 구한뒤 음수로 변경

'''

## 모든 연산자의 가능한 조합을 구한 뒤 마지막에 계산
N = int(input())
arr = list(map(int , input().split()))
operators = list(map(int , input().split())) # 순서대로 + , - , x, %개수
maxV , minV = -1e9 , 1e9
def dfs(results, opertators):
    if len(results) == N-1:
        global maxV 
        global minV
        # 계산
        answer = arr[0]
        for i in range(N-1):
            operator = results[i]
            if operator == 0: # 더하기
                answer = answer+ arr[i+1]
            elif operator == 1: # 빼기
                answer = answer - arr[i+1]
            elif operator == 2: # 곱하기
                answer = answer * arr[i+1]
            else:        
                if answer <0 :
                    answer = -(-answer // arr[i+1])
                else:
                    answer = answer // arr[i+1]
        if maxV < answer:
            maxV = answer
        if minV > answer:
            minV = answer
                    
    
    for idx , operator in enumerate(opertators):
        if operator ==0:
            continue
        results.append(idx)
        opertators[idx] -= 1
        dfs(results , opertators)
        results.pop()
        opertators[idx] += 1
        
    
# 처음 연산자 구하기
L = []
for idx , operator in enumerate(operators):    
    if operator == 0:
        continue
    operators[idx] -=1
    L.append(idx)
    dfs(L , operators)
    L.pop()
    operators[idx] +=1
    
print(int(maxV))
print(int(minV))
    
#####################################################################################################################
'''
더 간단한 방법 계산을 해나가면서 진행 하는 경우(dfs 입력으로 모든 연산자의 개수를 집어넣어줌) , 
dfs의 입력으로 수열의 첫번째 값 , step , 누적합 , 각 연산자 갯수(+,-,*,%)를 입력으로 간단하게 

'''
