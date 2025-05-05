from queue import PriorityQueue
from itertools import permutations


def prim_MST(graph,unvisited):
    if not unvisited:
        return 0
    mst_cost=0
    visited=set()
    start=next(iter(unvisited)) #take any random node fromu nvisited
    visited.add(start)
    node_edges=[]

    for node in unvisited:
        if node!=start:
            node_edges.append((graph[start][node],start,node))
    
    while len(visited)<len(unvisited):
        node_edges=[(graph[u][v],u,v) for u in visited for v in unvisited if v not in visited]

        if not node_edges:
            break
        cost,u,v=min(node_edges)
        visited.add(v)
        mst_cost+=cost
    return mst_cost


def heuristics(graph,unvisited,start,current):
    if not unvisited:
        return graph[current][start]
    h1=min(graph[current][v] for v in unvisited)
    h2=prim_MST(graph,unvisited)
    h3=min(graph[start][v] for v in unvisited)
    return h1+h2+h3


def a_star(graph,start):
    n=len(graph)
    que=PriorityQueue()
    que.put((0,0,start,[start],set(range(n))-{start}))
    # f,g,current_node,path,unvisited

    while not que.empty():
        f,g,current,path,unvisited=que.get()

        if not unvisited:
            return path+[start],g+graph[current][start]
        
        for node in unvisited:
            new_g=g+graph[current][node]
            new_unvisited=unvisited-{node}
            h=heuristics(graph,unvisited,start,node)
            new_f=f=new_g+h
            que.put((new_f,new_g,node,path+[node],new_unvisited))
    return None,float('inf')



graph=[
    [0,12,10,19,8],
    [12,0,3,7,6],
    [10,3,0,2,20],
    [19,7,2,0,4],
    [8,6,20,4,0]
]
start=0
path,cost=a_star(graph,start)
print(path)
print(cost)