# escolhido o algoritmo merge_sort
# apresentado no curso por este
# possuir complexidade O(n log n)
# que é a performance que o requisito pedia.
# Tal complexidade se dá pois a cada iteração
# do iterável sua quantidade é diminuida pela
# metade(log n) e só depois são feitos loops
#  não aninhados(n log n)


def is_anagram(first_string, second_string):
    if not first_string or not second_string:
        return False
    first_array = list(first_string)
    second_array = list(second_string)
    sorted_first_string = "".join(merge_sort(first_array))
    sorted_second_string = "".join(merge_sort(second_array))
    if sorted_first_string == sorted_second_string:
        return True
    return False


def merge_sort(array):
    if len(array) <= 1:
        return array
    mid = len(array) // 2
    left, right = merge_sort(array[:mid]), merge_sort(array[mid:])
    return merge(left, right, array[:])


def merge(left, right, merged):

    left_cursor, right_cursor = 0, 0

    while left_cursor < len(left) and right_cursor < len(right):

        if left[left_cursor] <= right[right_cursor]:
            merged[left_cursor + right_cursor] = left[left_cursor]
            left_cursor += 1
        else:
            merged[left_cursor + right_cursor] = right[right_cursor]
            right_cursor += 1

    for left_cursor in range(left_cursor, len(left)):
        merged[left_cursor + right_cursor] = left[left_cursor]

    for right_cursor in range(right_cursor, len(right)):
        merged[left_cursor + right_cursor] = right[right_cursor]

    return merged
