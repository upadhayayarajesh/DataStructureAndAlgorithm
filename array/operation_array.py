def delete(arr, x):
    """
    Delete an element from the array.
    Time Complexity: O(n)
    Space Complexity: O(n)
    :param arr: array
    :param x: element to be deleted
    :return: Array after deleting the element
    """
    new_arr = []
    for i in arr:
        if i == x:
            continue
        new_arr.append(i)
    return new_arr


if __name__ == '__main__':
    print(delete([1, 2, 3, 4, 5], 4))
