import heapq

# Manhattan Distance Heuristic
def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

# A* Algorithm
def a_star(grid, start, target, R, C):
    open_list = []
    heapq.heappush(open_list, (0, start))
    
    came_from = {}
    g_cost = {start: 0}
    
    directions = [(-1,0), (1,0), (0,-1), (0,1)]  # up, down, left, right
    
    while open_list:
        _, current = heapq.heappop(open_list)
        
        if current == target:
            # reconstruct path
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            path.reverse()
            return path
        
        for dx, dy in directions:
            nx, ny = current[0] + dx, current[1] + dy
            
            if 0 <= nx < R and 0 <= ny < C and grid[nx][ny] == 0:
                new_cost = g_cost[current] + 1
                
                if (nx, ny) not in g_cost or new_cost < g_cost[(nx, ny)]:
                    g_cost[(nx, ny)] = new_cost
                    f_cost = new_cost + heuristic((nx, ny), target)
                    heapq.heappush(open_list, (f_cost, (nx, ny)))
                    came_from[(nx, ny)] = current
    
    return None


# Read input from file
def read_input(filename):
    with open(filename, 'r') as file:
        data = file.read().strip().split('\n')
    
    R, C = map(int, data[0].split())
    
    grid = []
    for i in range(1, R+1):
        grid.append(list(map(int, data[i].split())))
    
    sr, sc = map(int, data[R+1].split())
    tr, tc = map(int, data[R+2].split())
    
    return grid, (sr, sc), (tr, tc), R, C


# Main
def main():
    grid, start, target, R, C = read_input("input.txt")
    
    path = a_star(grid, start, target, R, C)
    
    if path:
        print(f"Path found with cost {len(path)-1} using A*")
        print("Shortest Path:", path)
    else:
        print("Path not found using A*")


if __name__ == "__main__":
    main()
