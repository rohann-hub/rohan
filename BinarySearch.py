
## Binary search !!

def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1 

arr = [2, 3, 4, 10, 40]
target = 10
result = binary_search(arr, target)

if result != -1:
    print(f"Element found at index {result}")
else:
    print("Element not found")

## BFS ( Breadth-First Search )

from collections import deque
def bfs(graph, start):
    visited = []         
    queue = deque([start])  

    while queue:
        node = queue.popleft()  
        if node not in visited:
            visited.append(node) 
            queue.extend(graph[node])  

    return visited
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

print("BFS:", bfs(graph, 'A'))

## DFS ( Depth-First search )

def dfs(graph, start, visited=None):
    if visited is None:
        visited = [] 

    if start not in visited:
        visited.append(start) 
        for neighbor in graph[start]:  
            dfs(graph, neighbor, visited)  

    return visited
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

print("DFS:", dfs(graph, 'A'))

#### Binary Search tree (bst)
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert(self.root, value)

    def _insert(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self._insert(node.left, value)
        else:
            if node.right is None:
                node.right = Node(value)
            else:
                self._insert(node.right, value)

    def search(self, value):
        return self._search(self.root, value)

    def _search(self, node, value):
        if node is None or node.value == value:
            return node
        if value < node.value:
            return self._search(node.left, value)
        return self._search(node.right, value)

    def inorder(self):
        self._inorder(self.root)

    def _inorder(self, node):
        if node:
            self._inorder(node.left)
            print(node.value, end=" ")
            self._inorder(node.right)


if __name__ == "__main__":
    bst = BinarySearchTree()
    bst.insert(5)
    bst.insert(3)
    bst.insert(7)
    bst.insert(2)
    bst.insert(4)
    bst.insert(6)
    bst.insert(8)

    print("Inorder traversal:")
    bst.inorder()  

    print("\nSearch for 4:")
    result = bst.search(4)
    if result:
        print("Found:", result.value)  
    else:
        print("Not found")
