# 일곱 난쟁이 키의 합이 100
# 아홉 낸장이 키가 주어질때 일곱 난쟁이 찾는 프로그램
arr = []
for _ in range(9):
    arr.append(int(input()))

total = sum(arr)


def find(total):
    for i in range(9):
        for j in range(9):
            if i==j:
                continue
            if total - (arr[i]+arr[j]) == 100:
                return arr[i] , arr[j]

a,b = find(total)

arr.remove(a)
arr.remove(b)
arr.sort()
for i in arr:
    print(i)
            
        
            

