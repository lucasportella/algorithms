def is_palindrome_recursive(word, low_index, high_index):
    if high_index < 0:
        return False
    reversed_word = reverse(word, low_index, high_index)
    if reversed_word == word:
        return True
    return False


def reverse(word, low_index, high_index):
    if high_index == low_index:
        return word[low_index]
    return word[high_index] + reverse(word, low_index, high_index - 1)
