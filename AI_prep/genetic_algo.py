import random

N=5
iterations=30
city=['A','B','C','D','E']

cost=[
    [0,12,10,19,8],
    [12,0,3,7,6],
    [10,3,0,2,20],
    [19,7,2,0,4],
    [8,6,20,4,0]
]

def generate_random_route():
    route=[i for i in range(1,N)]
    random.shuffle(route)
    return [0]+route


def fitness_cost(route):
    cal_cost=sum(cost[route[i]][route[i+1]] for i in range(N-1))
    cal_cost+=cost[route[N-1]][route[0]]
    return cal_cost


def initialize_population():
    population=[]
    for _ in range(N-1):
        route=generate_random_route()
        population.append((route,fitness_cost(route)))
    return population


def selection(population):
    return sorted(population,key=lambda x:x[1])[:2]

def crossover(best_parent1,best_parent2):
    k=N//2
    start = best_parent1[:k]
    remaining = [gene for gene in best_parent2 if gene not in start]
    child = start + remaining    
    return child,fitness_cost(child)


def mutation(child):
    i,j=random.sample(range(1,N),2)
    child[i],child[j]=child[j],child[i]
    return child,fitness_cost(child)





def genetic_algorithm():
    population=initialize_population()

    for i in range(iterations):
        best_parent1,best_parent2=selection(population)
        child=crossover(best_parent1[0],best_parent2[0])
        mutated_child=mutation(list(best_parent1[0]))

        population=[best_parent1,best_parent2,child,mutated_child]

    optimal_sol=min(population,key=lambda x:x[1])
    print("->".join(city[i] for i in optimal_sol[0]), "->", city[0])
    print(optimal_sol[1])


genetic_algorithm()