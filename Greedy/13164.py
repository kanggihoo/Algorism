'''
N명을 줄세우고 K개의 조로 나누기
이때 각 조에는 최소 한명 존재, 같은 조의 학생은 서로 인접
조마다 티셔츠 비용은 조에서 가장 큰 키와 작은 키의 차이만큼
최대한 비용 아끼는 K개 조의 최소 티셔츠 비용

'''
N , K = map(int , input().split())
S = list(map(int , input().split()))

# 인접한 학생간의 차이 구하기 
sub = [S[i]-S[i-1] for i in range(1,N)]
# print(sub)
# 차이가 큰 것을 정렬(오름차순)
sub.sort()
# k개의 조로 나누기 위해서는 k-1번 분리하면 됨
for _ in range(K-1):
    sub.pop()
print(sum(sub))