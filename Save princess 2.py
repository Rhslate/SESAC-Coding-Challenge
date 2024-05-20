def nextMove(N, r, c, grid):
    # Find the position of the princess
    for i in range(N):
        for j in range(N):
            if grid[i][j] == 'p':
                p_r, p_c = i, j  # Store princess position

    # Determining the move to get closer to the princess
    if r > p_r:
        print("UP")
    elif r < p_r:
        print("DOWN")
    elif c > p_c:
        print("LEFT")
    elif c < p_c:
        print("RIGHT")
        
if __name__ == "__main__":
    N = int(input().strip())
    r, c = map(int, input().strip().split())
    grid = []
    for _ in range(N):
        grid.append(list(input().strip()))

    nextMove(N, r, c, grid)