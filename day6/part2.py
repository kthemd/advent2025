from math import prod

def main():
    lines = []
    operators = []
    total = 0
    # push the strings of numbers to a list, and replace the \n
    # newline flags with ' ' a space for our iterator later
    with open('input') as f:
        for line in f:
            if "*" in line:
                operators = line.strip().split()
            else:
                lines.append(line.replace('\n,', ' '))
    
    # zip the strings of numbers together
    bundled = zip(*lines)

    # pop the operators from the list to get our current operation
    # construct numbers by getting the next character from the zip
    # until we reach a tuple of all empty strings, at which point
    # we can do the math and move on
    for op in operators:
        numbers = []
        while True:
            number = ''.join(next(bundled))
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