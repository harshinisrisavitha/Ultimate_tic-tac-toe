from collections import deque


# dfs implementation

# graph=[
#     [0,1,1],
#     [1,0,0],
#     [1,0,0]
# ]


graph = [
    [0, 1, 1, 0, 0, 0],  
    [0, 0, 0, 1, 1, 0],  
    [0, 0, 0, 0, 0, 1], 
    [0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 1], 
    [0, 0, 0, 0, 0, 0],  
]




n=len(graph)
visited=[False]*n
path=[]

def dfs(graph,visited,node,path):
    visited[node]=True
    print(node)
    path.append(node)

    for i in range(n):
        if graph[node][i]!=0 and not visited[i]:
            if dfs(graph,visited,i,path):
                return True
    path.pop()
    return False

if(dfs(graph,visited,0,path)):
    print(path)


# bfs implementation


def bfs(graph,start,path):
    visited=[False]*len(graph)
    visited[start]=True
    queue=deque([start])
    path.append(start)

    while queue:
        node=queue.popleft()
        print(node)
        for i in range(len(graph)):
            if graph[node][i]!=0 and not visited[i]:
                queue.append(i)
                visited[i]=True
                path.append(i)

path=[]
bfs(graph,0,path)
print(path)



# dfid implementation

def dfs(graph,goal,node,depth,path,visited):
    if node==goal:
        path.append(node)
        return True
    if depth<0:
        return False
    visited[node]=True
    path.append(node)
    for next in range(len(graph)):
        if graph[node][next]!=0 and not visited[next]:
            if dfs(graph,goal,next,depth-1,path,visited):
                return True
            
    path.pop()
    visited[node]=False
    return False

def dfid(graph,start,goal):
    for depth in range(len(graph)+1):
        visited=[False]*len(graph)
        path=[]
        if dfs(graph,goal,start,depth,path,visited):
            return path
    return False
start=0
goal=5
path=dfid(graph,start,goal)
print(path)