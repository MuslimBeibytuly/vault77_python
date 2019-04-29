def selection_sort(l: list) -> None:
    for slot in range(len(l) - 1, 0, -1):
        min_i = 0
        for temp in range(1, slot + 1):
            if l[min_i] > l[temp]:
                min_i = temp
        temp = l[min_i]
        l[min_i] = l[slot]
        l[slot] = temp
