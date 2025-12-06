from math import prod

def main():
    lines = []
    operators = []
    total = 0
    # trim newlines from the strings of numbers, and flip them
    # (for ease of popping the operator list)
    with open('input') as f:
        for line in f:
            if "*" in line:
                operators = line.strip().split()
            else:
                lines.append(line.strip('\n')[::-1])
    
    # zip the strings of numbers together
    bundled = zip(*lines)

    # pop the operators from the list to get our current operation
    # construct numbers by getting the next character from the zip
    # until we reach a tuple of all empty strings, at which point
    # we can do the math and move on
    while len(operators) > 0:
        op = operators.pop()
        numbers = []
        while True:
            try:
                number = ''.join(next(bundled))
            except StopIteration:
                number = ''
            if number.strip() == '':
                break
            numbers.append(int(number))
        if op == '*':
            total += prod(numbers)
        else:
            total += sum(numbers)
    print(total)

if __name__ == '__main__':
    main()