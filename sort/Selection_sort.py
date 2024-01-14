class Selection_sort:
    """
    Selection sort unstable sorting algorithm
    It does very low memory writes.
    """

    def selection(self, arr):
        """
        Time Complexity: O(n ^2)
        Space Complexity: O(1)
        :param arr: Array to be sorted
        :return: Sorted array.
        """
        for i in range(len(arr) - 1):
            min_index = i
            for j in range(i + 1, len(arr)):
                if arr[j] < arr[min_index]:
                    min_index = j
            arr[i], arr[min_index] = arr[min_index], arr[i]
        return arr


if __name__ == '__main__':
    test_arr_1 = [10, 5, 8, 20, 2, 18]
    selection_sort = Selection_sort()
    print(selection_sort.selection(test_arr_1))
