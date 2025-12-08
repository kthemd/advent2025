import math
import networkx as nx

def dist(p1, p2):
    # simple function to calculate the distance between two three-dimensional points
    return math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2 + (p1[2] - p2[2])**2)

def main():
    distance_cache = {}
    points = []
    # parse a list of tuples containing the x,y,z points
    with open('input') as f:
        for line in f:
            parts = line.strip().split(',')
            points.append((tuple(int(x) for x in parts)))
    # iterate through the list of points to brute force each point's
    # distances to every other point. 
    for p1 in points:
        for p2 in points:
            if p1 is not p2:
                comb = [str(p1), str(p2)]
                comb.sort()
                key = f"{comb[0]}|{comb[1]}"
                if key not in distance_cache:
                    distance = dist(p1, p2)
                    distance_cache[key] = distance
    
    # take the cached distances and convert them to a list we can sort
    distance_list = [[v, k] for k,v in distance_cache.items()]
    distance_list.sort()

    junctions = nx.Graph()

    # add the first 1000 closest junctions as connected edges in a graph
    for i in range(1000):
        p1, p2 = distance_list[i][1].split('|')
        junctions.add_edge(p1, p2)
    
    # take a list of connected nodes in the graph and sort them by size
    # multiply the length of the three largest connections
    result = [len(x) for x in nx.connected_components(junctions)]
    result.sort(reverse=True)
    print(math.prod(result[:3]))

if __name__ == '__main__':
    main()