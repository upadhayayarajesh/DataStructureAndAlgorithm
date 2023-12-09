def greatest_common_divisor_naive(a, b):
    """
    Returns the greatest common division of two positive integers.
    In other words it can be asked as, find the largest sized square that can be used to fill the whole rectangle
    formed by these two integers area.
    Time Complexity: O(min(a,b))
        - Linear time
    Space Complexity: O(c)
        -Constant time
    :param a: Positive integer
    :param b: Positive integer
    :return: GCD of two positive integers.
    """

    result = min(a, b)
    while result > 0:
        if a % result == 0 and b % result == 0:
            break
        result -= 1
    return result


def greatest_common_divisor_efficient(a, b):
    """
    Returns the greatest common division of two positive integers.
    Efficient version is called Euclidean algorithm.
    Euclidean algorithms say
        - if b be smaller than a
        - then gcd(a,b) = gcd(a-b,b)
    Time Complexity: O(log (min(a,b))
        - It's the log time as modular and minimum of two integers.
    Space Complexity: O(c)
        -Constant time
    :param a: Positive integer
    :param b: Positive integer
    :return: GCD of two positive integers.
    """
    while a != b:
        if a > b:
            a = a - b
        elif b > a:
            b = b - a

    return a


def greatest_common_divisor_efficient_optimized(a, b):
    """
    Returns the greatest common division of two positive integers.
    Euclidean algorithm
        - Optimized version of Euclidean algorithm using modular division.
    Time Complexity: O(log (min(a,b))
        - It's the log time as modular and minimum of two integers.
    Space Complexity: O(c)
        - Constant time
    :param a: Positive integer
    :param b: Positive integer
    :return: GCD of two positive integers.
    """
    if b == 0:
        return a
    else:
        greatest_common_divisor_efficient_optimized(b, a % b)
    return a


if __name__ == '__main__':
    print(greatest_common_divisor_efficient(14, 14))
