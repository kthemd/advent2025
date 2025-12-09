from itertools import combinations

def area(p1, p2):
    length = max(p1[0], p2[0]) - min(p1[0], p2[0]) + 1
    height = max(p1[1], p2[1]) - min(p1[1], p2[1]) + 1
    return length * height

def test_intersection(line1, ray):
    # function to test for whether one line segment intersects with another
    # for the purposes of this exercise, we only care for overlapping lines,
    # we do not mind if lines share exactly one point i.e. corners and Ts
    start1, end1 = line1
    start2, end2 = ray

    # if 3 x or y positions are the same, there won't be an overlap so we
    # can exit early.
    if start1[0] == end1[0] == end2[0]:
        return False
    if start1[1] == end1[1] == end2[1]:
        return False

    # function to calculate the cross product of three points
    def orientation(p1, p2, p3):
        x1, y1 = p1
        x2, y2 = p2
        x3, y3 = p3
        result = ((y2 - y1) * (x3 - x2)) - ((x2 - x1) * (y3 - y2))
        if result == 0:
            return 0
        elif result > 0:
            return 1
        else:
            return 2
        
    # get the four orientations of three points among the two lines 
    # (line1 -> each endpoint of line 2 and vice versa)
    o1 = orientation(start1, end1, start2)
    o2 = orientation(start1, end1, end2)
    o3 = orientation(start2, end2, start1)
    o4 = orientation(start2, end2, end1)

    # if both pairs of orientations (o1 to o2, o3 to o4) are not
    # equal, an overlap has occurred.
    if o1 != o2 and o3 != o4:
        return True
    else:
        return False

with open('input') as f:
    points = []
    # parse the inputs into a list of x,y points. track an index variable 
    # and a side_length variable to find the biggest edge in our shape,
    # which is the best candidate to start our search from later.
    cur_idx = 0
    biggest_idx = 0
    biggest_size = 0
    for line in f:
        x, y = line.strip().split(',')
        tup = int(x),int(y)
        if len(points) > 1:
            cur_size = abs(points[-1][0] - tup[0]) + abs(points[-1][1] - tup[1])
            if cur_size > biggest_size:
                biggest_size = cur_size
                biggest_idx = cur_idx
        points.append(tup)
        cur_idx += 1
    
    # combine all x,y points into pairs
    pairs = list(combinations(points, 2))
    # sort pairs by area, from largest to smallest
    pairs.sort(key=lambda x: area(x[0], x[1]), reverse=True)

    # for each pair in the sorted list, construct its rectangle and see if
    # it intersects with any 
    final = False
    for pair in pairs:
        intersects = False
        p1, p2 = pair
        x1, y1 = p1
        x2, y2 = p2
        cx = round((x1 + x2) / 2)
        cy = round((y1 + y2) / 2)
        corners = (x1, y1), (x1, y2), (x2, y2), (x2, y1)

        # perform line intersections for all lines of the shape
        # start with the index of the shape's longest line, which
        # for this puzzle is the most likely point of collision.
        points_length = len(points)
        for i in range(points_length):
            point = points[(i + biggest_idx) % points_length]
            prev = points[(i + biggest_idx) % points_length - 1]
            line = (point[0], point[1]), (prev[0], prev[1])
            # if an intersection occurs for any corner, mark it as
            # invalid and break out to take the next candidate
            for corner in corners:
                ray = ((cx, cy), corner)
                if test_intersection(line, ray):
                    intersects = True
                    break
            if intersects:
                break
        if not intersects:
            final = pair
            break
    print(area(final[0], final[1]))