#!/usr/bin/env python3

def main():
    zero_count = 0
    dial = 50
    with open("input") as input:
        for line in input:
            operation = line.strip()[0]
            number = int(line.strip()[1:])

            # each rotation over 100 is always a hit, so trim the number to
            # its tens place and add the hundreds place directly to our count
            if number > 100:
                zero_count += number // 10**2 % 10
                number = number % 100
            
            # turn the dial left or right
            if operation == "L":
                dial -= number
            else:
                dial += number
            
            # if the dial is on 0 or below zero, or over 100, add to the counter
            if dial <= 0 or dial > 99:
                zero_count += 1

            # messy edge case for rolling over to the left
            if dial < 0 and abs(dial) == abs(number):
                zero_count -= 1

            # trim the number into the appropriate range again
            dial = dial % 100

if __name__ == "__main__":
    main()