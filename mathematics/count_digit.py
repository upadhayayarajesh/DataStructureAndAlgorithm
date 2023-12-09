def count_digit(number):
    """
    Recursive process of find the total digits in the given number.
    Args:
        number(int): Integer positive number to find the count of digit.

    Returns:
        int: Count of a digit provided in the number.

    Time Complexity: O(n)
        - Here n is the number of digits in the provided number.
    Space Complexity: o(n)
        - We can have number of digit(n) calls in out recursion calls stacks.
    """
    if number < 1:
        return 0
    else:
        return 1 + count_digit(number / 10)


def count_digit_2(number):
    """
       Loop process of find the total digits in the given number.

       Time Complexity: O(n)
            - Here n is the number of digits in the provided number.
        Space Complexity: o(n)
            - We are only saving a number total_digit variable into our program.

       Args:
           number(int): Integer positive number to find the count of digit.

       Returns:
           int: Count of a digit provided in the number.
       """
    total_digit = 0
    while number > 1:
        total_digit += 1
        number = number / 10
    return total_digit


if __name__ == "__main__":
    print(count_digit(599))
    print(count_digit_2(599))
