#!/usr/bin/env python3

def main():
    zero_count = 0
    dial = 50
    with open("input") as input:
        for line in input:
            operation = line.strip()[0]
            number = int(line.strip()[1:])

            # apply the number to the dial's position
            if operation == "L":
                dial -= number
            else:
                dial += number
            
            # deal with out-of-bounds cases
            while dial < 0:
                dial += 100
            while dial > 99:
                dial -= 100
            
            # check if the dial has landed on zero
            if dial == 0:
                zero_count += 1
    print(zero_count)


if __name__ == "__main__":
    main()