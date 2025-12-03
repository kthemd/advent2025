import timeit
def get_digit(number, place):
    return number // 10**place % 10

def main():
    total = 0
    banks = 12
    with open("input") as f:
        for line in f:
            # prepare variables for each line, and convert the line to a list of numbers
            biggest = 0
            numbers = [int(c) for c in line.strip()]
            length = len(numbers)
            for idx, val in enumerate(numbers):
                # iterate through the digits of our result, so long as there are at least
                # that many numbers remaining
                start = min(banks-1, length-idx-1)
                for step in range(start, -1, -1):
                    # extract the digit we're comparing. if the new number is larger,
                    # replace it and break out of the loop
                    digit = get_digit(biggest, step)
                    if val > digit:
                        front = (biggest // 10 ** (step + 1)) * (10 ** (step + 1))
                        biggest = front + (val * 10**step)
                        break
            #print(biggest)
            total += biggest
    print(f"Grand total: {total}")

if __name__ == "__main__":
    a = timeit.timeit(main, number=100) * 1e3
    print(round(a, 3)/100, "ms")