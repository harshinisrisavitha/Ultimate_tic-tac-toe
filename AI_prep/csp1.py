from collections import deque
import copy

variables = {'A', 'B', 'C', 'D', 'E'}
domains = {
    var: ['Red', 'Green', 'Blue'] for var in variables
}

neighbours = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'E'],
    'D': ['B', 'E'],
    'E': ['B', 'C', 'D']
}


def is_valid(assignment, var, value):
    for neighbour in neighbours[var]:
        if neighbour in assignment and assignment[neighbour] == value:
            return False
    return True


def ac3(domains, neighbours):
    que = deque((xi, xj) for xi in variables for xj in neighbours[xi])

    while que:
        xi, xj = que.popleft()
        if revise(domains, xi, xj):
            if not domains[xi]:
                return False
            for xk in neighbours[xi]:
                if xk != xi:
                    que.append((xk, xi))
    return True


def revise(domains, xi, xj):
    revised = False
    to_remove = []
    for x in domains[xi]:
        if all(x == y for y in domains[xj]):
            to_remove.append(x)
    for x in to_remove:
        domains[xi].remove(x)
        revised = True
    return revised


def backtracking(assignment, local_domains):
    if len(assignment) == len(variables):
        return assignment

    unassigned = [v for v in variables if v not in assignment]
    var = unassigned[0]

    for value in local_domains[var]:
        if is_valid(assignment, var, value):
            assignment[var] = value

            new_domains = copy.deepcopy(local_domains)
            new_domains[var] = [value]

            if ac3(new_domains, neighbours):
                result = backtracking(assignment, new_domains)
                if result:
                    return result

            del assignment[var]
    return None


# Start solving
solution = backtracking({}, copy.deepcopy(domains))
if solution:
    print("Solution:")
    for k in sorted(solution.keys()):
        print(f"{k}: {solution[k]}")
else:
    print("No solution found.")
