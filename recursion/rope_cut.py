def rope_cut(n, a, b, c):
    """
    Find the maximum sum of cuts in the provided number n.
    Time Complexity: O(3^n)
    Space Complexity: O(3^n)
    :param n: Total rope
    :param a: First cut
    :param b: Second cut
    :param c: Third cut
    :return: Maximum sum of cuts of rope(n).
    """
    if n == 0:
        return 0
    if n < 0:
        return -1

    k = max(rope_cut(n - a, a, b, c), rope_cut(n - b, a, b, c), rope_cut(n - c, a, b, c))
    if k == -1:
        return -1
    return k + 1


if __name__ == '__main__':
    print(rope_cut(9, 2, 2, 2))
    print(rope_cut(23, 12, 9, 11))
