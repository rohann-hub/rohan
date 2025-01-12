
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


