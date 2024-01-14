class Bubble:
    """
    Stability sorting algorithm.
    """

    def bubble_sort(self, arr):
        """
        Time Complexity: O(N^2)
        Space Complexity: O(1)
        :param arr: Array to be sorted
        :return: A sorted array
        """
        length = len(arr)
        while length > 1:
            for i in range(length - 1):
                if arr[i] > arr[i + 1]:
                    arr[i], arr[i + 1] = arr[i + 1], arr[i]

            length -= 1
        return arr


if __name__ == "__main__":
    test_arr_1 = [2, 4, 5, 6, 3, 1]
    bubble_sort = Bubble()
    print(bubble_sort.bubble_sort(test_arr_1))
