def kth_bit(n, k):
    """
    Checks if the kth bits are one or not
    Time Complexity: O(log n)
    Space complexity: O(n) where n is numb of bits saved for a number.
    :param n: Number to be checked
    :param k: Digit in the binary representation of number n.
    :return: Boolean if the kth bit is one or not.
    """
    bit_array = [0] * 32
    counter = 31
    while n > 0:
        remainder = n % 2
        n = int(n / 2)
        bit_array[counter] = remainder
        counter -= 1
    if bit_array[32 - k] == 1:
        return True
    return False


if __name__ == "__main__":
    print(kth_bit(0, 3))
