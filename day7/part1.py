from collections import defaultdict

def travel(grid, start, collisions=set()):
    # follow the beam down from the start. At each collision point,
    # store that point in a set of collisions and call this function
    # recursively on the top of each split beam. Return a union of
    # all collision points encountered.
    row, col = start
    next = (row+1, col)
    if grid[next] == '#':
        return collisions
    if grid[next] == "^":
        if next not in collisions:
            collisions.add(next)
            return collisions | travel(grid, (row+1, col+1), collisions) | \
                    travel(grid, (row+1, col-1), collisions)
        else:
            return collisions
    else:
        return travel(grid, (row+1, col), collisions)


coords = defaultdict(lambda:'#')
start = tuple()
# parse the row,col coordinate of each spot on the input
# into a dictionary with a key (row,col) and a value of
# the cell's contents. The dicitonary will return '#' for
# any key not established. 
with open('input') as f:
    for i,row in enumerate(f):
        for j,col in enumerate(row):
            coords[(i, j)] = col
            if col == "S":
                start = (i+1, j)
    
    splits = len(travel(coords, start))
    print(splits)