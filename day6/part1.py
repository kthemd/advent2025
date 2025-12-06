from math import prod

def main():
    problems = []
    operators = []
    total = 0

    # parse the data into lists of numbers and a list of operators
    with open('input') as f:
        for line in f:
            l = line.strip().split()
            if l[0] not in "*+":
                problems.append([int(x) for x in l])
            else:
                operators = l

    # zip the lists of numbers together
    bundled = list(zip(*problems))
    
    # zip the bundled variables together with the operator
    for nums, op in zip(bundled, operators):
        if op == "*":
            total += prod(nums)
        else:
            total += sum(nums)
    print(total)

if __name__ == '__main__':
    main()