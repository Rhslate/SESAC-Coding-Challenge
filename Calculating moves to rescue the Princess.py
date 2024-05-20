def displayPathtoPrincess(n, grid):
    # Initialize positions
    m_pos = None
    p_pos = None

    # Finding the positions of 'm' (bot) and 'p' (princess)
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 'm':
                m_pos = (i, j)
            elif grid[i][j] == 'p':
                p_pos = (i, j)

    # Initialize a list to store the moves
    moves = []

    # Generate moves to get from m_pos to p_pos
    while m_pos != p_pos:
        if m_pos[0] < p_pos[0]:
            moves.append("DOWN")
            m_pos = (m_pos[0] + 1, m_pos[1])
        elif m_pos[0] > p_pos[0]:
            moves.append("UP")
            m_pos = (m_pos[0] - 1, m_pos[1])
        
        if m_pos[1] < p_pos[1]:
            moves.append("RIGHT")
            m_pos = (m_pos[0], m_pos[1] + 1)
        elif m_pos[1] > p_pos[1]:
            moves.append("LEFT")
            m_pos = (m_pos[0], m_pos[1] - 1)

    # Print the moves
    for move in moves:
        print(move)

if __name__ == "__main__":
    n = int(input().strip())
    grid = []
    for _ in range(n):
        grid.append(list(input().strip()))

    displayPathtoPrincess(n, grid)