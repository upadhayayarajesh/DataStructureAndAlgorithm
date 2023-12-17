def generate_subset(s, e, index):
    """
    Generate subset of set s
    Time Complexity: O(2^n)
    Space Complexity: O(2^n)
    :param e: current "" empty string.
    :param index: start with 0
    :param s: Set s
    :return: None
    """
    if index == len(s):
        print(e)
        return
    generate_subset(s, e, index + 1)
    generate_subset(s, e + s[index], index + 1)


if __name__ == '__main__':
    generate_subset("ABC", "", 0)
