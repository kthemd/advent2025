#p1
beams_p1 = []
collisions = set()
# make a list of booleans sized to our input and track row, col coordinates
# as we iterate over each line. Whenever a beam hits a collision point, turn
# that beam off, enable its neighbors, and add the point to our set.
with open('input') as f:
    for row, line in enumerate(f):
        if len(beams_p1) == 0:
            beams_p1 = [False] * len(line.strip())
        for col, val in enumerate(line.strip()):
            if not beams_p1[col] and val == "S":
                beams_p1[col] = True
            if beams_p1[col] and val == "^":
                collisions.add((row, col))
                beams_p1[col] = False
                beams_p1[col+1] = True
                beams_p1[col-1] = True
    
    print(len(collisions))

#p2
beams_p2 = []
# as above, but with a list of integers set to 0 instead of booleans.
# Rather than tracking collision points, add the number of beams at
# each collision to its neighbors, then zero out that column.
with open('input') as f:
    for line in f:
        if len(beams_p2) == 0:
            beams_p2 = [0] * len(line.strip())
        for col, val in enumerate(line.strip()):
            if not beams_p2[col] and val == "S":
                beams_p2[col] += 1
            if beams_p2[col] and val == "^":
                beams_p2[col+1] += beams_p2[col]
                beams_p2[col-1] += beams_p2[col]
                beams_p2[col] = 0
    
    print(sum(beams_p2))