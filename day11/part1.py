from collections import deque

connections = {}

with open('input') as f:
    for line in f:
        node, outputs = line.strip().split(':')
        connections[node] = outputs.strip().split(' ')
    
    # BFS search using whole paths as list elements in order
    # to find all possible paths from start -> end
    queue = deque()
    start = 'you'
    end = 'out'
    queue.append(list([start]))

    total = 0
    while queue:
        path = queue.popleft()
        current = path[-1]

        if current == end:
            total += 1
            continue
        
        for next in connections[current]:
            new_path = list(path)
            new_path.append(next)
            queue.append(new_path)
    print(total)