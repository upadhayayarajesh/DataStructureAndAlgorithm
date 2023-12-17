def sum_digit(n):
    """
    Returns the sum of digit on N
    Time Complexity: O(d), where d is the number of digits in n.
    Space Complexity: O(d), where d is the number of digits in n.
    :param n: Positive integer number
    :return: Sum of digits in n
    """
    if n <= 9:
        return n
    return (n % 10) + sum_digit(int(n / 10))


if __name__ == '__main__':
    print(sum_digit(253))
    print(sum_digit(10))
    print(sum_digit(9987))
