from factorial import factorial_iterative


def count_trailing_zero(n):
    """
    It counts the trailing zero in the factorial of n.(naive approach)
    Time Complexity: O(n)
        - factorial method and ignoring the minor checks for a while statement.
    Space Complexity: O(c)
        -Constant time
    :param n: Takes a positive integer
    :return: Trailing zeros( zero at last) in the factorial of the n.
    """
    fact = factorial_iterative(n)
    result = 0
    while fact % 10 == 0:
        result += 1
        fact = int(fact / 10)
    return result


def count_trailing_zero_efficient(n):
    """
    It counts the trailing zero in the factorial of n.(naive approach)
    Time Complexity: O(log_5(n)
        - factorial method and ignoring the minor checks for a while statement.
    Space Complexity: O(c)
        - Constant time
    :param n: Takes a positive integer
    :return: Trailing zeros( zero at last) in the factorial of the n.
    """
    five_count = 0
    while n >= 5:
        n = int(n / 5)
        five_count += n
    return five_count


if __name__ == "__main__":
    print(count_trailing_zero_efficient(251))  # 62
    print(count_trailing_zero_efficient(100))  # 25
