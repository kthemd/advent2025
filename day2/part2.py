#!/usr/bin/env python3
import re

def main():
    answer = 0
    match = r"^(\d+)\1+$"
    with open("input") as f:
        # split the comma-separated list into ranges
        sequences = f.read().strip().split(',')
        # for each range, get the start and end
        for seq in sequences:
            start, end = seq.split('-')
            # for each number in the range, check for duplication
            for number in range(int(start), int(end)+1):
                if re.search(match, str(number)):
                    answer += number
    
    print(answer)

if __name__ == "__main__":
    main()