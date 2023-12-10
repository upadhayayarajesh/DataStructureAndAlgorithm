def compute_power(x, n):
    """
    Computes the power of n to x in Log (n) time complexity.
    Time Complexity: Theta (log(n))
    Space Complexity: Theta (c)
    :param x: Positive Integer
    :param n: Positive Integer
    :return: Compute the power of n raise to the x.
    """
    res = x
    for i in range(int(n / 2)):
        res *= res
    if n % 2 != 0:
        res *= x
    return res


if __name__ == '__main__':
    print(compute_power(2, 3))
