def palindrome(s):
    """
    Checks if the word is palindrome
    Time Complexity:O(n)
    Space Complexity:O(n)
    :param s: String
    :return: Boolean
    """

    if len(s) == 0 or len(s) == 1:
        return True
    if s[0] == s[len(s) - 1] and palindrome(s[1: len(s) - 1]):
        return True
    else:
        return False


if __name__ == "__main__":
    print(palindrome("aba"))
    print(palindrome("abaffgg"))
