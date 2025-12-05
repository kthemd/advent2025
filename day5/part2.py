def enter_range(range_list, lo, hi):
    added = False
    for k,v in enumerate(range_list):
        # for ranges in the list, see if either hi or lo falls
        # within the range. if so, extend that range. if not,
        # create a new range
        if v[0] <= lo <= v[1]:
            range_list[k][1] = max(range_list[k][1], hi)
            added = True
            break
    if not added:
        range_list.append([lo, hi])


def main():
    ranges = []
    with open("input") as f:
        for line in f:
            # make the initial list of ranges and sort it
            if line.strip() == "":
                break
            else:
                lo, hi = line.strip().split('-')
                lo = int(lo)
                hi = int(hi)
                ranges.append([lo, hi])
        ranges.sort()

    # iterate over the groupings of ranges and consolidate overlapping entries
    new_ranges = []
    for item in ranges:
        lo, hi = item
        enter_range(new_ranges, lo, hi)
    ranges = new_ranges

    
    ids = sum((hi-lo+1) for lo, hi in ranges)
    print(ids)

if __name__ == '__main__':
    main()

#353507173555373