def first_occurrence(arr, s):
    """
    Array to search for the s element.
    Time Complexity: O(log(n))
    Space Complexity: O(1)
    :param arr: Array
    :param s: Element to be found in the array.
    :return: Index or -1
    """
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = int((low + high) / 2)
        if arr[mid] > s:
            high = mid
        elif arr[mid] < s:
            low = mid + 1
        else:
            if mid == 0 or arr[mid - 1] != s:
                return mid
            else:
                high = mid - 1
    return -1


if __name__ == "__main__":
    test_arr_1 = [5, 10, 10, 15, 15]
    test_arr_2 = [10, 10, 10]
    print(first_occurrence(test_arr_1, 15))  # O/P = 3
    print(first_occurrence(test_arr_2, 10))  # O/P = 10
