def sorted_rotated_array_1(arr, x):
    """
    Find the element x in the sorted rotated array
    Time Complexity: O(N)
    Space Complexity: O(1)
    :param arr: Rotated sorted array
    :param x: Element to be found
    :return: index of the element in an array
    """""
    for i, v in enumerate(arr):
        if v == x:
            return i
    return -1


def sorted_rotated_array_2(arr, x):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = int((low + high) / 2)
        if arr[mid] == x:
            return mid
        elif arr[low] < arr[mid]:
            if arr[low] <= x < arr[mid]:
                high = mid - 1
            else:
                low = mid + 1
        else:
            if arr[mid] < x <= arr[high]:
                low = mid + 1
            else:
                high = mid - 1
    return -1


if __name__ == '__main__':
    test_arr_1 = [10, 20, 40, 60, 5, 8]  # O/P = 4

    print(sorted_rotated_array_2(test_arr_1, 5))
