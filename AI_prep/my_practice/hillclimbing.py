import random

def hill_climbing(graph,heuristic,start,goal):
    current=start
    path=[current]
    visited=set([current])
    total_cost=0

    while current!=goal:
        neighbours=[(neighbour,graph[current][neighbour],heuristic[neighbour])for neighbour in range(len(graph))if graph[current][neighbour]>0 and neighbour not in visited]

        if not neighbours:
            return None,float('inf')
        
        next_node,cost,h=min(neighbours,key=lambda x:x[2])

        visited.add(next_node)
        path.append(next_node)
        total_cost+=cost
        current=next_node
    return path,total_cost



def random_restart_hill_climbing(graph, heuristic, goal, max_restarts=10):
    n = len(graph)
    best_path = None
    best_cost = float('inf')

    for _ in range(max_restarts):
        start = random.randint(0, n - 1)
        if start == goal:
            continue  # skip trivial start

        path, cost = hill_climbing(graph, heuristic, start, goal)
        if path and cost < best_cost:
            best_path = path
            best_cost = cost

    return best_path, best_cost



graph = [
    [0, 1, 4, 0, 0],
    [1, 0, 4, 2, 7],
    [4, 4, 0, 3, 5],
    [0, 2, 3, 0, 4],
    [0, 7, 5, 4, 0]
]

# Heuristic values (estimates to goal E=4)
heuristic = [7, 6, 2, 1, 0]

start = 0  # A
goal = 4   # E

path, cost = random_restart_hill_climbing(graph, heuristic, goal,max_restarts=5)
node_names = ['A', 'B', 'C', 'D', 'E']

if path:
    print("Path:", ' -> '.join(node_names[i] for i in path))
    print("Cost:", cost)
else:
    print("No path found (stuck in local maximum).")
