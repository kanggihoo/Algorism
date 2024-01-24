# 모든 자리가 1로 이루어진 A,B 에서 A,B의 최대 공약수 구하기 

while(1):
    A,B = map(int , input().split())

    A , B = int("1"*A) , int("1"*B)
    while(A%B !=0):
        A , B = B, A%B
    print(B)


