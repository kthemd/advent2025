connections = {}

with open('input') as f:
    for line in f:
        node, outputs = line.strip().split(':')
        connections[node] = outputs.strip().split(' ')

# recursively call this function on each child node until reaching
# the goal node (or the end of the graph). store the result in the
# memo dictionary
def get_all_paths(start, end, memo):
    if start == end:
            return 1

    if start in connections:
        if start not in memo:
            memo[start] = sum(get_all_paths(child, end, memo) for child in connections[start])
    else:
        memo[start] = 0
    return memo[start]

# establish a memoization table for each function call
# call get_all_paths on each necessary step of the journey
stf = {}
svr_to_fft = get_all_paths('svr','fft',stf)
ftd = {}
fft_to_dac = get_all_paths('fft','dac',ftd)
dts = {}
dac_to_svr = get_all_paths('dac','out',dts)

# the answer is the product of each of the above steps
print(svr_to_fft * fft_to_dac * dac_to_svr)