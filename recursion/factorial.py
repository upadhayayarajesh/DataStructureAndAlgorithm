def factorial(n):
    """
    Calculate the factorial of n
    Time Complexity: O(n)
    Space Complexity:O(n)
    :param n: Positive Integer
    :return: Factorial of n
    """
    if n == 0:
        return 1
    return n * factorial(n - 1)


if __name__ == '__main__':
    print(factorial(4))
