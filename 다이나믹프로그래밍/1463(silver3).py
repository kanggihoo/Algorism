# 정수 X에 사용할 수 있는 연산은 다음과 같이 세 가지 이다.

# X가 3으로 나누어 떨어지면, 3으로 나눈다.
# X가 2로 나누어 떨어지면, 2로 나눈다.
# 1을 뺀다.

# 세개를 적절히 사용해서 1을 만들려고 할때 연산횟수가 최소가 되도록


result = None
N = int(input())
D = [0 for i in range(N+1)]


for i in range(2,N+1):
    # 3또는 2로 나누어 떨어지는 경우 

    if i % 3 ==0 and i %2 ==0: 
        D[i] = min(D[i//3]+1 , D[i//2]+1 , D[i-1]+1)    
    elif i % 3==0:
        D[i] = min(D[i//3]+1 , D[i-1]+1)
    elif i % 2==0:
        D[i] = min(D[i//2]+1,D[i-1] +1)
    else:
        D[i] = D[i-1]+1
print(D[N])


    

