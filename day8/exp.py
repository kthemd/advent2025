from itertools import combinations
import math

def dist(p1, p2):
    # simple function to calculate the distance between two three-dimensional points
    return math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2 + (p1[2] - p2[2])**2)

def main():
    # build a dictionary of 'networks' with points as keys. the values are sets,
    # beginning with only the point itself as a member.
    circuits = {}
    with open('input') as f:
        for line in f:
            x,y,z = line.strip().split(',')
            tup = int(x), int(y), int(z)
            circuits[tup] = {tup,}

    # make a list of all possible pairs of points. Sort it according to distance
    # via the above function.
    pairs = list(combinations(circuits, 2))
    pairs.sort(key=lambda p: dist(p[0],p[1]))

    
    for i, val in enumerate(pairs):
        p1, p2 = val
        for c in circuits:
            if p1 in circuits[c]: c1 = c
            if p2 in circuits[c]: c2 = c
        
        if c1 != c2:
            circuits[c1] |= circuits[c2]
            del circuits[c2]
        
        if i+1 == 1000:
            circuit_sizes = sorted([len(circuits[c]) for c in circuits], reverse=True)
            print(math.prod(circuit_sizes[:3]))
        
        if len(circuits) == 1:
            print(p1[0] * p2[0])
            break

if __name__ == '__main__':
    main()