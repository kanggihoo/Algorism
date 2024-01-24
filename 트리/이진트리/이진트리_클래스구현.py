# 노드 클래스 정의
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
# 이진 탐색 트리 클래스
class BST:
    def __init__(self):
        self.root = None
    
    def insert(self , key):
        if not self.root: # 루트 노트가 없는 경우
            self.root = Node(key)
        else:
            cur = self.root
            while 1:
                if key < cur.val:
                    if cur.left:
                        cur = cur.left
                    else:
                        cur.left = Node(key)
                        break
                else:
                    if cur.right:
                        cur = cur.right
                    else:
                        cur.right = Node(key)
                        break
    
    def search(self , key):
        cur = self.root
        if not cur: # 루트 노드가 없는 경우
            return False
        else: # 루트 노드 존재
            while cur: # 리프 노드가 나올 때까지 반복
                if key < cur.val:
                    cur = cur.left
                elif key > cur.val:
                    cur = cur.right
                else:
                    return True
            return False

def solution(lst , search_lst):
    bst = BST()
    
    for key in lst:
        bst.insert(key)
    result = []
    
    for search_val in search_lst:
        result.append(bst.search(search_val))
    return result

print(solution([5, 3, 8, 4, 2, 1, 7, 10], [1, 2, 5, 6]))
print(solution([1, 3, 5, 7, 9], [2, 4, 6, 8, 10]))


        
        
        
                
            
                
            
    
    
        