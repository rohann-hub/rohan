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
