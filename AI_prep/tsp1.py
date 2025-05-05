from collections import deque

# using bfs
# using dfs

cities=[
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]




# def dfs(cities,visited,node,count,cost,min_cost,start):
#     if count==len(cities) and cities[node][start]:
#         return min(min_cost,cost+cities[node][start])
    
#     for city in range(len(cities)):
#         if cities[node][city]!=0 and not visited[city]:
#             visited[city]=True
#             min_cost=dfs(cities,visited,city,count+1,cost+cities[node][city],min_cost,start)
#             visited[city]=False
#     return min_cost

# def tsp():
#     n=len(cities)
#     visited=[False]*n
#     visited[0]=True
#     return dfs(cities,visited,0,1,0,float('inf'),0)

# print(tsp())


def tsp_dfs(cities,visited,node,count,cost,min_cost,start):
    if count==len(cities) and cities[node][start]:
        return min(min_cost,cost+cities[node][start])
    
    for city in range(len(cities)):
        if cities[node][city]!=0 and not visited[city]:
            visited[city]=True
            min_cost=tsp_dfs(cities,visited,city,count+1,cost+cities[node][city],min_cost,start)
            visited[city]=False
        
    return min_cost


def tsp():
    n=len(cities)
    visited=[False]*n
    visited[0]=True
    return tsp_dfs(cities,visited,0,1,0,float('inf'),0)

print(tsp())