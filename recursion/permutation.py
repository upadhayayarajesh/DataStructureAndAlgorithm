def generate_permutations(string, start=0):
    """
    Time complexity: O(n!)
    Space complexity: O(n!)
    :param string: given string
    :param start: starting swapping index
    :return: None
    """
    if start == len(string) - 1:
        print(''.join(string))
    else:
        for i in range(start, len(string)):
            # Swap the current character with the character at position 'start'
            string[start], string[i] = string[i], string[start]

            # Recursively generate permutations for the remaining characters
            generate_permutations(string, start + 1)

            # Swap the characters back to restore the original order
            string[start], string[i] = string[i], string[start]


if __name__ == '__main__':
    input_string = "abc"
    input_characters = list(input_string)
    generate_permutations(input_characters)
