def is_palindrome(n):
    """
    It checks for palindrome number.
    Palindrome number is a number that becomes same on reversing its order.
    Time Complexity: o(d)
        - Here d is number of digits in n.
    Space Complexity: o(n)
        - Constant time.
    :param n: Takes a positive integer
    :return: Boolean whether a number is palindrome or not.
    """
    if n < 0:
        return False

    original_num = n
    result_num = 0
    while n != 0:
        result_num = (result_num * 10) + n % 10
        n = int(n / 10)

    return result_num == original_num


if __name__ == "__main__":
    print(is_palindrome(8))  # True
    print(is_palindrome(8668))  # True
    print(is_palindrome(8768))  # False
