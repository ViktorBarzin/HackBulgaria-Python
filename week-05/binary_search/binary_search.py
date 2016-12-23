def binary_search(sorted_list, start, end, search):
    mid = (start + end) // 2

    # If item at middle is equal as search, return index
    if sorted_list[mid] == search:
        return mid
    # If item at middle is bigger than search, go in left sub-array
    elif sorted_list[mid] > search:
        return binary_search(sorted_list, start, mid - 1, search)
    # If item at middle is smaller than search, go in right sub-array
    elif sorted_list[mid] < search:
        return binary_search(sorted_list, mid + 1, end, search)


def turning_point(array, start, end):
    mid = (start + end) // 2
    if mid + 1 >= len(array) or mid - 1 < 0:
        return 'None turning point'

    # If item is turning point return its index
    if array[mid - 1] < array[mid] > array[mid + 1]:
        return mid + 1
    # If item at middle is bigger than search, go in left sub-array
    elif array[mid + 1] < array[mid] < array[mid - 1]:
        return turning_point(array, start, mid - 1)
    # If item at middle is smaller than search, go in right sub-array
    elif array[mid - 1] < array[mid] < array[mid + 1]:
        return turning_point(array, mid + 1, end)


def main():
    l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    # turning_array = [1, 4, 5, 2]
    turning_array = [1, 4, 5, 6, 2]
    s = 9
    # print(binary_search(l, 0, len(l), s))
    print(turning_point(turning_array, 0, len(turning_array)))
if __name__ == '__main__':
    main()

