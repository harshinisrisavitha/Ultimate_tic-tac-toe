import heapq

def a_star(graph,heuristic,start,goal):
    n=len(graph)
    que=[(heuristic[start],0,start,[start])]
    visited=set()
    g_score=[float('inf')]*n
    g_score[start]=0

    while que:
        f,g,node,path=heapq.heappop(que)

        if node==goal:
            return path,g
        
        if node in visited:
            continue
        visited.add(node)

        for neighbour in range(n):
            cost=graph[node][neighbour]
            if cost>0 and neighbour not in visited:
                new_g=g+cost
                if new_g<g_score[neighbour]:
                    g_score[neighbour]=new_g
                    f_score=new_g+heuristic[neighbour]
                    heapq.heappush(que,(f_score,new_g,neighbour,path+[neighbour]))


graph = [
    [0, 1, 4, 0, 0],
    [1, 0, 4, 2, 7],
    [4, 4, 0, 3, 5],
    [0, 2, 3, 0, 4],
    [0, 7, 5, 4, 0]
]

# Heuristic (straight-line estimates to goal node E=4)
heuristic = [7, 6, 2, 1, 0]

start = 0  # Node A
goal = 4   # Node E

path, cost = a_star(graph, heuristic, start, goal)
node_names = ['A', 'B', 'C', 'D', 'E']
print("Path:", ' -> '.join(node_names[i] for i in path))
print("Cost:", cost)
