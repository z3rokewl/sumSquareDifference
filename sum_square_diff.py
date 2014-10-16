
def sum_square_diff():
    sum_squared = 5050 ** 2

    # to sum 1^2 + 2^2 + 3^2 ... n ^ 2:
    # n * (n + 1) * (2n + 1) / 6
    sum_squares = 100 * 101 * 201 * 1.0 / 6.0
    return sum_squared - sum_squares


def main():
    print sum_square_diff()
    return 0 

if __name__ == '__main__':
    main()