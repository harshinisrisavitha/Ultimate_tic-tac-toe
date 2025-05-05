from collections import deque

# Adjacency matrix implementation


def bfs(graph,source):
    n=len(graph)
    visited=[False]*n
    queue=deque([source])
    visited[source]=True
    while queue:
        node=queue.popleft()
        print(node,end=" ")
        for neighbour in range(n):
            if graph[node][neighbour] and not visited[neighbour]:
                    queue.append(neighbour)
                    visited[neighbour]=True
                
             
graph=[
     [0, 1, 1, 0, 0, 0],  
    [0, 0, 0, 1, 1, 0],  
    [0, 0, 0, 0, 0, 1], 
    [0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 1], 
    [0, 0, 0, 0, 0, 0],  
]

bfs(graph,0)

#adjacency list implemented

# def bfs(graph,start):
#     n=len(graph)
#     visited=set()
#     queue=deque([start])
#     while queue:
#         node=queue.popleft()
#         if node not in visited:
#             print(node)
#             visited.add(node)
#             queue.extend(neighbour for neighbour in graph[node] if neighbour not in visited)
        
    

# graph = {
#     'A': ['B', 'C'],
#     'B': ['D', 'E'],
#     'C': ['F'],
#     'D': [],
#     'E': ['F'],
#     'F': []
# }

# bfs(graph,'A')

      
