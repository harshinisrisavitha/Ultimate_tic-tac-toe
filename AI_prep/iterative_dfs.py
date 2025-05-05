# def ids_dfs(graph,node,goal,depth,visited,path):
#     if depth==0 and node==goal:
#         return path+[node]
#     if depth>0:
#         visited[node]=True
#         for neighbour in range(len(graph)):
#             if graph[node][neighbour] and not visited[neighbour]:
#                 result=ids_dfs(graph,neighbour,goal,depth-1,visited,path+[node])
#                 if result:
#                     return result
                
#     return None
    




# def ids(graph,start,goal,max_depth):
#     for depth in range(max_depth):
#         visited=[False]*len(graph)
#         result=ids_dfs(graph,start,goal,depth,visited,[])
#         if result:
#             return result
#     return None


# graph = [
#     # A B C D E
#     [0, 1, 0, 1, 0],  # A
#     [1, 0, 1, 0, 0],  # B
#     [0, 1, 0, 0, 1],  # C
#     [1, 0, 0, 0, 0],  # D
#     [0, 0, 1, 0, 0],  # E
# ]
# start = 0  # A
# goal = 4   # E
# max_depth = 4
# path = ids(graph, start, goal, max_depth)
# print("Path from A to E:", path)

def tsp_dfid(graph):
    n=len(graph)
    best_cost=float('inf')
    best_path=None

    def dfs(visited,depth,path,cost,city):
        nonlocal best_path,best_cost
        
        if len(path)==n:
            total_cost=cost+graph[city][0]
            if total_cost<best_cost:
                best_cost=total_cost
                best_path=path[:]
            return 
            
        if len(path)>=depth:
            return 
        
        visited[city]=True
        for next in range(n):
            if not visited[next] and graph[city][next]!=0:
                path.append(next)
                dfs(visited,depth,path,cost+graph[city][next],next)
                path.pop()
        visited[city]=False

    for depth in range(1,n+1):
        visited=[False]*n
        dfs(visited,depth,[0],0,0)
    return best_path,best_cost


num=int(input("Enter the no of citites present"))
print("Enter the cost of travelling fro 1 city to another")

graph=[[ 0 for i in range(num)]for j in range(num)]

for i in range(num):
    for j in range(num):
        graph[i][j]=int(input(f"graph{i}{j}: "))

for row in graph:
    print(row)

best_path,best_cost=tsp_dfid(graph)
print(best_path)
print(best_cost)

    