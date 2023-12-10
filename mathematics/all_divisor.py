import math


def all_divisor_number(n):
    """
    Finds all the divisors of a number in sorted ascending order
    Time Complexity:O(n)
    Space Complexity:O(c)
    :param n:
    :return: List of all divisors
    """
    for i in range(1, n + 1):
        if n % i == 0:
            print(i)


def all_divisor_number_efficient(n):
    """
    Finds all the divisors of a number in unsorted ascending order
    Time Complexity:O(sqrt(n))
    Space Complexity:O(c)
    :param n:
    :return: List of all divisors
    """
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            print(i)
            if i != int(n / i):
                print(int(n / i))


def all_divisor_number_efficient(n):
    """
    Finds all the divisors of a number in sorted ascending order
    Time Complexity:O(sqrt(n))
    Space Complexity:O(c)
    :param n:
    :return: List of all divisors
    """
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            print(i)

    for i in range(int(math.sqrt(n)), 0, -1):
        if (n % i) == 0:
            if i != int(n/i):
                print(int(n / i))


if __name__ == '__main__':
    # all_divisor_number(15)
    # all_divisor_number(6)
    # all_divisor_number_efficient(100)
    all_divisor_number_efficient(100)
