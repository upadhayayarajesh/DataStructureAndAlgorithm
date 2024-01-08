def peak_elem_arr_1(arr):
    """
    Find a Peak element in an array
    If arr[i-1] <= arr[i] >= arr[i+1] it is a peak element.
    Time Complexity: O(N)
    Space Complexity: O(1)
    :param arr: Array of Integer
    :return: Peak Element
    """
    if len(arr) == 0:
        return 0
    if arr[0] >= arr[1]:
        return 0
    if arr[len(arr) - 1] >= arr[len(arr) - 2]:
        return len(arr) - 1

    for i in range(1, len(arr) - 2):
        if arr[i - 1] >= arr[i] <= arr[i + 1]:
            return i


def peak_elem_arr_2(arr):
    """
        Find a Peak element in an array
        If arr[i-1] <= arr[i] >= arr[i+1] it is a peak element.
        Time Complexity: O(log(N))
        Space Complexity: O(1)
        :param arr: Array of Integer
        :return: Peak Element
        """
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = int((low + high) / 2)
        if (mid == 0 or arr[mid - 1] <= arr[mid]) and (mid == len(arr) - 1 or arr[mid + 1] <= arr[mid]):
            return mid
        elif mid > 0 and arr[mid - 1] >= arr[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return -1


if __name__ == '__main__':
    test_arr_1 = [5, 20, 40, 30, 20, 50, 60]  # O/P = 6 or 2

    print(peak_elem_arr_1(test_arr_1))
    print(peak_elem_arr_2(test_arr_1))
