import re

def main():
    pattern = r'^(\d+x\d+): (.+)$'
    presents = {}

    # parse the presents into a dictionary, taking their largest possible size for now
    with open('input') as f:
        present_dimensions = []
        regions = []
        for line in f:
            if line.strip() == "":
                presents[present_number] = present_dimensions
                present_dimensions = []
            elif line.strip()[-1] == ':':
                present_number = int(line.strip()[:-1])
            elif '#' in line:
                present_dimensions.append(len(line.strip()))
            else:
                # break regions down into width, height ints and a list of their required presents
                if (matches := re.search(pattern, line)) is not None:
                    width, height = map(int, matches.group(1).split('x'))
                    required_presents = [int(p) for p in matches.group(2).strip().split(' ')]
                    regions.append([width, height, required_presents])
                else:
                    print("Malformed line: ", line)
    # baited and switched.
    # testing merely for whether the maximum size each present could take would
    # fit laid next to each other, without any packing, is sufficent for the
    # regions given in the problem.
    total = 0
    for region in regions:
        area_available = region[0] * region[1]
        space_needed = 0
        for i, present in enumerate(region[2]):
            space_needed += (sum(presents[i]) * present)
        if space_needed <= area_available:
            total += 1
    print(total)

if __name__ == "__main__":
    main()