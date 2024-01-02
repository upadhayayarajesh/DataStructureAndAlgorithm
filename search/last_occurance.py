def last_occurrence(arr, s):
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
        if arr[mid] < s:
            low = mid + 1
        elif arr[mid] > s:
            high = mid - 1
        else:
            if mid == len(arr) - 1 or arr[mid + 1] != arr[mid + 1]:
                return mid
            else:
                low = mid + 1
    return -1


if __name__ == "__main__":
    test_arr_1 = [5, 10, 10, 15, 15]
    test_arr_2 = [10, 10, 10]
    print(last_occurrence(test_arr_1, 15))  # O/P = 4
    print(last_occurrence(test_arr_2, 10))  # O/P = 2
