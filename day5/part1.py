def main():
    fresh = 0
    ranges = []
    ids = []
    header = True
    with open("input") as f:
        for line in f:
            if line.strip() == "":
                header = False
            elif header == True:
                lo, hi = line.strip().split('-')
                ranges.append([int(lo), int(hi)])
            else:
                id = int(line.strip())
                ids.append(id)
    
    for id in ids:
        for range in ranges:
            if range[0] <= id <= range[1]:
                fresh += 1
                break
    print(fresh)

if __name__ == '__main__':
    main()