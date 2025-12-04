def get_grid(grid, row, col, default = '.'):
    # helper function to grab a cell's contents safely
    if row < 0 or col < 0:
        return default
    try:
        return grid[row][col]
    except IndexError:
        return default

def get_neighbors(grid, row, col):
    # function to see whether a cell is blocked or not
    clear = 0
    blocked = 0
    adjacencies = ((-1, 1), (0, 1), (1, 1), (-1, 0), (1, 0), (-1, -1), (0, -1), (1, -1))
    for adj in adjacencies:
        nr = row + adj[0]
        nc = col + adj[1]
        if get_grid(grid, nr, nc) == '.':
            clear += 1
        else:
            blocked += 1
    return clear, blocked


def main():
    total = 0
    grid = []
    with open("input") as f:
        for line in f:
            row = [c for c in line.strip()]
            grid.append(row)
    
    while True:
        old_total = total
        # for each row, then for each cell, use get_neighbors on '@' cells to see
        # if it is blocked or not. if not, add that cell to the total and clear it
        for i, row in enumerate(grid):
            for j, c in enumerate(row):
                if c == "@":
                    _, blocked = get_neighbors(grid, i, j)
                    if blocked < 4:
                        grid[i][j] = '.'
                        total += 1
        # if the old_total hasn't gone up, we've removed everything we can
        if total == old_total:
            break
    print(total)

if __name__ == '__main__':
    main()