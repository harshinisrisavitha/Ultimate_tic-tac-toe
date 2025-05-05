from collections import deque
from itertools import product

# Define the crossword structure
domains = {
    "1A": {"TELL", "TENT", "TEST", "SELF", "SAVE", "SORT"},
    "3A": {"SERVE", "SOLVE", "SENSE", "SAVED", "ASSET", "ALERT", "ARIVE", "RINSE", "RIVAL", "RIVER"},
    "5A": {"EGG", "EAR", "EAT"},
    "1D": {"SERVE", "SOLVE", "SENSE", "SAVED", "ASSET", "ALERT", "ARIVE", "RINSE", "RIVAL", "RIVER"},
    "2D": {"SERVE", "SOLVE", "SENSE", "SAVED", "ASSET", "ALERT", "ARIVE", "RINSE", "RIVAL", "RIVER"},
    "4D": {"TELL", "TENT", "TEST", "SELF", "SAVE", "SORT"}
}

# Intersecting positions (variable1, index1, variable2, index2)
constraints = [
    ("1A", 0, "1D", 0),
    ("1A", 2, "2D", 0),
    ("1A", 3, "4D", 0),
    ("3A", 1, "1D", 3),
    ("5A", 0, "1D", 4),
    ("5A", 2, "2D", 4),
    ("3A", 3, "2D", 3),
    ("3A", 4, "4D", 3)
]

def is_consistent(word1, index1, word2, index2):
    return word1[index1] == word2[index2]

def ac3(domains, constraints):
    queue = deque(constraints)
    while queue:
        var1, index1, var2, index2 = queue.popleft()
        removed = False
        for word1 in set(domains[var1]):
            if not any(is_consistent(word1, index1, word2, index2) for word2 in domains[var2]):
                domains[var1].remove(word1)
                removed = True
        if removed:
            for (v1, i1, v2, i2) in constraints:
                if v2 == var1:
                    queue.append((v1, i1, v2, i2))
    return domains

def is_valid_assignment(assignment):
    for var1, index1, var2, index2 in constraints:
        if var1 in assignment and var2 in assignment:
            if assignment[var1][index1] != assignment[var2][index2]:
                return False
    return True

def backtrack(assignment, domains):
    if len(assignment) == len(domains):
        return assignment
   
    var = next(v for v in domains if v not in assignment)
    for word in domains[var]:
        new_assignment = assignment.copy()
        new_assignment[var] = word
        if is_valid_assignment(new_assignment):
            result = backtrack(new_assignment, domains)
            if result:
                return result
    return None

# Apply AC3 algorithm
reduced_domains = ac3(domains, constraints)

# Solve using backtracking
solution = backtrack({}, reduced_domains)

# Print solution
if solution:
    for k, v in solution.items():
        print(f"{k}: {v}")
else:
    print("No solution found")