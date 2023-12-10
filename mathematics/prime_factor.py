import math


def prime_factors(n):
    """
    Finds a list of prime factors of a number
    Time Complexity: O(sqrt(n))
    Space Complexity: O(c)
    :param n: Integer
    :return: Print a prime factors of a number
    """
    if n == 1:
        return
    for i in range(2, int(math.sqrt(n) + 1)):
        while n % i == 0:
            print(i)
            n /= i
    if n > 1:
        print(n)


if __name__ == "__main__":
    prime_factors(12)
