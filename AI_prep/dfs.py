
def dfs(node,visited,matrix):
    visited[node]=True
    print(node,end=" ")
    for neighbours in range(3):
        if matrix[node][neighbours]==1 and not visited[neighbours]:
            dfs(neighbours,visited,matrix)


matrix=[
    [0,1,1],
    [1,0,0],
    [1,0,0]
]

visited=[False]*len(matrix)
dfs(0,visited,matrix)