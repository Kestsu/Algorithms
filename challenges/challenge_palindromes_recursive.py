def is_palindrome_recursive(word, low_index, high_index):
    # if word is None:
    #     return False

    # low_index = 0
    # high_index = len(word) - 1

    # while low_index != high_index:
    #     if word[low_index] == word[high_index]:
    #         low_index += 1
    #         high_index -= 1
    #     else:
    #         return False
    # return True

    if low_index is None and high_index is None:
        low_index = 0
        high_index = len(word) - 1
    if word is None:
        return False
    if low_index != high_index:
        if word[low_index] == word[high_index]:
            low_index += 1
            high_index -= 1
            is_palindrome_recursive(word, low_index, high_index)
        return False
    return True


if __name__ == '__main__':
    print(is_palindrome_recursive("ABCBA", 0, 4))
