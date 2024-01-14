class Merge_sort:
    """
    Merge sort is a stable sorting algorithm
    Sorts in O(NlogN) time and space is O(n)
    """

    def merge_func(self, arr1, left_half, right_half):
        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr1[k] = left_half[i]
                i += 1
            else:
                arr1[k] = right_half[j]
                j += 1
            k += 1
        while i < len(left_half):
            arr1[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr1[k] = right_half[j]
            j += 1
            k += 1

    def merge(self, arr1):
        """
        Time complexity : O(n log(n))
        Space complexity : O(n)
        :param arr1: Array to be sorted
        :return: Sorted array
        """
        if len(arr1) > 1:
            mid = int(len(arr1) / 2)
            left_half = arr1[:mid]
            right_half = arr1[mid:]
            self.merge(left_half)
            self.merge(right_half)
            self.merge_func(arr1, left_half, right_half)
        return arr1


if __name__ == '__main__':
    test_arr_1_1 = [5, 10, 27, 7, 45]
    merge_sort = Merge_sort()
    print(merge_sort.merge(test_arr_1_1))
