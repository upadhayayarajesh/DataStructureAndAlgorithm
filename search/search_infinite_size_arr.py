def search_infinite_size_arr_1(arr, x):
    """
    Finding the index of the x if present in the array or return -1
    Time Complexity: O(position of x)
    Space Complexity: O(1)
    :param arr: Array is huge, and you don't know the length of the array
    :param x: element to be search
    :return: index of the x or -1
    """
    i = 0
    while True:
        if arr[i] == x:
            return i
        if arr[i] > x:
            return -1
        i += 1


def search_infinite_size_arr_2(arr, x):
    """
        Finding the index of the x if present in the array or return -1
        Time Complexity: O(log(position of x))
        Space Complexity: O(1)
        :param arr: Array is huge, and you don't know the length of the array
        :param x: element to be search
        :return: index of the x or -1
        """
    i = 1
    while arr[i] < x:
        i *= 2
    if arr[i] == x:
        return i
    elif arr[i] > x:
        for j in range(i, int(i / 2 + 1), -1):
            if arr[j] == x:
                return j
        return -1


if __name__ == '__main__':
    test_arr_1 = [1, 2, 3, 4, 5, 6, 7, 8]  # O/P = -1
    print(search_infinite_size_arr_1(test_arr_1, 5))
    print(search_infinite_size_arr_2(test_arr_1, 5))
