import logging
import doctest


def merge(input_list, left_part, right_part):
    i, j, k = 0, 0, 0
    logging.info('Inside merge part')
    while i < len(left_part) and j < len(right_part):
        logging.info('Entered i < len(left_part) and j < len(right_part) loop')
        if left_part[i] <= right_part[j]:
            input_list[k] = left_part[i]
            i = i + 1
        else:
            input_list[k] = right_part[j]
            j = j + 1
        k = k + 1
    logging.info('Out of  i < len(left_part) and j < len(right_part) loop')

    while i < len(left_part):
        logging.info('Entered i < len(left_part) loop')
        input_list[k] = left_part[i]
        i = i + 1
        k = k + 1
    logging.info('Out of i < len(left_part) loop')

    while j < len(right_part):
        logging.info('Entered j < len(right_part) loop')
        input_list[k] = right_part[j]
        j = j + 1
        k = k + 1
    logging.info('Out of j < len(right_part) loop')

    return input_list, left_part, right_part


def merge_sort(input_list):
    """Возвращает факториал числа n, которое является числом >= 0.

        Если резульатат умещается в int, возвращается int.
        Иначе возвращается long.

        >>> merge_sort([15, 13, 11, 16, 18, 69, 46, 22, 11, 10, 8, 5, 8])
        [5, 8, 8, 10, 11, 11, 13, 15, 16, 18, 22, 46, 69]
        >>> merge_sort([15, 13, 11, 16, 18, 69, 46, 22, 11, 10, 8, 5, 9])
        [5, 8, 9, 10, 11, 11, 13, 15, 16, 18, 22, 46, 69]

        """

    logging.info('Inside splitting part')
    if len(input_list) > 1:
        left_part = input_list[:len(input_list) // 2]
        right_part = input_list[len(input_list) // 2:]

        merge_sort(left_part)
        merge_sort(right_part)

        logging.info('Starting merging')
        merge(input_list, left_part, right_part)
        logging.info('Finished merging')
    return input_list

def main():
    logging.basicConfig(filename='merge_sort.log', filemode='w', level=logging.INFO)
    logging.info('Started')

    test_list = [15, 13, 11, 16, 18, 69, 46, 22, 11, 10, 8, 5, 8]
    print(test_list)

    merge_sort(test_list)
    print("return {}".format(merge_sort(test_list)))

    logging.info('Finished')


if __name__ == '__main__':
    main()
    doctest.testmod()
