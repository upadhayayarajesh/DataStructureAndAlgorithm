def two_pointer_1(arr, x):
    """
    True or False if a sum of pair is equal to x
    Time complexity: O(N^2)
    Space complexity: O(1)
    :param x: Inger sum
    :param arr: Sorted array
    :return: Boolean value
    """
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] + arr[j] == x:
                return True
    return False


def two_pointer_2(arr, x):
    """
    True or False if a sum of pair is equal to x
    Time complexity: O(N)
    Space complexity: O(1)
    :param x: Inger sum
    :param arr: Sorted array
    :return: Boolean value
    """
    low = 0
    high = len(arr) - 1
    while low <= high:
        if arr[low] + arr[high] == x:
            return True
        elif arr[low] + arr[high] > x:
            high -= 1
        else:
            low += 1

    return False


if __name__ == '__main__':
    test_arr_1 = [2, 5, 8, 12, 30]

    print(two_pointer_1(test_arr_1, 17))  # O/P = True
    print(two_pointer_2(test_arr_1, 17))  # O/P = True
