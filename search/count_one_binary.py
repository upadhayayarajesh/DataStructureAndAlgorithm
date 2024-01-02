def count_one_binary(arr):
    """
    Find the number of ones in the binary sorted array.
    Time Complexity: O(N)
    Space Complexity: O(1)
    :param arr: Array
    :return: Integer
    """
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = int((low + high) / 2)
        if arr[mid] == 0:
            low = mid + 1
        else:
            if mid == 0 or arr[mid - 1] == 0:
                return len(arr) - mid
            else:
                high = mid - 1
    return -1


if __name__ == '__main__':
    test_arr_1 = [0, 0, 0, 1, 1, 1]
    test_arr_2 = [1, 1, 1, 1, 1, 1]

    print(count_one_binary(test_arr_1))
    print(count_one_binary(test_arr_2))
