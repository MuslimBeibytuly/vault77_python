def merge_sort(some_list: list) -> None:
    if len(some_list) > 1:
        print(some_list)
        # divide
        mid: int = len(some_list) // 2
        left = some_list[:mid]
        right = some_list[mid:]
        merge_sort(left)
        merge_sort(right)

        i = 0 # left
        j = 0 # right
        k = 0 # array
        
        while i < len(left) and j < len(right):
            if right[j] > left[i]:
                some_list[k] = left[i]
                i += 1
            else:
                some_list[k] = right[j]
                j += 1
            k += 1
        
        while i < len(left):
            some_list[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            some_list[k] = right[j]
            j += 1
            k += 1
        print(some_list)
