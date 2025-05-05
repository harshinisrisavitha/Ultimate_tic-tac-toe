

def hill_climbing(start,goal):
    current=start
    path=[current]

    while True:
        neighbours=possible_moves(current)
        best_neighbour=min(neighbours,key=lambda x:misplaced_tiles(x,goal),default=None)

        print(f"H={misplaced_tiles(current,goal)}")

        if best_neighbour and misplaced_tiles(best_neighbour,goal)<misplaced_tiles(current,goal):
            current=best_neighbour
            path.append(current)

        else:
            print("stuck")
            break

        
    
