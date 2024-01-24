from queue import PriorityQueue

PQ = PriorityQueue() # 우선순위 큐 생성


## 큐에 값 집어 넣기 (put method 사용)
# 값을 집어넣을때 우선순위 값만을 넣을수도 있으며, 우선순위와 원하는 값을 같이 튜플로 넣을 수도 있다. 
PQ.put((3, 'Apple'))
PQ.put((1, 'Banana'))
PQ.put((2, 'Cherry'))

## get method 사용시 우선순위 값이 가장 작은 순으로 나오며, get 메서드 사용사 우선순위 큐의 사이즈가 줄어든다.
print("Q size : " , PQ.qsize())
print(PQ.get()[0])  # Banana
print("Q size : " , PQ.qsize())
print(PQ.get()[0])  # Cherry
print("Q size : " , PQ.qsize())
print("Q size : " , PQ.empty())
print(PQ.get()[0])  # Apple
print("Q size : " , PQ.qsize())

## qsize 메서드로 현재 우선순위 큐의 사이즈(저장된 원소 개수 반환)

## empty 메서드로 현재 큐가 비어 있으면 True, 원소가 있으면 False 반환 
