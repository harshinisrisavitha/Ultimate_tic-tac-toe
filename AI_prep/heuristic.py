import heapq




def best_fs(graph,start,goal,heuristics):
    que=[(heuristics[start],start,[start],0)]
    #tuple=heuristics,node,path,cost
    visited=set()

    while que:
        heuristic,node,path,cost=heapq.heappop(que)

        if node==goal:
            return cost,path
        visited.add(node)
        for neighbour,edge_wt in graph[node].items():
            if neighbour not in visited:
                new_cost=cost+edge_wt
                heapq.heappush(que,(heuristics[neighbour],neighbour,path+[neighbour],new_cost))
    return None,float('inf')





graph={
    'A':{'B':6,'C':3},
    'B':{'A':6,'D':2},
    'C':{'A':3,'D':4,'E':7},
    'D':{'B':2,'C':4,'E':1,'F':5},
    'E':{'C':7,'D':1,'F':2},
    'F':{'D':5,'E':2,'G':3},
    'G':{'F':3}
}
heuristics={
    'A':8,
    'B':6,
    'C':5,
    'D':3,
    'E':2,
    'F':1,
    'G':0
}

start='A'
goal='G'

cost,path=best_fs(graph,start,goal,heuristics)
if path:
    print(path)
    print(cost)