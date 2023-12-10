import math


def check_prime(n):
    """
    Checks if a number is prime or not
    Time Complexity: O(n)
        - Linear time
    Space Complexity: O(c)
        - Constant space
    :param n:  Positive Integer
    :return: Boolean
    """
    if n == 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False

    return True


def is_prime_efficient(n):
    """
        Checks if a number is prime or not
        Time Complexity: O(sqrt(n))
            - Square root of n
        Space Complexity: O(c)
            - Constant space
        :param n:  Positive Integer
        :return: Boolean
        """
    if n == 1:
        return False
    for i in range(2, int(math.sqrt(n))):
        if n % i == 0:
            return False

    return True


if __name__ == "__main__":
    print(check_prime(12))
    print(is_prime_efficient(13))
