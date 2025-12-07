from functools import cache

def get_grid(grid, row, col, default = '#'):
    # helper function to grab a cell's contents safely
    if row < 0 or col < 0:
        return default
    try:
        return grid[row][col]
    except IndexError:
        return default

@cache
def travel(grid, start):
    # follow the initial beam down to a collision point. From there,
    # split and follow each diverging beam. Recurse until all beams
    # have been followed to their endpoint.
    row, col = start
    next = (row+1, col)
    nr, nc = next
    if get_grid(grid, nr, nc) == '#':
        return 1
    if get_grid(grid, nr, nc) == "^":
        return travel(grid, (row+1, col+1)) + \
            travel(grid, (row+1, col-1))
    else:
        return travel(grid, next)

grid = []
start = tuple()
# parse the input and transform the list into a tuple so it becomes hashable
with open('input') as f:
    for row in f:
        grid.append([c for c in row.strip()])
    frozen_grid = tuple(tuple(x) for x in grid)
    for i,v in enumerate(frozen_grid[0]):
        if v == "S":
            start = (0,i)

    print(travel(frozen_grid, start))