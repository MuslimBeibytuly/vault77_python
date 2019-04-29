def bubble_sort(some_list: list) -> None:
    max_elem_i = 0
    for i in range(max_elem_i + 1, len(some_list)):
        print(some_list)
        if some_list[max_elem_i] > some_list[i]:
            temp = some_list[i]
            some_list[i] = some_list[max_elem_i]
            some_list[max_elem_i] = temp
            max_elem_i = i
