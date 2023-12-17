def count_set_bit(n):
    """
    Count the number of ones in an n.
    Time complexity: Theta(d) where d = num of bits from last to msb.
    Space complexity: O(c)
    :param n: Number provided
    :return: Integer for the number of ones in a number.
    """
    count = 0
    while n > 0:
        if n % 2 == 1:
            count += 1
        n = int(n / 2)
    return count


if __name__ == "__main__":
    print(count_set_bit(13))
