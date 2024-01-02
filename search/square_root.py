def square_root_1(n):
    """
    Floor of square root of n
    Time Complexity: O(N^ 1/2)
    Space Complexity: O(1)
    :param n: Positive Integer
    :return: Floor of sqrt of n
    """
    i = 1
    while i * i <= n:
        i = i + 1
    return i - 1


def square_root_2(n):
    """
       Floor of square root of n
       Time Complexity: O(log (N))
       Space Complexity: O(1)
       :param n: Positive Integer
       :return: Floor of sqrt of n
       """
    low = 1
    high = n
    ans = -1
    while low <= high:
        mid = int((low + high) / 2)
        if mid * mid == n:
            return mid
        elif mid * mid > n:
            high = mid - 1
        else:
            low = mid + 1
            ans = mid
    return ans


if __name__ == '__main__':
    print(square_root_1(9))  # O/P = 3
    print(square_root_1(5))  # O/P = 2
    print(square_root_1(12))  # O/P = 3

    print(square_root_2(9))
    print(square_root_2(5))
    print(square_root_2(12))
