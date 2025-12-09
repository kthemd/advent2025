from itertools import combinations

def area(p1, p2):
    length = max(p1[0], p2[0]) - min(p1[0], p2[0]) + 1
    height = max(p1[1], p2[1]) - min(p1[1], p2[1]) + 1
    return length * height

with open('input') as f:
    # parse the inputs into a list of x,y points
    points = []
    for line in f:
        x, y = line.strip().split(',')
        tup = int(x),int(y)
        points.append(tup)
    
    # combine all x,y points into pairs
    pairs = list(combinations(points, 2))
    # sort pairs by area, from largest to smallest
    pairs.sort(key=lambda x: area(x[0], x[1]), reverse=True)

    # print the top result
    top = pairs[0]
    print(top)
    print(area(top[0], top[1]))
