test_list = [15, 13, 11, 16, 18, 69, 46, 22, 11, 10, 8, 5, 8]
print(test_list)


def merge(input_list, left_part, right_part):
    i, j, k = 0, 0, 0
    while i < len(left_part) and j < len(right_part):
        if left_part[i] <= right_part[j]:
            input_list[k] = left_part[i]
            i = i + 1
        else:
            input_list[k] = right_part[j]
            j = j + 1
        k = k + 1

    while i < len(left_part):
        input_list[k] = left_part[i]
        i = i + 1
        k = k + 1

    while j < len(right_part):
        input_list[k] = right_part[j]
        j = j + 1
        k = k + 1

    return input_list, left_part, right_part


def merge_sort(input_list):
    if len(input_list) > 1:

        left_part = input_list[:len(input_list) // 2]
        right_part = input_list[len(input_list) // 2:]

        merge_sort(left_part)
        merge_sort(right_part)

        merge(input_list, left_part, right_part)


merge_sort(test_list)
print(test_list)
