from greatest_common_divisor import greatest_common_divisor_efficient


def least_common_multiple(a, b):
    """
    Find the least common multiple of a and b.
    Time Complexity: O(log (min(a,b))
        - gcd time complexity
    Space Complexity: O(c)
        - Constant space.
    :param a:  Positive integer
    :param b:  Positive integer
    :return:  Least common multiple
    """
    return int(a * b / greatest_common_divisor_efficient(a, b))


if __name__ == '__main__':
    print(least_common_multiple(4, 6))
