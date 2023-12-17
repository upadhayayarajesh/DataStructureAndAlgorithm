def sum_n_natural(n):
    """
    Returns the sum of N natural numbers
    Time Complexity: O(n)
    Space Complexity: O(n)
    :param n: Number greate than or equal to zero
    :return: Integers sum of natural numbers
    """
    if n == 0:
        return 0
    return n + sum_n_natural(n - 1)


if __name__ == '__main__':
    print(sum_n_natural(5))
