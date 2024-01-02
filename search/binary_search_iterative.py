def binary_search_iterative(arr, s):
    """
    Find the s in the array using the binary search iterative approach.
    Time Complexity: O(log(N))
    Space Complexity: O(1)
    :param arr:
    :param s:
    :return:
    """
    start = 0
    end = len(arr) - 1
    while start <= end:
        mid = int((start + end) / 2)
        if arr[mid] == s:
            return mid
        elif arr[mid] > s:
            end = mid - 1
        else:
            start = mid + 1

    return -1


if __name__ == "__main__":
    test_arr_1 = [10, 20, 30, 40, 50, 60]
    test_arr_2 = [5, 15, 25]
    test_arr_3 = [5, 15]
    test_arr_4 = [10, 10]

    print(binary_search_iterative(test_arr_1, 20))  # O/P = 1
    print(binary_search_iterative(test_arr_2, 25))  # O/P = 2
    print(binary_search_iterative(test_arr_3, 25))  # O/P = -1
    print(binary_search_iterative(test_arr_4, 10))  # O/P = 0 or 1
