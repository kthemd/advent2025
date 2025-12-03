def main():
    total = 0
    with open("input") as f:
        for line in f:
            numbers = [int(c) for c in line.strip()]
            left = 0
            right = 0
            for n in numbers:
                if (left*10 + right) < (right * 10 + n):
                    left = right
                    right = n
                elif (left*10 + right) < (left*10 + n):
                    right = n
            total += (left*10 + right)
            print(str(f"{left}{right}"))
    print(f"Grand total: {total}")

if __name__ == "__main__":
    main()