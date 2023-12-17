def print_1_to_n_recursion(n):
    """
    Print from one to n recursively
    Time Complexity: O(n)
    Space Complexity:O(n)
    :param n: Positive Integer greater than or equal to 1.
    :return: None
    """
    if n == 0:
        return
    print_1_to_n_recursion(n - 1)
    print(n)


if __name__ == '__main__':
    print_1_to_n_recursion(4)
