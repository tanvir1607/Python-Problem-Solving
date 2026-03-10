def sum_of_digits(x):
    total = 0
    while x:
        total += x % 10
        x //= 10
    return total


def main():
    test = int(input())
    for _ in range(test):
        x = int(input())
        cnt = 0
        for y in range(x + 1, x + 81 + 1):
            if y - sum_of_digits(y) == x:
                cnt += 1
        print(cnt)


if __name__ == "__main__":
    main()