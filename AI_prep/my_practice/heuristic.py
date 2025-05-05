import heapq





def best_fs(heuristics,node,path,cost):
    visited=set()
    queue=([heuristics[node],node,[node],0])

    while queue:
        heuristic,node,path,cost=heapq.heappop()
        visited.add(node)
        if node==goal:
            return cost,path
        for neighbour,edge_wt in graph.items():
            if neighbour not in visited:
                visited.add(neighbour)
                cost=cost+edge_wt
                heapq.heappush([heuristics[neighbour],neighbour,path+[neighbour],0])
    return float('inf'),None



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


