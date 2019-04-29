def selection_sort(l: list) -> None:
    for slot in range(len(l) - 1, 1, -1):
        max_i = 0
        for temp in range(1, slot):
            if l[max_i] < l[temp]:
                max_i = temp
        temp = l[max_i]
        l[max_i] = l[slot]
        l[slot] = temp
