'''
N개의 노드가 있고 1자로 연결되어 있다고
하면 총 N-1개의 연결이 있음
이때 K개의 그룹으로 분활하기 위해서는
K-1개의 연견을 끊으면 되는데
이때 각 연결의 비용값을 정렬 후 
K-1개 제거 후 나머지 연결의 총합을
구하면 된다.

'''
N = int(input())
K = int(input())
if K >= N:
    print(0)
else: 
    arr = list(map(int , input().split()))
    # 중복 제거
    arr = list(set(arr))
    # 오름차순 정렬
    arr.sort()
    diff = [] 
    # 이웃한 노드가 차이계산
    for i in range(1,len(arr)):
        diff.append(arr[i]-arr[i-1])
    # 차이를 다시 정렬
    diff.sort()
    for _ in range(K-1):
        diff.pop()
    print(sum(diff))

    