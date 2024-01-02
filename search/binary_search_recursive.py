def binary_search_recursive(arr, start, end, s):
    """
        Find the s in the array using the binary search recursive approach.
        Time Complexity: O(log(N))
        Space Complexity: O(1)
        :param end: End index of array.
        :param start: Starting index for array
        :param arr:Array
        :param s: Element to be find
        :return: index of the element s if present in the array.
        """
    if start > end:
        return -1
    mid = int((start + end) / 2)
    if arr[mid] == s:
        return mid
    elif arr[mid] > s:
        return binary_search_recursive(arr, start, mid - 1, s)
    else:
        return binary_search_recursive(arr, mid + 1, end, s)


if __name__ == "__main__":
    test_arr_1 = [10, 20, 30, 40, 50, 60]
    test_arr_2 = [5, 15, 25]
    test_arr_3 = [5, 15]
    test_arr_4 = [10, 10]

    print(binary_search_recursive(test_arr_1, 0, len(test_arr_1) - 1, 20))  # O/P = 1
    print(binary_search_recursive(test_arr_2, 0, len(test_arr_2) - 1, 25))  # O/P = 2
    print(binary_search_recursive(test_arr_3, 0, len(test_arr_3) - 1, 25))  # O/P = -1
    print(binary_search_recursive(test_arr_4, 0, len(test_arr_4) - 1, 10))  # O/P = 0 or 1
