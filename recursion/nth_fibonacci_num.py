def nth_fibonacci(n):
    """
     Returns the nth Fibonacci Number using recursion
     Time Complexity: O(2^n)
     Space Complexity: O(2^n)
     :param n: Positive number greate than or equal to zero.
     :return: Nth Fibonacci Number
     """
    if n <= 1:
        return n
    return nth_fibonacci(n - 1) + nth_fibonacci(n - 2)


if __name__ == '__main__':
    print(nth_fibonacci(4))
