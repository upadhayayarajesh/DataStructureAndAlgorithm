def print_n_to_1_recursion(n):
    """
    Print a number n to 1 recursively
    Time Complexity: O(n)
    Space Complexity:O(n)
    :param n: Positive Integer greater than or equal to 1.
    :return: None
    """
    if n == 0:
        return
    print(n)
    print_n_to_1_recursion(n - 1)


if __name__ == '__main__':
    print_n_to_1_recursion(5)
